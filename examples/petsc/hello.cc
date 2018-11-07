#include <cstdio>
#include <petscksp.h>
int main(int argc, char* argv[])
{
  int ierr = PetscInitialize(&argc, &argv, NULL, NULL);
  if (ierr) return ierr;
  printf("hello world!\n");
  ierr = PetscFinalize();
  return ierr;
}
