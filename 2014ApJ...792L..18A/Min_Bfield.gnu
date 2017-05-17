#!/usr/bin/gnuplot -persist
#
#    
#    	G N U P L O T
#    	Version 4.4 patchlevel 3
#    	last modified March 2011
#    	System: Linux 3.2.0-52-generic
#    
#    	Copyright (C) 1986-1993, 1998, 2004, 2007-2010
#    	Thomas Williams, Colin Kelley and many others
#    
#    	gnuplot home:     http://www.gnuplot.info
#    	faq, bugs, etc:   type "help seeking-assistance"
#    	immediate help:   type "help"
#    	plot window:      hit 'h'
# set terminal wxt 0
# set output
unset clip points
set clip one
unset clip two
set bar 1.000000 front
set border 31 front linetype -1 linewidth 1.000
set xdata
set ydata
set zdata
set x2data
set y2data
set timefmt x "%d/%m/%y,%H:%M"
set timefmt y "%d/%m/%y,%H:%M"
set timefmt z "%d/%m/%y,%H:%M"
set timefmt x2 "%d/%m/%y,%H:%M"
set timefmt y2 "%d/%m/%y,%H:%M"
set timefmt cb "%d/%m/%y,%H:%M"
set boxwidth
set style fill  empty border
set style rectangle back fc lt -3 fillstyle   solid 1.00 border lt -1
set style circle radius graph 0.02, first 0, 0 
set dummy x,y
set format x "% g"
set format y "% g"
set format x2 "% g"
set format y2 "% g"
set format z "% g"
set format cb "% g"
set angles radians
unset grid
set key title ""
set key inside right top vertical Right noreverse enhanced autotitles nobox
set key noinvert samplen 4 spacing 1 width 0 height 0 
set key maxcolumns 0 maxrows 0
unset label
unset arrow
set style increment default
unset style line
unset style arrow
set style histogram clustered gap 2 title  offset character 0, 0, 0
unset logscale
set offsets 0, 0, 0, 0
set pointsize 1
set pointintervalbox 1
set encoding default
unset polar
unset parametric
unset decimalsign
set view 60, 30, 1, 1
set samples 100, 100
set isosamples 10, 10
set surface
unset contour
set clabel '%8.3g'
set mapping cartesian
set datafile separator whitespace
unset hidden3d
set cntrparam order 4
set cntrparam linear
set cntrparam levels auto 5
set cntrparam points 5
set size ratio 0 1,1
set origin 0,0
set style data points
set style function lines
set xzeroaxis linetype -2 linewidth 1.000
set yzeroaxis linetype -2 linewidth 1.000
set zzeroaxis linetype -2 linewidth 1.000
set x2zeroaxis linetype -2 linewidth 1.000
set y2zeroaxis linetype -2 linewidth 1.000
set ticslevel 0.5
set mxtics default
set mytics default
set mztics default
set mx2tics default
set my2tics default
set mcbtics default
set xtics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set xtics autofreq  norangelimit
set ytics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set ytics autofreq  norangelimit
set ztics border in scale 1,0.5 nomirror norotate  offset character 0, 0, 0
set ztics autofreq  norangelimit
set nox2tics
set noy2tics
set cbtics border in scale 1,0.5 mirror norotate  offset character 0, 0, 0
set cbtics autofreq  norangelimit
set title "" 
set title  offset character 0, 0, 0 font "" norotate
set timestamp bottom 
set timestamp "" 
set timestamp  offset character 0, 0, 0 font "" norotate
set rrange [ * : * ] noreverse nowriteback  # (currently [8.98847e+307:-8.98847e+307] )
set trange [ * : * ] noreverse nowriteback  # (currently [-5.00000:5.00000] )
set urange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set vrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set xlabel "" 
set xlabel  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set x2label "" 
set x2label  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set xrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set x2range [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set ylabel "" 
set ylabel  offset character 0, 0, 0 font "" textcolor lt -1 rotate by -270
set y2label "" 
set y2label  offset character 0, 0, 0 font "" textcolor lt -1 rotate by -270
set yrange [ * : * ] noreverse nowriteback  # (currently [0.00000:100.000] )
set y2range [ * : * ] noreverse nowriteback  # (currently [0.0102030:100.000] )
set zlabel "" 
set zlabel  offset character 0, 0, 0 font "" textcolor lt -1 norotate
set zrange [ * : * ] noreverse nowriteback  # (currently [-10.0000:10.0000] )
set cblabel "" 
set cblabel  offset character 0, 0, 0 font "" textcolor lt -1 rotate by -270
set cbrange [ * : * ] noreverse nowriteback  # (currently [8.98847e+307:-8.98847e+307] )
set zero 1e-08
set lmargin  -1
set bmargin  -1
set rmargin  -1
set tmargin  -1
set locale "en_GB.UTF-8"
set pm3d explicit at s
set pm3d scansautomatic
set pm3d interpolate 1,1 flush begin noftriangles nohidden3d corners2color mean
set palette positive nops_allcF maxcolors 0 gamma 1.5 color model RGB 
set palette rgbformulae 7, 5, 15
set colorbox default
set colorbox vertical origin screen 0.9, 0.2, 0 size screen 0.05, 0.6, 0 front bdefault
set loadpath 
set fontpath 
set fit noerrorvariables



set xrange [ 1.00000 : 5.00000 ] noreverse nowriteback

a1=(19.0/12.0)
a2=(1.0/12.0)
a3=(5.0/4.0)
a4=(7.0/4.0)

f1(x)=gamma((x/4.0)+a1)*gamma((x/4.0)-a2)*gamma((x/4.0)+a3)
f2(x)=(x+1.0)*gamma((x/4.0)+a4)

a(x)=((pi**0.5)/2.0)*f1(x)/f2(x)

#print "a(1.0)",a(1.0)
#print "a(1.5)",a(1.5)
#print "a(2.0)",a(2.0)
#print "a(2.5)",a(2.5)
#print "a(3.0)",a(3.0)
#print "a(3.5)",a(3.5)
#print "a(4.0)",a(4.0)
#print "a(4.5)",a(4.5)
#print "a(5.0)",a(5.0)

#plot a(x)

alpha=0.89
p=2.0*alpha+1.0

nu_min=325.0*10**6.0
nu_max=8.5*10**9.0
nu=610.0*10**6.0

mu0=4.0*pi*10**(-7.0)
# volume filling factor
phi=0.5
# energy in protons over electrons
eta=41.0
V=phi*5.96*10**43.0
Lnu=1.07*10**9.0

H1(x)=(1.0/(a(x)*(x-2.0)))*(nu_min**((2.0-x)/2.0)-nu_max**((2.0-x)/2.0))*nu**((x-1.0)/2.0)
H2(x)=(((7.4126*10**-19.0)**(2.0-x))/(2.344*10**-25.0))*(1.253*10**37.0)**((1.0-x)/2.0)

G(x)=H1(x)*H2(x)

print "G(p) ",G(p)

# note- factor of 1e4 puts result into G
Bmin=(((3.0*mu0/2.0)*G(p)*eta*Lnu/V)**(2.0/7.0))*1e4

# note- factor of 1e7 puts result into erg
Etot=(7.0/(6.0*mu0))*V**(3.0/7.0)*((3.0*mu0/2.0)*G(p)*eta*Lnu)**(4.0/7.0)*1e7

print "Bmin (G) ",Bmin

print "Etot (erg) ",Etot

# critical Bfield value
Bcrit=4.4*10**13.0
# electron mass in eV
me=0.511*10**6.0
# radio photon energy in eV

# chose which energy to analyse (3 energy choices below)
Eg=nu*(6.63*10**-34.0)/(1.6*10**-19.0)
#Eg=nu_min*(6.63*10**-34.0)/(1.6*10**-19.0)
#Eg=nu_max*(6.63*10**-34.0)/(1.6*10**-19.0)

print "Eg (eV) ",Eg

gamma=((Eg/me)*(Bcrit/Bmin))**0.5
print "gamma ",gamma

Ee=gamma*me

# note- 1.2e4 is cooling time of 1e14 eV electron in 3muG Bfield in yrs
tcool=(1e14/Ee)*((3.0e-6)/Bmin)**2.0*1.2e4

print "tcool (yrs) ",tcool

# Larmor radius in AU- note 1e13 is 1 AU in cm
Rlar=Ee/(300.0*Bmin)/1e13

print "Rlar (AU) ",Rlar

# speed of light in AU s^-1
c=3.0*10**(-3.0)

tlar=Rlar/c

# shock velocity (km s^-1)
beta=200.0/(3.0*10**5.0)

# note- factor of 3e7 is s in yr
tacc=tlar/(beta**2.0)/3e7

print "tacc (yrs) ",tacc

#    EOF
