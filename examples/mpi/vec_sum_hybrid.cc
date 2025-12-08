#include <cstdio>
#include <cstdlib>
#include <mpi.h>
#include <omp.h>

int main(int argc, char **argv)
{
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Global problem size; can override with command-line argument
    long long N_global = 1000000000LL;
    if (argc > 1) {
        N_global = std::atoll(argv[1]);
    }

    // Block decomposition of [0, N_global) across ranks
    long long base = N_global / size;
    long long rem  = N_global % size;

    // First 'rem' ranks get one extra element
    long long n_local = base + (rank < rem ? 1 : 0);

    // Global starting index for this rank
    long long start = rank * base + (rank < rem ? rank : rem);
    long long end   = start + n_local;   // global index end (exclusive)

    // Allocate local chunk and initialize
    double *v = new double[n_local];
    #pragma omp parallel for
    for (long long j = 0; j < n_local; ++j) {
        v[j] = static_cast<double>(start + j);
    }

    // Synchronize before timing
    MPI_Barrier(MPI_COMM_WORLD);
    double t0 = MPI_Wtime();

    ////////////////////////////////////////////////////////////////////////////
    // Sum local data using OpenMP reduction.  This is the "local work".
    double s_local = 0.0;
    #pragma omp parallel for reduction(+:s_local)
    for (long long j = 0; j < n_local; ++j) {
        s_local += v[j];
    }

    // Barrier to separate compute from any later comms (optional but nice)
    MPI_Barrier(MPI_COMM_WORLD);
    double t_local = MPI_Wtime() - t0;

    // Reduce local sums to global sum on rank 0
    double s_global = 0.0;
    MPI_Reduce(&s_local, &s_global, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    ////////////////////////////////////////////////////////////////////////////

    // Get max time across ranks (gives "slowest" rank time)
    double t_max = 0.0;
    MPI_Reduce(&t_local, &t_max, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        // Reference sum: 0 + 1 + ... + (N_global-1) = N(N-1)/2
        long double N = static_cast<long double>(N_global);
        long double s_ref = 0.5L * (N * N - N);

        std::printf("sum is   %.15e\n", s_global);
        std::printf("expected %.15Le\n", s_ref);
        std::printf("max elapsed time over %d ranks: %f s\n", size, t_max);
    }

    delete [] v;
    MPI_Finalize();
    return 0;
}
