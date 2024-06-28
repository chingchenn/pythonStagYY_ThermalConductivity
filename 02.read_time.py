#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:20:46 2024

@author: chingchen
"""

import pandas as pd
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
# plt.rcParams["font.family"] = "Times New Roman"


figpath = '/Users/chingchen/Desktop/figure/StagYY/'
mp4 = 1
labelsize   = 25
bwith       = 3
fig_Nu_t    = 1
fig_F_t     = 0
fig_T       = 0
fig_mobility=0
fig_cmbtemp=0
fig_erupt_heatflux=0
newcolors = ['#2F4F4F','#4682B4','#CD5C5C','#708090',
              '#AE6378','#282130','#7E9680','#24788F',
              '#849DAB','#EA5E51','#35838D','#4198B9',
              '#414F67','#97795D','#6B0D47','#A80359','#52254F']
header_list = ['istep','time','F_top','F_bot','Tmin',
               'Tmean','Tmax','Vmin','Vrms','Vmax','eta_min',
               'eta_mean','eta_max','ra_eff','Nu_top','Nu_bot',
               'C_min','C_mean','C_max','F_mean','F_max',
               'erupt_rate','erupta','erupt_heatflux',
               'entrainment','Cmass_error','H_int',
               'r_innercore','Tsurf','Tcmb']

path = '/Users/chingchen/Desktop/data/'

model = 'kvar_a0217'
f = 0.55
file = path+model+'_time.dat'
ff = pd.read_csv(file,sep = '\\s+')    
# for kk, model in enumerate(model_list):
if fig_Nu_t:
    fig,(ax) = plt.subplots(1,1,figsize=(12,10))
    kk = 1
    ax.plot(ff.time, ff.Nu_bot,color = newcolors[kk+1],lw=3,label = 'Nu_bot')   
    ax.plot(ff.time, ff.Nu_top,color = newcolors[kk],lw=3,label = 'Nu_top')
        
    ax.tick_params(labelsize=labelsize)
    for axis in ['top','bottom','left','right']:
                ax.spines[axis].set_linewidth(bwith)
    ax.grid()
    # ax.set_xlim(xmin_Nu,xmax_Nu)
    ax.set_ylim(0, 60)
    # ax.set_xlabel('time',fontsize = labelsize)
    ax.set_ylabel('heat flux',fontsize = labelsize)
    ax.legend(fontsize = 20)
    ax.set_title(model,fontsize = labelsize)
if fig_mobility:
    fig4,(ax4) = plt.subplots(1,1,figsize=(12,6))
    kk = 1
       
    ax4.plot(ff.time, ff.Tmean,color = newcolors[kk],lw=5,label = 'Tmean')
    # ax3.plot(ff.time, ff.Tmean,color = newcolors[kk+1],lw=3,label = 'F_bot')
    
    ax4.tick_params(labelsize=labelsize)
    for axis in ['top','bottom','left','right']:
        ax4.spines[axis].set_linewidth(bwith)
    ax4.grid()
    # ax.set_xlim(0.09,0.12)
    # ax.set_ylim(7,8.2)
    ax4.set_xlabel('time',fontsize = labelsize)
    ax4.set_ylabel('Temperature',fontsize = labelsize)
    ax4.legend(fontsize = 20)
    # ax.set_title('t = '+str(i),fontsize = labelsize)
if fig_cmbtemp:
    fig5,(ax5) = plt.subplots(1,1,figsize=(12,6))
    kk = 1
       
    ax5.plot(ff.time, ff.Tcmb*2500,color = newcolors[kk],lw=2,label = 'erupt_heatflux')
    # ax3.plot(ff.time, ff.Tmean,color = newcolors[kk+1],lw=3,label = 'F_bot')
    
    ax5.tick_params(labelsize=labelsize)
    for axis in ['top','bottom','left','right']:
        ax5.spines[axis].set_linewidth(bwith)
    ax5.grid()
    # ax.set_xlim(0.09,0.12)
    # ax5.set_ylim(0,100)
    ax5.set_xlabel('time',fontsize = labelsize)
    ax5.set_ylabel('Temperature',fontsize = labelsize)
    ax5.legend(fontsize = 20)
    # ax.set_title('t = '+str(i),fontsize = labelsize)
if fig_erupt_heatflux:
    fig5,(ax5) = plt.subplots(1,1,figsize=(12,6))
    kk = 1
       
    ax5.plot(ff.time, ff.erupt_heatflux,color = newcolors[kk],lw=2,label = 'erupt_heatflux')
    # ax3.plot(ff.time, ff.Tmean,color = newcolors[kk+1],lw=3,label = 'F_bot')
    
    ax5.tick_params(labelsize=labelsize)
    for axis in ['top','bottom','left','right']:
        ax5.spines[axis].set_linewidth(bwith)
    ax5.grid()
    # ax.set_xlim(0.09,0.12)
    ax5.set_ylim(0,100)
    ax5.set_xlabel('time',fontsize = labelsize)
    ax5.set_ylabel('Temperature',fontsize = labelsize)
    ax5.legend(fontsize = 20)
    # ax.set_title('t = '+str(i),fontsize = labelsize)