# MPI Tutorial

This directory contains files to support a short, three-day overview of
MPI, a standard for parallel computing on a variety of parallel computer
architectures, including multi-core laptops and clusters with 1000's of cores.
Here, the focus is limited to use of MPI with Python via the `mpi4py` model. 
Like the OpenMP lessons, this tutorial is organized by exercise.

## Exercise 1 - Hello, World

Use `mpi4py` to produce a program that displays several messages of the form
`Hello, from process 1 of 4`.  This will require acquiring the `rank` and
`size` from the `mpi4py.MPI.COMM_WORLD` communicator.

## Exercise 2 - Roger That

Use `send` and `recv` to send a string message from rank 0 to rank 1.  Confirm
receipt by printing the received message.  Then, extend to a variety of
types.

## Exercise 3 - `send` vs `Send`, etc.

What's the difference between `send` and `Send` (and `recv` and `Recv`)? Go
look at `mpi4py`'s documentation.  Then, use the exercise template to quantify
the difference.

## Exercise 4 - From One to All

Use `send` and `recv` to spread data from rank 0 to every other rank.

## Exercise 5 - A Collective Study

Run the exercise 5 code with 4 processes and determine what `bcast`, 
`gather`, `Allgather`, and `scatter` are doing.

## Exercise 6 - 2-D Jacobi Iteration

You are given a basic program that computes the temperature in a 
two-dimensional box subject to fixed boundary temperatures.  Your job
is to parallelize this code and to extract the best performance possible
using the `mpi4py` functions considered so far.


 


