## plot_SED
##

__author__ = "Rachael Ainsworth ,rainsworth@cp.dias.ie>"
__date__ = "2015-11-11"
__version__ = "0.1"

import math
import numpy as np
import pylab as plt
import scipy as sp
import scipy.constants as const
from matplotlib.ticker import ScalarFormatter


## read data from file
#freq, flux, stdev = np.loadtxt('L1551.dat', unpack=True)

def file_len(fname):
    f=open(fname,'r')
    for i, l in enumerate(f):
        pass
    return i + 1

file = raw_input('Input file: ')
flen = file_len(file)
print '**File has ',flen,' lines'

freq=np.zeros(flen)
flux=np.zeros(flen)
stdev=np.zeros(flen)
    
indat=open(file,'r')
i=-1
while True:
        line=indat.readline()
        if not line:break
        
        items=line.split()
        i+=1
        freq[i]=float(items[0])
        flux[i]=float(items[1])
        stdev[i]=float(items[2])

## define variables from metro_totalfit2 and target source name for title


K1 = 0.000455609269858
alpha = -1.12318759235
Title = 'DG\,Tau\,counter-jet?'


x = 10.**np.linspace(1.0, 20, 5000)

xnorm = 0.4e9

y = (K1*(x/xnorm)**(alpha))



## create plot
plt.figure(1)
ax = plt.gca()
plt.loglog(x/1e9, y, 'k--')
plt.errorbar(freq, flux, fmt='ko', label="data",
             yerr=stdev, ecolor='black')
plt.errorbar(0.608, 0.00027, yerr=0.00008, ecolor='k', capsize=4, elinewidth=1, lolims=True)# 'kv', markersize=10)
plt.xlabel(r'$\nu\,\mathrm{(GHz)}$', fontsize=15)
plt.ylabel(r'$S_\nu\,\mathrm{(Jy)}$', fontsize=15)
plt.xlim(0.1, 10)
plt.ylim(1e-5, 1e-3)
plt.xticks([0.1, 1, 10], [r'$0.1$', r'$1$', r'$10$'])
plt.yticks([0.00001, 0.0001, 0.001], [r'$10^{-5}$', r'$10^{-4}$', r'$10^{-3}$'])
ax.text(0.7, 0.0006, r'$\mathrm{'+str(Title)+'}$', fontsize=25)

## save plot to file
plt.savefig('plot_spec.eps')

## display plot on screen
plt.show()
