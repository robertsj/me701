/**

In this example, we will solve the nonlinear system

  x - y = 4  
  x^2+y = -3 

using x0=1/2 and y0=-3.

*/

#include <petscsnes.h>
#include "example2_f_and_J.hh"

int main(int argc,char **args)
{

  // Declare variables.
  SNES snes;
  KSP ksp;
  PC pc;
  Vec z, r;
  Mat J;
  int ierr;

  // Initialize PETSc.
  ierr = PetscInitialize(&argc, &args, NULL, NULL);
  
  // Set up the nonlinear solver.
  ierr = SNESCreate(PETSC_COMM_SELF, &snes);

  // Create the vectors for the solution and residual, i.e.,
  // z and r=f(z), respectively.
  ierr = VecCreateSeq(PETSC_COMM_SELF, 2, &z);
  ierr = VecDuplicate(z, &r);

  // Provide an initial guess.
  double *z_a;
  ierr = VecGetArray(z, &z_a);
  z_a[0] = 0.5;
  z_a[1] = -1.0;
  ierr = VecRestoreArray(z, &z_a);

  // Set the residual function.
  ierr = SNESSetFunction(snes, r,  residual, NULL);

  // Set the jacobian function
  ierr = SNESSetJacobian(snes, J, J, jacobian, NULL);

  // Time to solve
  ierr = SNESSolve(snes, NULL, z);

  ierr = VecView(z, PETSC_VIEWER_STDOUT_WORLD);
  
  // Clean-up time!
  ierr = VecDestroy(&z); CHKERRQ(ierr);
  ierr = VecDestroy(&r); CHKERRQ(ierr); 
  ierr = SNESDestroy(&snes);CHKERRQ(ierr);
  ierr = PetscFinalize();
  return ierr;
}

