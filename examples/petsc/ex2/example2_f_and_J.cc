#include <cstdio>

#include "example2_f_and_J.hh"

int residual(SNES snes, Vec z, Vec f, void *ctx)
{
  printf("residual call!\n");
  int ierr;
  const double *zz;
  double *ff;

  // get the Vec's as dumb pointers
  ierr = VecGetArrayRead(z, &zz);
  ierr = VecGetArray(f, &ff);

  // get the components 
  double x = zz[0];
  double y = zz[1];

  // compute the residual
  ff[0] = x - y - 4; 
  ff[1] = x*x + y + 3;

  // restore vectors
  ierr = VecRestoreArrayRead(z, &zz);
  ierr = VecRestoreArray(f, &ff);

  return 0;
}

int jacobian(SNES snes, Vec z, Mat J, Mat B, void *ctx)
{
  printf("jacobian call!\n");
  int ierr;
  const double *zz;
  double J_a[4];

  // get the Vec's as dumb pointers
  ierr = VecGetArrayRead(z, &zz);

  // set the components 
  J_a[0] = 1;
  J_a[1] = -1;
  J_a[2] = 2*zz[0];
  J_a[3] = 1;
  int idx[2] = {0, 1};
  ierr = MatSetValues(J, 2, idx, 2, idx, J_a, INSERT_VALUES); 
  ierr = MatAssemblyBegin(J, MAT_FINAL_ASSEMBLY);
  ierr = MatAssemblyEnd(J, MAT_FINAL_ASSEMBLY);

  // restore vectors
  ierr = VecRestoreArrayRead(z, &zz);


  return 0;
}
