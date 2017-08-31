#!/usr/bin/env python3
import pandas as pd # we'll use Pandas for reading the data
import numpy as np  # we'll use NumPy to do the heavy lifting
import matplotlib.pyplot as mpl # we'll use matplotlib to do the plotting
from plot_defaults import *


indata = pd.read_csv('Abdika_waveforms_cat.csv', sep=',',header=0)
myarr = indata.values
myarr_labels = indata.columns

wf = myarr[:,91]
time = myarr[:,-1]


myfig = mpl.figure(figsize=(12,8))
myfig.subplots_adjust(hspace=0)
myfig.subplots_adjust(left=0.14)
myfig.subplots_adjust(bottom=0.14)
myfig.subplots_adjust(top=0.97)
myfig.subplots_adjust(right=0.99)



mpl.plot(time,wf/1.0e-20,label="A5O05.5")
wf = myarr[:,68]
time = myarr[:,-1]
mpl.plot(time,wf/1.0e-20,label="A3O09.0")

mpl.xlim(-0.015,0.028)
mpl.ylim(-1.25,0.5)
mpl.xlabel("Time [s]",fontsize=30,labelpad=5)
mpl.ylabel("$h_+$ [$10^{-20}$]",fontsize=30,labelpad=7)

ax = mpl.gca()
ax.tick_params(direction='in',which='both',axis='both',bottom=True,top=True,left=True,right=True)
xminorLocator = mpl.MultipleLocator(0.0025)
xmajorLocator = mpl.MultipleLocator(0.01)
yminorLocator = mpl.MultipleLocator(0.1)
ymajorLocator = mpl.MultipleLocator(0.5)
ax.xaxis.set_major_locator(xmajorLocator)
ax.xaxis.set_minor_locator(xminorLocator)
ax.yaxis.set_minor_locator(yminorLocator)
ax.yaxis.set_major_locator(ymajorLocator)

set_ticklines(ax,2.0,2.0*0.75)


myleg = mpl.legend(loc='lower right',frameon=False)


mpl.savefig('mygw.png')
