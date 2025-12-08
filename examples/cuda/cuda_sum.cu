// cuda_sum.cu
#include <cstdio>
#include <cstdlib>
#include <cuda_runtime.h>

// Macro's like these are super useful for debugging!  The basic idea is
// to wrap CUDA API calls and check their return values.  So, if we have
// some call like 
//     cudaXYZ(...)
// we'd never know if it returned an error message that could help 
// to explain why our code is misbehaving.  We could also write
//    cudaError_t err = cudaXYZ(...);
//    if (err != cudaSuccess) { ...handle/print error... }
// but that's tedious.  Instead, we can just write 
//    HANDLE_ERROR(cudaXYZ(...))
// once and use it everywhere.  Although we could make this a function,
// using a macro allows us to capture __FILE__ and __LINE__ info, which
// contains the file name and line number where the error occurred.
#define HANDLE_ERROR(call)                                                  \
    do {                                                                  \
        cudaError_t err = (call);                                         \
        if (err != cudaSuccess) {                                         \
            std::fprintf(stderr, "CUDA error at %s:%d: %s\n",             \
                         __FILE__, __LINE__, cudaGetErrorString(err));    \
            std::exit(EXIT_FAILURE);                                      \
        }                                                                 \
    } while (0)

// This is the kernel.  When called with <<<N, T>>>, the kernel
// is executed on a 1-D grid of N blocks, each with a set of T threads.
__global__ void sum_kernel(const double* __restrict__ v, long n, double* sum)
{
    long idx = blockIdx.x * blockDim.x + threadIdx.x;
    long stride = blockDim.x * gridDim.x;
    double local_sum = 0.0;
    for (long i = idx; i < n; i += stride) 
    {
        local_sum += v[i];
    }
    // Atomically accumulate into global sum
    atomicAdd(sum, local_sum);
}

int main(int argc, char* argv[])
{
    // Setup problem size
    long long n = 100000000LL;   // default vector length
    int blocks = 256;            // default number of blocks
    int threads_per_block = 256; // default threads per block
    if (argc > 1) {
        n = std::atoll(argv[1]);
    }
    if (argc > 2) {
        blocks = std::atoi(argv[2]);
    }
    if (blocks >  65535) {
        blocks = 65535; // maximum number of blocks in a CUDA grid
    }
    if (argc > 3) {
        threads_per_block = std::atoi(argv[3]);
    }

    // Allocate and initialize data on the HOST
    double* v_h = new double[n];
    for (long long i = 0; i < n; ++i) {
        v_h[i] = static_cast<double>(i);
    }

    // Allocate data and sum on the DEVICE.  Copy data from
    // the HOST and set initial sum to zero.
    double* v_d   = nullptr;
    double* sum_d = nullptr;
    HANDLE_ERROR(cudaMalloc(&v_d,   n * sizeof(double)));
    HANDLE_ERROR(cudaMalloc(&sum_d, sizeof(double)));
    HANDLE_ERROR(cudaMemcpy(v_d, v_h, n * sizeof(double), cudaMemcpyHostToDevice));
    double zero = 0.0;
    HANDLE_ERROR(cudaMemcpy(sum_d, &zero, sizeof(double), cudaMemcpyHostToDevice));

    // Start Timer --->
    cudaEvent_t start, stop;
    HANDLE_ERROR(cudaEventCreate(&start));
    HANDLE_ERROR(cudaEventCreate(&stop));
    HANDLE_ERROR(cudaEventRecord(start));

    // Launch kernel
    sum_kernel<<<blocks, threads_per_block>>>(v_d, n, sum_d);
    HANDLE_ERROR(cudaGetLastError());
    HANDLE_ERROR(cudaEventRecord(stop));
    HANDLE_ERROR(cudaEventSynchronize(stop));

    float elapsed_ms = 0.0f;
    HANDLE_ERROR(cudaEventElapsedTime(&elapsed_ms, start, stop));
    // <--- Stop Timer

    // Copy result back and compare to reference
    double s = 0.0;
    HANDLE_ERROR(cudaMemcpy(&s, sum_d, sizeof(double), cudaMemcpyDeviceToHost));
    double s_ref = 0.5 * (static_cast<double>(n) * static_cast<double>(n - 1));
    std::printf("sum is %.1f expected %.1f\n", s, s_ref);
    std::printf("etime (kernel only) %f ms\n", elapsed_ms);

    // Cleanup
    delete[] v_h;
    HANDLE_ERROR(cudaFree(v_d));
    HANDLE_ERROR(cudaFree(sum_d));
    HANDLE_ERROR(cudaEventDestroy(start));
    HANDLE_ERROR(cudaEventDestroy(stop));

    return 0;
}
