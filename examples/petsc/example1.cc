// This example sets up our favorite matrix of 2's and -1's and solves
// it for a right-hand side of ones.  It is a slight simplification of
// ex1.c from the PETSc KSP tutorials.

#include <petscksp.h>

int main(int argc,char **args)
{

  Mat A; // system matrix
  Vec x; // system solution
  Vec b; // system right-hand side

  KSP ksp; // the linear solver "context"
  PC pc; // the preconditioner "context"

  PetscErrorCode ierr; // int value equal to zero when all is well!

  int n = 10; // system sisze
  

  // Initialize PETSc.  What does NULL mean?
  ierr = PetscInitialize(&argc, &args, NULL, NULL); CHKERRQ(ierr);
  // What does CHKERRQ do?
  
  // Set up the system matrix
  ierr = MatCreateSeqAIJ(PETSC_COMM_SELF, n, n, 3, NULL, &A); CHKERRQ(ierr);
  MatSetUp(A); CHKERRQ(ierr);
  double values[3] = {-1.0, 2.0, -1.0};
  int columns[3];
  // Set all but the first and last rows (which only have two elements)
  int row;
  for (row = 1; row < n-1; ++row) 
  {
    columns[0] = row-1;
    columns[1] = row;
    columns[2] = row+1;
    ierr = MatSetValues(A, 1, &row, 3, columns, values, INSERT_VALUES); 
    CHKERRQ(ierr);
  }
  // Set the last row
  row  = n-1; 
  columns[0] = n-2; 
  columns[1] = n-1;
  ierr = MatSetValues(A, 1, &row, 2, columns, values, INSERT_VALUES);
  CHKERRQ(ierr);
  // Set the first row
  row = 0; 
  columns[0] = 0; 
  columns[1] = 1; 
  values[0] = 2.0; 
  values[1] = -1.0;
  ierr = MatSetValues(A, 1, &row, 2, columns, values, INSERT_VALUES);
  CHKERRQ(ierr);
  // Assemble the matrix
  ierr = MatAssemblyBegin(A, MAT_FINAL_ASSEMBLY);CHKERRQ(ierr);
  ierr = MatAssemblyEnd(A, MAT_FINAL_ASSEMBLY);CHKERRQ(ierr);

  // Set up the right-hand side and the solution
  ierr = VecCreateSeq(PETSC_COMM_SELF, n, &x); CHKERRQ(ierr);
  ierr = VecDuplicate(x, &b); CHKERRQ(ierr);
  VecSet(b, 1.0);

  // Create linear solver and solve the system.
  ierr = KSPCreate(PETSC_COMM_SELF, &ksp); CHKERRQ(ierr);
  ierr = KSPSetOperators(ksp, A, A); CHKERRQ(ierr);
  ierr = KSPGetPC(ksp, &pc); CHKERRQ(ierr);
  ierr = PCSetType(pc, PCJACOBI); CHKERRQ(ierr);
  ierr = KSPSetTolerances(ksp, 1.0e-5, PETSC_DEFAULT, PETSC_DEFAULT, PETSC_DEFAULT);
  CHKERRQ(ierr);
  // Set runtime options, e.g.,
  //     -ksp_type <type> -pc_type <type> -ksp_monitor -ksp_rtol <rtol>
  ierr = KSPSetFromOptions(ksp); CHKERRQ(ierr);
  ierr = KSPSolve(ksp, b, x); CHKERRQ(ierr);

  // View the solver information.  Could also use -ksp_view
  ierr = KSPView(ksp, PETSC_VIEWER_STDOUT_WORLD); CHKERRQ(ierr);

  // View the solution
  ierr = VecView(x, PETSC_VIEWER_STDOUT_WORLD); CHKERRQ(ierr);

  // Clean-up time!
  ierr = VecDestroy(&x); CHKERRQ(ierr);
  ierr = VecDestroy(&b); CHKERRQ(ierr); 
  ierr = MatDestroy(&A); CHKERRQ(ierr);
  ierr = KSPDestroy(&ksp);CHKERRQ(ierr);
  ierr = PetscFinalize();
  return ierr;
}


