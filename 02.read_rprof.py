#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:36:04 2024

@author: chingchen
"""

import pandas as pd
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"


figpath = '/Users/chingchen/Desktop/figure/StagYY/'
mp4 = 1
labelsize = 15
bwith = 3
fig_Nu_t = 0
fig_F_t  = 0
fig_T    = 1
fig_mobility = 0

newcolors = ['#2F4F4F','#4682B4','#CD5C5C','#708090',
              '#AE6378','#282130','#7E9680','#24788F',
              '#849DAB','#EA5E51','#35838D','#4198B9',
              '#414F67','#97795D','#6B0D47','#A80359','#52254F']
header_list = ['r','Tmean','Tmin','Tmax','vrms','vmin','vmax',
               'vzabs','vzmin','vzmax','vhrms','vhmin','vhmax',
               'etalog','etamin','etamax','elog','emin','emax',
               'slog','smin','smax','whrms','whmin','whmax',
               'wzrms','wzmin','wzmax','drms','dmin','dmax',
               'enadv','endiff','enradh','enviscdiss','enadiabh',
               'cmean','cmin','cmax','rhomean','rhomin','rhomax',
               'airmean','airmin','airmax','primmean','primmin',
               'primmax','ccmean','ccmin','ccmax','fmeltmean',
               'fmeltmin','fmeltmax','metalmean','metalmin',
               'metalmax','gsmean','gsmin','gsmax','viscdisslog',
               'viscdissmin','viscdissmax','advtot','advdesc',
               'advasc','tcondmean','tcondmin','tcondmax']

path = '/Users/chingchen/Desktop/model/'
model = 'kvar_a0105'
i=4
fig,(ax) = plt.subplots(1,1,figsize=(5,7))
ff = pd.read_csv(path+model+'/datafile/'+model+'_data_'+str(i)+'.txt',
                  sep = '\\s+',header = None,names = header_list)    
ax.scatter(ff.vhrms,ff.r,color = '#414F67',s=10)


ax.tick_params(labelsize=labelsize)
for axis in ['top','bottom','left','right']:
        ax.spines[axis].set_linewidth(bwith)
ax.grid()
ax.set_ylim(0,1)
#ax2.set_xlim(0.8,1)
#ax.set_xlim(0.2,0.3)