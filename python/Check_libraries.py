# This script prints the version of the different python libraries installed on the device.

import sys
print('python    : {}'.format(sys.version))

import scipy
print('scipy     : {}'.format(scipy.__version__))

import numpy 
print('numpy     : {}'.format(numpy.__version__))

import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))

import pandas
print('pandas    :{}'.format(pandas.__version__))

import sklearn
print('sklearn   : {}'.format(sklearn.__version__))

import seaborn
print('seaborn   :{}'.format(seaborn.__version__))
