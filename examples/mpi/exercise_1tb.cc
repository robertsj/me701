#include <mpi.h>
#include <omp.h>
#include <iostream>
#include <sstream>
#include <string>
#include <unistd.h>
#include <string>

std::string hostname()
{
    char buf[256];
    gethostname(buf, sizeof(buf));
    buf[255] = '\0';    // just in case
    return std::string(buf);
}

int main(int argc, char* argv[])
{
    int provided;
    MPI_Init_thread(&argc, &argv, MPI_THREAD_FUNNELED, &provided);
    if (provided < MPI_THREAD_FUNNELED) {
        std::cerr << "MPI thread support too weak\n";
        MPI_Abort(MPI_COMM_WORLD, 1);
    }

    MPI_Comm comm = MPI_COMM_WORLD;
    int rank, size;
    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    // Local buffer for this rank (shared by threads)
    std::ostringstream local_stream;

    #pragma omp parallel
    {
        int tid      = omp_get_thread_num();
        int nthreads = omp_get_num_threads();

        for (int t = 0; t < nthreads; ++t) {
            if (tid == t) {
                local_stream << "Rank " << rank << ", Thread " << tid << " on host " << hostname() << "\n";
            }
            #pragma omp barrier
        }
    }

    // One string per MPI process
    std::string local_str = local_stream.str();

    // Now we serialize output by rank on process 0
    if (rank == 0) {
        // Print rank 0's own message first
        std::cout << "===== Rank 0 =====\n";
        std::cout << local_str;

        // Receive and print others in order
        for (int r = 1; r < size; ++r) {
            MPI_Status status;

            // 1) Receive length
            int len = 0;
            MPI_Recv(&len, 1, MPI_INT, r, 0, comm, &status);

            // 2) Receive the string of that length
            std::string buf(len, '\0');
            MPI_Recv(buf.data(), len, MPI_CHAR, r, 1, comm, &status);

            std::cout << "===== Rank " << r << " =====\n";
            std::cout << buf;
        }
    } else {
        // Non-root ranks send their data to rank 0
        int len = static_cast<int>(local_str.size());
        MPI_Send(&len, 1, MPI_INT, 0, 0, comm);
        MPI_Send(local_str.data(), len, MPI_CHAR, 0, 1, comm);
    }

    MPI_Finalize();
    return 0;
}
