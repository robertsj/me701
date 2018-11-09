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
  int option = 0;

  // Declare variables.
  SNES snes;
  KSP ksp;
  PC pc;
  Vec z, r;
  Mat J, J_mf;
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
  if (option == 0)
  {
    // Use the explicitly created Jacobian matrix, which is computed
    // using the function "jacobian"
    ierr = SNESSetJacobian(snes, J, J, jacobian, NULL);
  }
  else
  {
    // Otherwise, use a matrix-free Jacobian based on finite differences.  This
    // "fake" matrix is J_mf and is applied via J_mf*v ~ (f(z+e*v)-f(z))/e.
    // When the system is solved using a Krylov method, we get a Jacobian-Free
    // Newton-Krylov (JFNK) approach.  For more, see
    //    https://www.cs.odu.edu/~keyes/papers/jfnk.pdf
    ierr = MatCreateSNESMF(snes, &J_mf);
    ierr = SNESSetJacobian(snes, J_mf, J, SNESComputeJacobianDefault, NULL);
  }

  // Last chance to override behavior.
  ierr = SNESSetFromOptions(snes);

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

