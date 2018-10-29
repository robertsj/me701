#ifndef POINT_HH_
#define POINT_HH_

#include <iostream>

class Point
{

public:

	/**
	 *  Constructor for a 3-D Cartesian-coordinate point
	 *
	 *  Arguments:
	 *     x - point along x axis
	 *     ...
	 */
	Point(double x, double y, double z);

	// Addition between two points
	Point operator +(const Point &other);

	// Multiplication by a scalar
	Point operator *(const double a);

	// Getters
	double x() const {return m_x;}
	double y() const {return m_y;}
	double z() const {return m_z;}

private:

	// Use of "m_" stands for "member" attribute/variable.
	// There are many style guides out there.  Whatever you
	// choose to do, do it consistently.
	double m_x;
	double m_y;
	double m_z;

};

// Print a Point object as part of an output stream (e.g., cout << P)
std::ostream & operator << (std::ostream &out, const Point &P);

#endif // POINT_HH_
