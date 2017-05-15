"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt


x1 = np.linspace(0.0, 5.0)
x2 = np.linspace(0.0, 2.0)

y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)

#Loinard et al 2007
#dateL = [1988.831, 1988.866, 1988.874, 1989.093, 1989.098, 1990.2, 1990.257, 1990.263, 1992.88, 1995.534, 1998.178, 1998.222, 2001.052, 2003.477]
#ttauNL = [0.86, 0.87, 0.74, 1.09, 0.94, 1.07, 0.76, 0.95, 0.75, 0.9, 1.04, 0.94, 1.05, 0.72]
#ttauSL = [10.06, 4.36, 4.16, 4.98, 5.18, 4.9, 8.1, 7.61, 3.1, 5.76, 4.57, 4.67, 4.15, 5.04]
#ttauTL = [10.92, 5.23, 4.9, 6.07, 6.12, 5.97, 8.86, 8.56, 3.85, 6.66, 5.61, 5.61, 5.2, 5.76]

#Johnston et al 2003
#dateJ = [1983.7084, 1986.2546, 1988.8282, 1989.091, 1992.883, 1995.5305, 2001.0531]

dateJ5 = [1983.7084, 1986.2546, 1988.8282, 1992.883, 1995.5305]
ttauNJ5 = [0.8, 0.5, 0.5, 0.3, 0.4]
ttauSJ5 = [7.0, 4.2, 7.6, 2.8, 3.3]
ttauTJ5 = [7.8, 4.7, 8.1, 3.1, 3.7]

dateJ8 = [1988.8282, 1989.091, 1992.883, 1995.5305, 2001.0531]
ttauNJ8 = [0.8, 0.9, 0.7, 0.6, 0.8]
ttauSJ8 = [10.0, 6.0, 2.6, 4.0, 3.2]
ttauTJ8 = [10.8, 6.9, 3.3, 4.6, 4.0]

dateJ15 = [1983.7084, 1986.2546, 1988.8282, 1989.091, 1992.883, 1995.5305, 2001.0531]
ttauNJ15 = [2.2, 0.9, 2, 2.1, 1.3, 1.1, 1.5]
ttauSJ15 = [9.1, 3.5, 13.5, 5.7, 2, 3.2, 3.3]
ttauTJ15 = [11.3, 4.4, 15.5, 7.8, 3.3, 4.3, 4.8]


dateJa = [1983.7084, 1986.2546, 1988.8282, 1989.091, 1992.883, 1995.5305, 2001.0531]
ttauNJa = [0.92, 0.54, 1.26, 1.34, 1.33, 0.92, 1]
ttauSJa = [0.24, -0.17, 0.5, -0.08, -0.31, -0.03, 0.05]
ttauTJa = [0.34, -0.06, 0.59, 0.2, 0.06, 0.14, 0.29]


ax1 = plt.subplot(311)
plt.semilogy(dateL, ttauNL, 'bo-')
plt.semilogy(dateL, ttauSL, 'ro-')
plt.semilogy(dateL, ttauTL, 'ko-')
plt.title('T Tau Variability')
plt.ylabel(r'$S_{3.6\,\mathrm{cm}}\,\mathrm{(mJy)}$')
plt.yticks([1, 10], [1, 10])
plt.setp(ax1.get_xticklabels(), visible=False)

ax2 = plt.subplot(312, sharex=ax1, sharey=ax1)
plt.plot(dateJ, ttauNJ, 'bo-')
plt.plot(dateJ, ttauSJ, 'ro-')
plt.plot(dateJ, ttauTJ, 'ko-')
plt.ylabel(r'$S_{2\,\mathrm{cm}}\,\mathrm{(mJy)}$')
plt.setp(ax2.get_xticklabels(), visible=False)

ax3 = plt.subplot(312, sharex=ax1, sharey=ax1)
plt.plot(dateJ, ttauNJ, 'bo-')
plt.plot(dateJ, ttauSJ, 'ro-')
plt.plot(dateJ, ttauTJ, 'ko-')
plt.ylabel(r'$S_{2\,\mathrm{cm}}\,\mathrm{(mJy)}$')
plt.setp(ax2.get_xticklabels(), visible=False)

ax4 = plt.subplot(313, sharex=ax1)
plt.plot(dateJa, ttauNJa, 'bo-')
plt.plot(dateJa, ttauSJa, 'ro-')
plt.plot(dateJa, ttauTJa, 'ko-')
plt.xlabel('Date')
plt.ylabel(r'$\alpha$')

plt.show()
