#include <mpi.h>
#include <omp.h>
#include <iostream>
#include <sstream>
#include <string>

int main(int argc, char* argv[])
{
    // Initialize MPI with thread support
    int provided;
    MPI_Init_thread(&argc, &argv, MPI_THREAD_FUNNELED, &provided);

    if (provided < MPI_THREAD_FUNNELED) {
        if (provided == MPI_THREAD_SINGLE) {
            std::cerr << "MPI does not support threads in this build.\n";
        } else {
            std::cerr << "Got weaker thread support than requested.\n";
        }
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    int rank, size;
    MPI_Comm comm = MPI_COMM_WORLD;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    #pragma omp parallel
    {
        int tid       = omp_get_thread_num();
        int nthreads  = omp_get_num_threads();

        // Build a per-thread message to keep lines intact
        std::ostringstream oss;
        oss << "Hello from MPI rank " << rank << " of " << size
            << ", OpenMP thread "    << tid   << " of " << nthreads
            << "!\n";

        // Print atomically per line (avoids character-level scrambling)
        #pragma omp critical
        {
            std::cout << oss.str();
        }
    }

    // Mimic the Python input() only on rank 0
    if (rank == 0) {
        std::cout << "blahblah";
        std::cout.flush();
        std::string dummy;
        std::getline(std::cin, dummy);
    }

    MPI_Finalize();
    return 0;
}
