# We can define things like the compiler
CXX=g++
CXXFLAGS=-g -O0

# List all objects here
OBJ = main.o \
      point.o \
      shapes.o 

# Rule to compile all objects
%.o: %.c 
	$(CXX) -c -o $@ $< $(CXXFLAGS)

# Main program
oo_demo: $(OBJ)
	$(CXX) -o $@ $^ $(CXXFLAGS)

all: oo_demo

# clean
clean: 
	rm -f *.o oo_demo
