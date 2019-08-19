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
    Circle C(2.0);


    Shape *S;
    S = new Circle(2.0);

    cout << "area of C is " << C.area() << endl;
    cout << "area of pointer to C is " << S->area() << endl;
    cout << "area of C is " << (*S).area() << endl;


	// Make a 2x4 rectangle
    Rectangle R(2, 4);

	// Make a 2x2 square
    Square SQ(2);


	// Make a vector of all the shapes, and then
	// loop through to print all their areas.
	std::vector<Shape*>  shapes;
	shapes.push_back(&C);
	shapes.push_back(&R);
	shapes.push_back(&SQ);
	for (int i = 0; i < shapes.size(); ++i)
	{
		cout << "Area of shape " << i << " is " << shapes[i]->area() << endl;
	}

	double a[4] = {1, 2, 3, 4};
    double *b;
    b = new double[4];
    for (int i = 0; i < 4; i++)
    	b[i] = 10.0*i + 1;


	// Make a Point based on *integers* and print.

	return 0;
}
