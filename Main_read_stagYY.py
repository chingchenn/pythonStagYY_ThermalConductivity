#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 11:53:34 2024

@author: chingchen
"""

import pandas as pd
import numpy as np


model = 'kvar_a0310'
path = '/Users/chingchen/Desktop/data/'+model+'/'
figpath = '/Users/chingchen/Desktop/figure/StagYY/'+model+'/' 
path = '/Users/chingchen/Desktop/data/'
figpath = '/Users/chingchen/Desktop/figure/StagYY/'


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

def yz2polar(y,z,f=0.55):
    Angle_to_Rad = y*np.pi/180
    radius = (z+f/(1-f))
    polar_x=radius*np.cos(Angle_to_Rad)
    polar_y=radius*np.sin(Angle_to_Rad)
    return radius,polar_x,polar_y

def read_profile_bs(frame):    
    file = path+model+'_profiles'+'_bs'+convert_frame_number(frame)+'.dat'
    ff = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None)  
    ff = np.array(ff)
    altitude,average,std,rms,min,max=ff.T
    return altitude,average,std,rms,min,max

def read_xyz_bs(frame):    
    header_list = ['bs_x','bs_y','bs_z','bs_comp']
    file = path+model+'_xyz'+'_bs'+convert_frame_number(frame)+'.dat'
    bs_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(bs_xyz)/2048),2048)
    xbs=np.reshape(np.array(bs_xyz.bs_x),newsize)
    ybs=np.reshape(np.array(bs_xyz.bs_y),newsize)
    zbs=np.reshape(np.array(bs_xyz.bs_z),newsize)
    cbs=np.reshape(np.array(bs_xyz.bs_comp),newsize)
    r,polar_x,polar_y = yz2polar(ybs,zbs)
    return xbs,ybs,zbs,cbs,polar_x,polar_y,r

def read_profile_temp(number):
    file = path+model+'_profiles'+'_t'+convert_frame_number(number)+'.dat'
    temp_profile = np.array(pd.read_csv(file,sep = '\\s+',skiprows=1,header=None))
    altitude,average,std,rms,min,max=temp_profile.T
    return altitude,average,std,rms,min,max
    
def read_xyz_temp(number):        
    ## read xyz ##
    header_list = ['temp_x','temp_y','temp_z','temp_comp']
    file = path+model+'_xyz'+'_t'+convert_frame_number(number)+'.dat'
    temp_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(temp_xyz)/2048),2048)
    xtemp=np.reshape(np.array(temp_xyz.temp_x), newsize)
    ytemp=np.reshape(np.array(temp_xyz.temp_y), newsize)
    ztemp=np.reshape(np.array(temp_xyz.temp_z), newsize)
    temp=np.reshape(np.array(temp_xyz.temp_comp), newsize)
    r,polar_x,polar_y = yz2polar(ytemp,ztemp)
    return xtemp,ytemp,ztemp,temp,polar_x,polar_y,r



def read_profile_vp(frame):    
    file = path+model+'_profiles'+'_vp'+convert_frame_number(frame)+'.dat'
    ff = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None)  
    ff = np.array(ff)
    altitude,average,std,rms,min,max=ff.T
    return altitude,average,std,rms,min,max

def read_xyz_vz(frame):    
    header_list = ['vz_x','vz_y','vz_z','vz_comp']
    file = path+model+'_xyz'+'_vz'+convert_frame_number(frame)+'.dat'
    vz_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(vz_xyz)/2048),2048)
    xvp=np.reshape(np.array(vz_xyz.vz_x),newsize)
    yvp=np.reshape(np.array(vz_xyz.vz_y),newsize)
    zvp=np.reshape(np.array(vz_xyz.vz_z),newsize)
    cvp=np.reshape(np.array(vz_xyz.vz_comp),newsize)
    r,polar_x,polar_y = yz2polar(yvp,zvp)
    return xvp,yvp,zvp,cvp,polar_x,polar_y,r


def read_xyz_vh(frame):    
    header_list = ['vh_x','vh_y','vh_z','vh_comp']
    file = path+model+'_xyz'+'_vhnorm'+convert_frame_number(frame)+'.dat'
    vh_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(vh_xyz)/2048),2048)
    xvp=np.reshape(np.array(vh_xyz.vh_x),newsize)
    yvp=np.reshape(np.array(vh_xyz.vh_y),newsize)
    zvp=np.reshape(np.array(vh_xyz.vh_z),newsize)
    cvp=np.reshape(np.array(vh_xyz.vh_comp),newsize)
    r,polar_x,polar_y = yz2polar(yvp,zvp)
    return xvp,yvp,zvp,cvp,polar_x,polar_y,r

def read_xyz_vy(frame):    
    header_list = ['vy_x','vy_y','vy_z','vy_comp']
    file = path+model+'_xyz'+'_vy'+convert_frame_number(frame)+'.dat'
    vy_xyz = pd.read_csv(file,sep = '\\s+',skiprows=1,header=None,names=header_list)  
    newsize=(int(len(vy_xyz)/2048),2048)
    xvp=np.reshape(np.array(vy_xyz.vy_x),newsize)
    yvp=np.reshape(np.array(vy_xyz.vy_y),newsize)
    zvp=np.reshape(np.array(vy_xyz.vy_z),newsize)
    cvp=np.reshape(np.array(vy_xyz.vy_comp),newsize)
    r,polar_x,polar_y = yz2polar(yvp,zvp)
    return xvp,yvp,zvp,cvp,polar_x,polar_y,r