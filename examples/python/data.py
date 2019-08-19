"""
Examples of different data structures.
"""

import sys
import numpy as np
import json
import pickle
import h5py

#%% World's simplest format: plain text?

print('arguments were: ', sys.argv)

x = input('enter something: ')


#%%

f = open('basic_numpy.py', 'r')
L = f.readlines()
f.close()

for line in L:
    if 'z[0]' in line:
        print(line)


#%% Expedite with NumPy
x = np.linspace(0, 1, 5000)
y = np.sin(x)
z = np.cos(x)

# dump to text file
np.savetxt('testnp.txt', np.array([x, y, z]).T)

x, y, z = np.loadtxt('testnp.txt', unpack=True)
#x = A[:, 0]
#y = A[:, 1]
# load it back in

np.save('my_x', x.reshape((1, len(x))))
np.savez('my_xz', x.reshape((1, len(x))))
np.savetxt('my_xtxt', x.reshape((1, len(x))))


x2 = np.load('my_x.npy')

#%% Alternatively, use binary NumPy format




#%% Consider the more complicated set of data

L = [1, 2.0, "3.0"]
D = {'a': 1, 'b': [2, 3]}
A = z.copy()

# how to store?
pickle.dump(D, open('pickle.p', 'wb'))

D2 = pickle.load(open('pickle.p', 'rb'))

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
