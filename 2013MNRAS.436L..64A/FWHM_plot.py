# Need to import the plotting package:
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['text.usetex']=True
mpl.rcParams['text.latex.unicode']=True

#define some data
x = [1.98, 3.96, 5.94, 7.92, 9.90]
y = [3.69, 7.80, 10.43, 11.87, 12.42]

#x = [1.98, 3.96, 5.94, 7.92, 9.90, 56, 335]
#y = [3.69, 7.80, 10.43, 11.87, 12.42, 29.4, 175]

#error data
y_error = [0.16, 0.09, 0.11, 0.17, 0.35]

#y_error = [0.16, 0.09, 0.11, 0.17, 0.35, 0, 0]

#fit data
#fit = polyfit(x, y, 1)
#fit_fn = poly1d(fit)

#plot data
#plt.plot(x, y, 'ko', x, fit_fn(x), 'k--')
plt.plot(x, y, 'ko')
#plt.loglog(x, y, 'ko')


#plot only errorbars
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="black")

#plot additional data & fit
plt.plot(56, 29.4, 'k^')
plt.errorbar(56, 29.4, yerr=4, linestyle="None", marker="None", color="black")


#plt.loglog(56, 29.4, 'k^')
#plt.arrow(335, 175, 0.0, -0.1, fc='k', ec='k', head_width=0.2, head_length=0.1)


#plot fit
#plt.loglog([1e-2, 3], [2.23e-2, 1.78], color='k', linestyle='-')
#plt.loglog([1e-2, 3], [2.77e-2, 7.71e-1], color='k', linestyle='--')
#plt.loglog([1e-2, 3], [2.38e-2, 1.22], color='k', linestyle=':')

plt.plot([0., 60.], [2.78, 68.], color='k', linestyle='-')
plt.plot([0., 60.], [6.67, 31.57], color='k', linestyle='--')




# Add some axis labels (we are using LaTeX here)
plt.xlabel('Projected distance from source (au)', fontsize=18)
plt.ylabel('FWHM jet diameter (au)', fontsize=18)

# Set view limits
plt.xlim(0, 60)
plt.ylim(0, 35)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)


plt.show()
#plt.savefig('FWHM.png')
