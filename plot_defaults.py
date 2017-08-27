#/usr/bin/env python
import matplotlib.pyplot as localpl
import matplotlib.ticker as mticker
from matplotlib import rc

rc('text', usetex=True)
rc('font', family='serif')
rc('font', serif='palatino')
rc('font', weight='medium')
rc('mathtext', default='sf')
rc("lines", markeredgewidth=1)
rc("lines", linewidth=3)
rc('axes', labelsize=30) #24
rc("axes", linewidth=2)
rc('xtick', labelsize=28)
rc('ytick', labelsize=28)
rc('xtick.major', size=13)
rc('ytick.major', size=13)
rc('xtick.minor', size=7)
rc('ytick.minor', size=7)
rc('legend', fontsize=28) #16
rc('xtick.major', pad=8)
rc('ytick.major', pad=8)

green1='#00ff00'
orange='#ffba00'


def set_ticklines(ax,major,minor):
    ticklines = ax.xaxis.get_majorticklines()
    localpl.setp(ticklines,mew=major)
    ticklines = ax.xaxis.get_minorticklines()
    localpl.setp(ticklines,mew=minor)
    ticklines = ax.yaxis.get_majorticklines()
    localpl.setp(ticklines,mew=major)
    ticklines = ax.yaxis.get_minorticklines()
    localpl.setp(ticklines,mew=minor)


def set_tick_sizes(ax, major, minor):
    for l in ax.get_xticklines() + ax.get_yticklines():
        l.set_markersize(major)
    for tick in ax.xaxis.get_minor_ticks() + ax.yaxis.get_minor_ticks():
        tick.tick1line.set_markersize(minor)
        tick.tick2line.set_markersize(minor)
    ax.xaxis.LABELPAD=10.
    ax.xaxis.OFFSETTEXTPAD=10.


