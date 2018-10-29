#include <iostream>
#include <vector>

// local includes
#include "shapes.hh"
#include "point.hh"
#include "tpoint.hh"

using std::cout;
using std::endl;


int main(int argc, char* argv[])
{

	// Make Points at 1,1,1 and 2,2,2
	Point P0(1, 1, 1);
	Point P1(2, 2, 2);

	// Add them
	Point P2 = P0 + P1;
	cout << "new point is " << P2 << endl;

	// Try to make a Shape
	//Shape A();

	// Make a circle of radius 2

	// Make a 2x4 rectangle

	// Make a 2x2 square



	// Make a vector of all the shapes, and then
	// loop through to print all their areas.
	std::vector<Shape*>  shapes;


	// Make a Point based on *integers* and print.

	return 0;
}
