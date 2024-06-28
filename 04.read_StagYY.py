#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:21:45 2024

@author: chingchen
"""

import pandas as pd
import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt

labelsize   = 25
bwith       = 3
f=0.55
newcolors = ['#2F4F4F','#4682B4','#CD5C5C','#708090',
              '#AE6378','#282130','#7E9680','#24788F',
              '#849DAB','#EA5E51','#35838D','#4198B9',
              '#414F67','#97795D','#6B0D47','#A80359','#52254F']


#========================== DO WHAT ==============================
temp=0          #- Temperature
bs=0            #- Basalt fraction
c=0             #- Composition
prm=0           #- Primordial composition
hz=0            #- Harzburgite composition
ph=0            #- Phase
ve=0            #- Velocity     
vp=0            #- Velocity & pressure: 
eta=0           #- Viscosity
fra=0           #- Melt fraction
hs=0            #- Volumetric heating
k=1             #- Thermal conductivity
rho=0           #- Density
drho=0          #- Density anomalies
g=0             #- Geoid

# 						  - Composition:                     c
# 						  - Primordial composition:        prm
# 						  - Basalt fraction:                bs
# 						  - Harzburgite composition:        hz
# 						  - Phase:                          ph
# 						  - Velocity                        ve
# 						  - Velocity & pressure:            vp
# 						  - Viscosity:                     eta
# 						  - Melt fraction:                   f

# 						  - Volumetric heating:             hs
# 						  - Thermal conductivity:            k
# 						  - Density:                       rho
# 						  - Density anomalies:            drho
# 						  - Geoid:                           g

#----------------------------------------------------------------------


model = 'kvar_a0310'
path = '/Users/chingchen/Desktop/data/'+model+'/'
figpath = '/Users/chingchen/Desktop/figure/StagYY/'+model+'/'
file = path+model+'_time.dat'
ff = pd.read_csv(file,sep = '\\s+')    
frame=900
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

if bs:
    #####--------------- read bs field ------------
    ## read profile ##
    header_list = ['altitude','average','standard deviation','RMS', 'min', 'max']
    file = path+model+'_profiles'+'_bs'+convert_frame_number(frame)+'.dat'
    ff = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    
    ## read xyz ##
    header_list = ['bs_x','bs_y','bs_z','bs_comp']
    file = path+model+'_xyz'+'_bs'+convert_frame_number(frame)+'.dat'
    bs_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(bs_xyz)/2048),2048)
    kk1,kk2,kk3 = np.reshape(np.array(bs_xyz.bs_y), newsize),np.reshape(np.array(bs_xyz.bs_z), newsize),np.reshape(np.array(bs_xyz.bs_comp), newsize)
    ### ------- convert xyz to polar coordinate ----------
    Angle_to_Rad = kk1*np.pi/180
    r = (kk2+f/(1-f))*2890
    # r=kk2
    x=r*np.cos(Angle_to_Rad)
    y=r*np.sin(Angle_to_Rad)
    fig,(ax) = plt.subplots(1,figsize=(13,13)) 
    ax.set_aspect('equal')
    cmap = plt.cm.get_cmap('RdBu_r')
    colorbar = ax.pcolormesh(x,y,kk3,cmap = cmap, vmin = 0,vmax = 1)
    # ax.axis('off')
    fig.gca()


if temp:
    #####--------------- read t field ------------
    
    ## read profile ##
    header_list = ['Altitude','average','standard deviation','RMS', 'min', 'max']
    file = path+model+'_profiles'+'_t'+convert_frame_number(frame)+'.dat'
    ff = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    
    ## read xyz ##
    header_list = ['temp_x','temp_y','temp_z','temp_comp']
    file = path+model+'_xyz'+'_t'+convert_frame_number(frame)+'.dat'
    temp_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(temp_xyz)/2048),2048)
    kk1,kk2,kk3 = np.reshape(np.array(temp_xyz.temp_y), newsize),np.reshape(np.array(temp_xyz.temp_z), newsize),np.reshape(np.array(temp_xyz.temp_comp), newsize)
    ### ------- convert xyz to polar coordinate ----------
    Angle_to_Rad = kk1*np.pi/180
    r = (kk2+f/(1-f))*2890
    x=r*np.cos(Angle_to_Rad)
    y=r*np.sin(Angle_to_Rad)
    fig,(ax) = plt.subplots(1,figsize=(13,13)) 
    ax.set_aspect('equal')
    cmap = plt.cm.get_cmap('RdBu_r')
    colorbar = ax.pcolormesh(x,y,kk3,cmap = cmap, vmin = 0,vmax = 1)
    # ax.axis('off')
    fig.gca()
if c:
    #####--------------- read t field ------------ 
    ## read profile ##
    header_list = ['Altitude','average','standard deviation','RMS', 'min', 'max']
    file = path+model+'_profiles'+'_c'+convert_frame_number(frame)+'.dat'
    ff = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    
    ## read xyz ##
    header_list = ['c_x','c_y','c_z','c_comp']
    file = path+model+'_xyz'+'_c'+convert_frame_number(frame)+'.dat'
    c_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(c_xyz)/2048),2048)
    kk1,kk2,kk3 = np.reshape(np.array(c_xyz.c_y), newsize),np.reshape(np.array(c_xyz.c_z), newsize),np.reshape(np.array(c_xyz.c_comp), newsize)
    ### ------- convert xyz to polar coordinate ----------
    Angle_to_Rad = kk1*np.pi/180
    r = (kk2+f/(1-f))*2890
    x=r*np.cos(Angle_to_Rad)
    y=r*np.sin(Angle_to_Rad)
    fig,(ax) = plt.subplots(1,figsize=(13,13)) 
    ax.set_aspect('equal')
    cmap = plt.cm.get_cmap('Dark2')
    colorbar = ax.pcolormesh(x,y,kk3,cmap = cmap, vmin = 1,vmax = 8)
    # ax.axis('off')
    fig.gca()
if k:
    #####--------------- read t field ------------
    ## read profile ##
    header_list = ['Altitude','average','standard deviation','RMS', 'min', 'max']
    file = path+model+'_profiles'+'_k'+convert_frame_number(frame)+'.dat'
    ff = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    
    ## read xyz ##
    header_list = ['kcond_x','kcond_y','kcond_z','kcond_comp']
    file = path+model+'_xyz'+'_k'+convert_frame_number(frame)+'.dat'
    kcond_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(kcond_xyz)/2048),2048)
    kk1,kk2,kk3 = np.reshape(np.array(kcond_xyz.kcond_y), newsize),np.reshape(np.array(kcond_xyz.kcond_z), newsize),np.reshape(np.array(kcond_xyz.kcond_comp), newsize)
    ### ------- convert xyz to polar coordinate ----------
    Angle_to_Rad = kk1*np.pi/180
    r = (kk2+f/(1-f))*2890
    x=r*np.cos(Angle_to_Rad)
    y=r*np.sin(Angle_to_Rad)
    fig,(ax) = plt.subplots(1,figsize=(13,13)) 
    ax.set_aspect('equal')
    cmap = plt.cm.get_cmap('Dark2')
    colorbar = ax.pcolormesh(x,y,kk3,cmap = cmap, vmin = 1,vmax = 8)
    # ax.axis('off')
    fig.gca()