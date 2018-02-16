# This script was adapted from http://scipy.github.io/old-wiki/pages/Cookbook/FittingData


from pylab import *
from scipy import *
from scipy import optimize




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
        flux[i]=float(items[1])*1e3
        stdev[i]=float(items[2])*1e3



powerlaw = lambda x, ynorm, alpha: ynorm * (x**alpha)

# Note: all positive, non-zero data
xdata = linspace(0.1, 20.0, 5000) 
ydataN = powerlaw(xdata, 0.22, 0.6) # amp = 0.76/(8^0.6)
ydataS = powerlaw(xdata, 5.16, 0.0) # amp = 5.16/(8^0.0)
ydata = ydataN + ydataS

logx = log10(xdata)
logy = log10(ydata)

# define our (line) fitting function
fitfunc = lambda p, x: p[0] + p[1] * x
errfunc = lambda p, x, y: (y - fitfunc(p, x))

pinit = [1.0, -1.0]
out = optimize.leastsq(errfunc, pinit,
                       args=(logx, logy), full_output=1)

pfinal = out[0]
covar = out[1]

alpha = pfinal[1]
ynorm = 10.0**pfinal[0]

print 'ynorm:',ynorm, 'index', alpha






##########
# from donna
##########

a = np.vstack([logx,np.ones(len(logx))]).T
m1,c = np.linalg.lstsq(a,logy)[0]
print "ynorm: ", 10**c, "alpha: ", m1,




##########
# Plotting data
##########
clf()
errorbar(freq, flux, fmt='ko', yerr=stdev, ecolor='black', label=r'$\mathrm{Observations}$')

#loglog(xdata, powerlaw(xdata, ynorm, alpha), 'k-', label=r'$\mathrm{T\,Tau\,total\,(\alpha=-0.03)}$')
#loglog(xdata, powerlaw(xdata, 0.22, 0.6), 'b:', label=r'$\mathrm{T\,Tau\,N\,(\alpha=0.6)}$')
#loglog(xdata, powerlaw(xdata, 6.35, -0.1), 'r--', label=r'$\mathrm{T\,Tau\,S\,(\alpha=-0.1)}$')

loglog(xdata, powerlaw(xdata, ynorm, alpha), 'k-', label=r'$\mathrm{T\,Tau\,total,\,}  S_{\nu}=6.00\left(\frac{\nu}{\mathrm{8\,GHz}}\right)^{0.06}\,\mathrm{(fitted)}$')
loglog(xdata, powerlaw(xdata, 0.22, 0.6), 'b:', label=r'$\mathrm{T\,Tau\,N,\,}  S_{\nu}=0.76\left(\frac{\nu}{\mathrm{8\,GHz}}\right)^{0.6}$')
loglog(xdata, powerlaw(xdata, 5.16, 0.0), 'r--', label=r'$\mathrm{T\,Tau\,S,\,}  S_{\nu}=5.16\left(\frac{\nu}{\mathrm{8\,GHz}}\right)^{0.0}$')

legend(loc=2)
xlabel(r'$\nu\,\mathrm{(GHz)}$', fontsize=15)
ylabel(r'$S_\nu\,\mathrm{(mJy)}$', fontsize=15)
xlim(0.1, 20.0)
ylim(0.1, 100.0)
plt.xticks([1, 10], [r'$1$', r'$10$'])
plt.yticks([0.1, 1, 10], [r'$0.1$', r'$1$', r'$10$'])
title(r'$\mathrm{Combined\,spectral\,index\,based\,on\,Johnston\,et\,al.\,(2003)}$', fontsize=15)

savefig('powerlaw3_Johnston2003.eps')
show()
