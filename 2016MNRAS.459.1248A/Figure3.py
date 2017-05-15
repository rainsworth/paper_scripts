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

#from matplotlib import rcParams
#rcParams['ps.fonttype'] = 42



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


#Mg = float(raw_input('Mgas: '))
#Te = float(raw_input('Te: '))
#alpha = float(raw_input('alpha: '))
#K2 = float(raw_input('K2: '))
#alpha2 = float(raw_input('alpha2: '))
#Title = str(raw_input('Title: '))

K1 = 0.00160999523372
alpha = 0.22931530465
K2 = 0.120581981054
alpha2 = 3.30955713671
#Title = 'L1551\,IRS\,5'
Title = '(a)\,L1551\,IRS\,5'

#K1 = 0.0034311101882
#alpha = 0.174038883418
#K2 = 0.0281572323141
#alpha2 = 2.56081208793
#Title = 'T\,Tau'
#Title = '(b)\,T\,Tau'

#K1 = 0.000547376413828
#alpha = 0.200418654408
#K2 = 0.0345423810545
#alpha2 = 2.54766658903
#Title = 'DG\,Tau'
#Title = '(c)\,DG\,Tau'


## plot thermal dust powerlaw
x1 = 10.**np.linspace(1.0, 20, 5000)

xnorm1 = 0.323e9

a = (K1*(x1/xnorm1)**alpha)

## plot modified blackbody
x2 = 10.**np.linspace(1.0, 20, 5000)

xnorm2 = 100e9

b = (K2*(x2/xnorm2)**(alpha2))


temp = 1e4
EM = 1.67e5
tau = 8.235e-2*(temp**(-1.35))*(x2**(-0.1))*(EM)


## plot total model

x = 10.**np.linspace(1.0, 20, 5000)

y=(K1*(x/xnorm1)**alpha)
y+=(K2*(x/xnorm2)**(alpha2))





## create plot
plt.figure(1)
ax = plt.gca()
plt.loglog(x2/1e9, y, 'k-')
plt.loglog(x1/1e9, a, 'k--')
plt.loglog(x2/1e9, b, 'k:')
plt.errorbar(freq, flux, fmt='ko', label="data",
             yerr=stdev, ecolor='black')
#plt.errorbar(0.323, 0.00038, yerr=0.00008, ecolor='k', capsize=4, elinewidth=1, lolims=True)# 'kv', markersize=10)
plt.xlabel(r'$\nu\,\mathrm{(GHz)}$', fontsize=15)
plt.ylabel(r'$S_\nu\,\mathrm{(Jy)}$', fontsize=15)
plt.xlim(0.1, 1000)
plt.ylim(1e-4, 1e3)
plt.xticks([0.1, 1, 10, 100, 1000], [r'$0.1$', r'$1$', r'$10$', r'$100$', r'$1000$'])
plt.yticks([0.0001, 0.001, 0.01, 0.1, 1, 10, 100, 1000], [r'$10^{-4}$', r'$0.001$', r'$0.01$', r'$0.1$', r'$1$', r'$10$', r'$100$', r'$1000$'])
#ax.annotate('L1551', xy=(0.7,1000))
#ax.text(0.2, 1000, r'$\mathrm{L1551\,IRS\,5}$', fontsize=20)
ax.text(0.2, 100, r'$\mathrm{'+str(Title)+'}$', fontsize=25)

## save plot to file
plt.savefig('plot_SED.eps')

## display plot on screen
plt.show()
