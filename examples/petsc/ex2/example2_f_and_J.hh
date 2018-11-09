#include <petscsnes.h>

int residual(SNES snes, Vec x, Vec f, void *ctx);
int jacobian(SNES snes, Vec x, Mat J, Mat B, void *ctx);
