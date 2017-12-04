
#include <mpi.h>
#include <cstdio>

int main() 
{
  // Initialize the MPI environment
  MPI_Init(NULL, NULL);
  int rank, size;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  int a=-1, b=-1;
  if (rank == 0) 
  {
    a = 1;
    //      buf count type dest tag  comm
    MPI_Send(&a, 1, MPI_INT, 1, 0, MPI_COMM_WORLD);
    //      buf count type  src tag  comm           status
    MPI_Recv(&b, 1, MPI_INT, 0, 1, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
  } 
  else if (rank == 1) 
  {
    b = 2;
    //      buf count type dest tag  comm
    MPI_Send(&b, 1, MPI_INT, 0, 1, MPI_COMM_WORLD);
    //      buf count type  src tag  comm           status
    MPI_Recv(&a, 1, MPI_INT, 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
  }
  std::printf("rank %i, a=%i, b=%i", rank, a, b);
  MPI_Finalize();
}
