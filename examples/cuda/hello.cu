// hello_cuda.cu
#include <cstdio>
#include <cstdlib>
#include <cuda_runtime.h>

#define CUDA_CHECK(call)                                          \
    do {                                                          \
        cudaError_t err = (call);                                 \
        if (err != cudaSuccess) {                                 \
            fprintf(stderr, "CUDA error at %s:%d: %s\n",          \
                    __FILE__, __LINE__, cudaGetErrorString(err)); \
            std::exit(EXIT_FAILURE);                              \
        }                                                         \
    } while (0)

// This is the "kernel" to be deployed on the GPU
__global__
void hello_kernel(int dev, int total_blocks, int threads_per_block)
{
    int b = blockIdx.x;
    int t = threadIdx.x;
    printf("Hello from device %d, block %d/%d, thread %d/%d\n",
           dev, b, total_blocks, t, threads_per_block);
}

int main()
{
    // Is there any CUDA device?
    int device_count = 0;
    cudaError_t err = cudaGetDeviceCount(&device_count);

    if (err != cudaSuccess || device_count == 0) {
        std::printf("No CUDA-capable GPU! Running CPU-only fallback.\n");
        std::printf("Hello from CPU!\n");
        return 0;
    }

    // Use device 0 by default
    int dev = 0;
    CUDA_CHECK(cudaSetDevice(dev));

    cudaDeviceProp prop{};
    CUDA_CHECK(cudaGetDeviceProperties(&prop, dev));

    std::printf("Using device %d: %s\n", dev, prop.name);

    // Launch a tiny kernel so output is readable
    int blocks  = 2;
    int threads = 4;

    // The "magic"
    hello_kernel<<<blocks, threads>>>(dev, blocks, threads);

    CUDA_CHECK(cudaGetLastError());       // check launch
    CUDA_CHECK(cudaDeviceSynchronize());  // wait for kernel + flush printf

    std::printf("Done.\n");
    return 0;
}
