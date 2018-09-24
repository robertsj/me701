"""
Examples of different data structures.
"""

import numpy as np
import json
import pickle
import h5py

#%% World's simplest format: plain text?





#%% Expedite with NumPy
x = np.linspace(0, 1)
y = np.sin(x)
z = np.cos(x)

# dump to text file

# load it back in


#%% Alternatively, use binary NumPy format




#%% Consider the more complicated set of data

L = [1, 2.0, "3.0"]
D = {'a': 1, 'b': [2, 3]}
A = z.copy()

# how to store?


#%% 

# create a test HDF5 file
name =  'mytestfile.hdf5'
f = h5py.File('mytestfile.hdf5', 'w')

# some "attributes" for the "root" group
f.attrs['file_name'] = 'mytestfile.hdf5'
f.attrs['author'] = 'roberts'

# make a new group and give it an attribute
day1 = f.create_group('day1')
day1.attrs['note'] = 'Experiments from day 1'
# add some datasets
day1.create_dataset("array", data=A)

f.close()


# open and inspect
g = h5py.File('mytestfile.hdf5', 'r')
