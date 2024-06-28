#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 12:07:13 2024

@author: chingchen
"""
import pandas as pd
import numpy as np
from PIL import Image
import moviepy.editor as mp
import Main_read_stagYY as ms
import matplotlib.pyplot as plt


figpath = '/Users/chingchen/Desktop/figure/StagYY/'
frame=2000
model = 'kvar_a0310'
nztot = 256
xtemp,ytemp,ztemp,temp,polar_x,polar_y,r=ms.read_xyz_bs(frame)
fig,(ax) = plt.subplots(1,figsize=(13,13)) 
ax.set_aspect('equal')
cmap = plt.cm.get_cmap('RdBu_r')
colorbar = ax.pcolormesh(polar_x,polar_y,temp,cmap = cmap, vmin = 0,vmax = 1)
ax.set_title('basalt field at '+str(frame)+' frame',fontsize=26)
fig.gca()
cax = plt.axes([0.93, 0.14, 0.03, 0.7])
cbar = plt.colorbar(colorbar, cax=cax)
fig.savefig(figpath+'basalt field at '+str(frame)+' frame.png')




xtemp,ytemp,ztemp,temp,polar_x,polar_y,r=ms.read_xyz_temp(frame)
fig2,(ax2) = plt.subplots(1,figsize=(13,13)) 
ax2.set_aspect('equal')
cmap = plt.cm.get_cmap('RdBu_r')
colorbar = ax2.pcolormesh(polar_x,polar_y,temp,cmap = cmap, vmin = 0,vmax = 1)
ax2.set_title('temperature field at '+str(frame)+' frame',fontsize=26)
fig.gca()
cax = plt.axes([0.93, 0.14, 0.03, 0.7])
cbar = plt.colorbar(colorbar, cax=cax)
fig2.savefig(figpath+'temperature field at '+str(frame)+' frame.png')

for frame in range(100,2002,100):
    xtemp,ytemp,ztemp,temp,polar_x,polar_y,r=ms.read_xyz_temp(frame)
    fig3,(ax3) = plt.subplots(1,figsize=(13,13)) 
    # ax.axis('off')
    fig3.gca()
    Tanomaly = np.ones(ytemp.shape)
    Tdepth,Tavg,Tstd,Trms,Tmin,Tmax=ms.read_profile_temp(frame)
    for nn in range(len(temp.T)):
        Tanomaly[:,nn] = temp[:,nn]-Tavg
    # Tavge_matrix = np.ones(ytemp.shape)
    

    ax3.set_aspect('equal')
    cmap = plt.cm.get_cmap('RdBu_r')
    colorbar = ax3.pcolormesh(polar_x,polar_y,Tanomaly,cmap = cmap, vmin = -0.25,vmax = 0.25)
    ax3.axis('off')
    fig3.gca()
    
    
#     Tplume = Tavg+0.5*(Tmax-Tavg)
#     Tslab = Tavg+0.5*(Tmin-Tavg)
#     tplume_field = temp-np.reshape(Tplume,(nztot,1))*np.ones(ytemp.shape)
#     tslab_field = (temp-np.reshape(Tslab,(nztot,1))*np.ones(ytemp.shape))
#     plume = (tplume_field>=0)
#     slab = (tslab_field<=0)
#     # ax.scatter(polar_x[plume], polar_y[plume], c='red',s=5)
#     # ax.scatter(polar_x[slab], polar_y[slab], c='darkblue',s=5)
    
#     ax.contour(polar_x,polar_y,tplume_field,levels=[0],colors='black')
#     ax.contour(polar_x,polar_y,tslab_field,levels=[0],colors='green')
#     ax.set_title('Time (frame): '+str(frame),fontsize=20)
#     cax = plt.axes([0.93, 0.285, 0.03, 0.431])
#     cbar = plt.colorbar(colorbar, cax=cax)
#     cbar.set_label(label = 'Temperature',size=12)
#     fig.savefig(figpath+model+'_Tanomaly_'+str(frame)+'.png' )
# frames = []
# for frame in range(100,2002,5):
#     img=figpath+model+'_Tanomaly_'+str(frame)+'.png'
#     new_frame = Image.open(img)
#     frames.append(new_frame)
# frames[0].save(figpath+model+'_Tanomaly_'+str(frame)+'_png2gif.gif', format='GIF', append_images=frames[1:], 
#                 save_all=True, duration=40, loop=0)
# clip = mp.VideoFileClip(figpath+model+'_Tanomaly_'+str(frame)+'_png2gif.gif')
# clip.write_videofile(figpath+'temperature_field_'+model+".mp4")
