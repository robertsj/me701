#ifndef SHAPES_HH_
#define SHAPES_HH_

//----------------------------------------------------------------------------//
class Shape
{

public:

	// Constructor
    Shape();

    // Return area of shape.
    double area();

private:

    // Member functions

    // This is a "pure virtual" function.  By declaring it
    // virtual and setting it equal to zero, we are *forcing*
    // it to be implemented in inherited classes.
    virtual double m_compute_area() = 0;


    // Member variables
};

//----------------------------------------------------------------------------//
class Circle: public Shape
{

public:

	Circle(double radius);

private:

	// Member functions
    double m_compute_area();

    // Member variables
    double m_radius;
};

//----------------------------------------------------------------------------//
class Rectangle: public Shape
{

public:

	Rectangle(double width, double height);

protected: // why?

    double m_compute_area();

    double m_width;
    double m_height;
};

//----------------------------------------------------------------------------//
class Square: public Rectangle
{

public:

	Square(double width);

};

#endif // SHAPES_HH
