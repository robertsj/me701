C FILE: FIB2.F
      SUBROUTINE FIB(A,N,S)
C
C     CALCULATE FIRST N FIBONACCI NUMBERS
C
      INTEGER, INTENT(IN) :: N
      REAL*8, INTENT(OUT) :: A(N)
      CHARACTER*10 :: S
      INTEGER :: M = 2 
      DO I=1,N
         IF (I.EQ.1) THEN
            A(I) = 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(I) = 1.0D0
         ELSE 
            A(I) = A(I-1) + A(I-2)
         ENDIF
      ENDDO
      PRINT *, M
      M = M + 1
      PRINT *, "S = ", S
      END
C END FILE FIB1.F
