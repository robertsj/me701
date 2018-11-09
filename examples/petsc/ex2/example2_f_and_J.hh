#include <petscsnes.h>

int residual(SNES snes, Vec z, Vec f, void *ctx);
int jacobian(SNES snes, Vec z, Mat J, Mat B, void *ctx);
