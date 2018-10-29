#ifndef TPOINT_T_HH_
#define TPOINT_T_HH_

template <class T>
TPoint<T>::TPoint(T x, T y, T z)
  : m_x(x), m_y(y), m_z(z)
{
	/* ... */
}

template <class T>
TPoint<T> TPoint<T>::operator+ (const TPoint<T> &other)
{
	T x = m_x + other.x();
	T y = m_y + other.y();
	T z = m_z + other.z();
	TPoint<T> new_point(x, y, z);
	return new_point;
}

template <class T>
TPoint<T> TPoint<T>::operator* (const double a)
{
	T x = m_x * a;
	T y = m_y * a;
	T z = m_z * a;
	TPoint<T> new_point(x, y, z);
	return new_point;
}

template <class T>
std::ostream & operator << (std::ostream &out, const TPoint<T> &P)
{
    out << "[" << P.x() << "," << P.y() << "," << P.z() << "]";
    return out;
}

#endif // TPOINT_T_HH_
