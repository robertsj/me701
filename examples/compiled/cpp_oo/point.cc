#include "point.hh"

#include <iostream>

Point::Point(double x, double y, double z)
  : m_x(x), m_y(y), m_z(z)
{
	/* ... */
}

Point Point::operator+ (const Point &other)
{
	double x = m_x + other.x();
	double y = m_y + other.y();
	double z = m_z + other.z();
	Point new_point(x, y, z);
	return new_point;
}

Point Point::operator* (const double a)
{
	double x = m_x * a;
	double y = m_y * a;
	double z = m_z * a;
	Point new_point(x, y, z);
	return new_point;
}

std::ostream & operator << (std::ostream &out, const Point &P)
{
    out << "(" << P.x() << "," << P.y() << "," << P.z() << ")";
    return out;
}
