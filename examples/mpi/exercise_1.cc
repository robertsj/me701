#include <mpi.h>
#include <iostream>

int main(int argc, char* argv[]) {

    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm comm = MPI_COMM_WORLD;

    MPI_Comm_rank(comm, &rank);
    MPI_Comm_size(comm, &size);

    std::cout << "Hello, from " << rank << " of " << size << "!" << std::endl;

    if (rank == 0) {
        std::cout << "blah blah";
        std::string dummy;
        std::getline(std::cin, dummy); // pauses like Python's input()
        std::cout << "byebye\n";
    }
    MPI_Finalize();
    return 0;
}
