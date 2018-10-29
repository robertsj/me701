#include "shapes.hh"

#include <cmath>
#include <iostream>

using std::cout;
using std::endl;

//----------------------------------------------------------------------------//
// SHAPE
//----------------------------------------------------------------------------//

Shape::Shape()
{
	/* ... */
}

double Shape::area()
{
	return this->m_compute_area();
}

//----------------------------------------------------------------------------//
// CIRCLE
//----------------------------------------------------------------------------//

Circle::Circle(double radius)
  : m_radius(radius)
{
	/* ... */
}

double Circle::m_compute_area()
{
	return M_PI*m_radius*m_radius;
}

//----------------------------------------------------------------------------//
// RECTANGLE
//----------------------------------------------------------------------------//


Rectangle::Rectangle(double width, double height)
  : m_width(width), m_height(height)
{
	/* ... */
}

double Rectangle::m_compute_area()
{
	return m_width * m_height;
}


//----------------------------------------------------------------------------//
// RECTANGLE
//----------------------------------------------------------------------------//


Square::Square(double width)
  : Rectangle(width, width)
{
	/* ... */
}

