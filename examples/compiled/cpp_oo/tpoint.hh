#ifndef TPOINT_HH_
#define TPOINT_HH_

#include <iostream>

template <class T>
class TPoint
{

public:

	/**
	 *  Constructor for a 3-D Cartesian-coordinate point
	 *
	 *  Arguments:
	 *     x - point along x axis
	 *     ...
	 */
	TPoint(T x, T y, T z);

	// Addition between two points
	TPoint operator +(const TPoint<T> &other);

	// Multiplication by a scalar
	TPoint operator *(const double a);

	// Getters
	T x() const {return m_x;}
	T y() const {return m_y;}
	T z() const {return m_z;}

private:

	// Use of "m_" stands for "member" attribute/variable.
	// There are many style guides out there.  Whatever you
	// choose to do, do it consistently.
	T m_x;
	T m_y;
	T m_z;

};

// Print a Point object as part of an output stream (e.g., cout << P)
template <class T>
std::ostream & operator << (std::ostream &out, const TPoint<T> &P);

// Include the template implementations
#include "tpoint.t.hh"

#endif // TPOINT_HH_
