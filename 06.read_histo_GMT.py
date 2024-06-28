#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:12:23 2024

@author: chingchen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def convert_frame_number(number):
    if number > 0 and number < 10:
        nn = '0000'+str(number)
    elif number >= 10 and number < 100:
        nn = '000'+str(number)
    elif number >= 100 and number < 1000:
        nn = '00'+str(number)
    elif number >= 1000 and number < 10000:
        nn = '0'+str(number)
    elif number >= 10000 :
        nn = str(number)
    return nn

path = '/Users/chingchen/Desktop/data/'
figpath = '/Users/chingchen/Desktop/figure/StagYY/'
frame=1800
model = 'kvar_a0310'
nztot = 256
scatter_size=0.5
bwith = 3
fontsize=20
fig,(ax,ax2) = plt.subplots(1,2,figsize=(14,11)) 

# --- plot temperature histrogram ---
file = path+model+'_'+convert_frame_number(frame)+'_temperature_histo-GMT.dat'
ff = pd.read_csv(file,sep = '\\s+',header=None)  

cmap = plt.cm.get_cmap('Greens')
data=np.array(ff)
data_temp_array = np.array_split(data, 512)
ax.scatter(ff[0][ff[2]!=0]*2500,(1-ff[1][ff[2]!=0])*2890,c=ff[2][ff[2]!=0],cmap = cmap,vmin=0, vmax=0.1,s=scatter_size)

# 
# fig,(ax2) = plt.subplots(1,figsize=(10,10)) 

file = path+model+'_'+convert_frame_number(frame)+'_temperature-in-plume_histo-GMT.dat'
ff = pd.read_csv(file,sep = '\\s+',header=None)  
cmap = plt.cm.get_cmap('Oranges')
data=np.array(ff)
data_temp_array = np.array_split(data, 512)
ax.scatter(ff[0][ff[2]!=0]*2500,(1-ff[1][ff[2]!=0])*2890,c=ff[2][ff[2]!=0],cmap = cmap,vmin=0, vmax=0.1,s=scatter_size)


file = path+model+'_'+convert_frame_number(frame)+'_temperature-in-slab_histo-GMT.dat'
ff = pd.read_csv(file,sep = '\\s+',header=None)  
cmap = plt.cm.get_cmap('Blues')
data=np.array(ff)
data_temp_array = np.array_split(data, 512)
ax.scatter(ff[0][ff[2]!=0]*2500,(1-ff[1][ff[2]!=0])*2890,c=ff[2][ff[2]!=0],cmap = cmap,vmin=0, vmax=0.1,s=scatter_size)


# --- plot Z velocity histrogram ---
file = path+model+'_'+convert_frame_number(frame)+'_Z-velocity_histo-GMT.dat'
ff = pd.read_csv(file,sep = '\\s+',header=None)  

cmap = plt.cm.get_cmap('Greens')
data=np.array(ff)
data_temp_array = np.array_split(data, 512)
ax2.scatter(ff[0][ff[2]!=0]*6.814*10**-4,(1-ff[1][ff[2]!=0])*2890,c=ff[2][ff[2]!=0],cmap = cmap,vmin=0, vmax=0.1,s=scatter_size)
# 

file = path+model+'_'+convert_frame_number(frame)+'_Z-velocity-in-plume_histo-GMT.dat'
ff = pd.read_csv(file,sep = '\\s+',header=None)  
cmap = plt.cm.get_cmap('Oranges')
data=np.array(ff)
data_temp_array = np.array_split(data, 512)
ax2.scatter(ff[0][ff[2]!=0]*6.814*10**-4,(1-ff[1][ff[2]!=0])*2890,c=ff[2][ff[2]!=0],cmap = cmap,vmin=0, vmax=0.1,s=scatter_size)

file = path+model+'_'+convert_frame_number(frame)+'_Z-velocity-in-slab_histo-GMT.dat'
ff = pd.read_csv(file,sep = '\\s+',header=None)  
cmap = plt.cm.get_cmap('Blues')
data=np.array(ff)
data_temp_array = np.array_split(data, 512)
ax2.scatter(ff[0][ff[2]!=0]*6.814*10**-4,(1-ff[1][ff[2]!=0])*2890,c=ff[2][ff[2]!=0],cmap = cmap,vmin=0, vmax=0.1,s=scatter_size)

### ---------------------------- figure setting --------------------------------
ax.set_xlim(0,3800)
ax2.set_xlim(-2,2)
xmajor_ticks = np.linspace(0,3800,num=5)
ax.set_xticks(xmajor_ticks)
ax.set_xlabel('Temperature (K)',fontsize=20)
ax2.set_xlabel('Vertical Velocity (cm/yr)',fontsize=20)
ax.set_ylabel('Depth (km)',fontsize=20)
for aa in [ax,ax2]:
    aa.grid()
    aa.set_ylim(2900,0)
    aa.tick_params(labelsize=fontsize)
    ymajor_ticks=[0,410,660,1000,1500,2000,2500,2890]
    aa.set_yticks(ymajor_ticks)
    for axis in ['top','bottom','left','right']:
        aa.spines[axis].set_linewidth(bwith)
fig.savefig(figpath+model+'_'+convert_frame_number(frame)+'_histogram_T&Vz.png')