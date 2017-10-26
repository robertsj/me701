def savevtk(v, nx, ny, nz, filename) :
    """ Save a 3-D scalar array in VTK format. """
    f = open(filename, 'w')
    out = ""
    out += '# vtk DataFile Version 2.0\n'
    out += 'Comment goes here\n'
    out += 'ASCII\n'
    out += '\n'
    out += 'DATASET STRUCTURED_POINTS\n'
    out += 'DIMENSIONS %i %i %i\n' % (nx, ny, nz)
    out += '\n'
    out += 'ORIGIN 0.000 0.000 0.000\n'
    out += 'SPACING 1.000 1.000 1.000\n'
    out += '\n'
    out += 'POINT_DATA %i\n' % (nx*ny*nz)
    out += 'SCALARS scalars double\n'
    out += 'LOOKUP_TABLE default\n'
    out += '\n'
    for k in range(nz) :
        for j in range(ny) :
            for i in range(nx) :
                out += '%f ' % (v[i + j * ny + k * ny * nz])
            out += '\n'
    f.write(out)
    f.close()
    
if __name__ == "__main__" :
    import numpy as np
    nx = 3
    ny = 3
    nz = 3
    n  = nx*ny*nz
    x = np.linspace(0, np.pi*2, nx)
    y = np.linspace(0, 10, ny)
    z = np.linspace(0, 10, nz)    
    x, y, z = np.meshgrid(x, y, z)
    x = x.reshape((n,))
    y = y.reshape((n,))
    z = z.reshape((n,))
    v = np.sin(x)*y+z
    savevtk(v, nx, ny, nz, "test.vtk")
    
