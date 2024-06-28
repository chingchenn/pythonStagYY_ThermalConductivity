#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 12:22:51 2024

@author: chingchen
"""

import stagpy
import numpy as np
from PIL import Image
from stagpy import field
import moviepy.editor as mp
from stagpy import stagyydata
import matplotlib.pyplot as plt

model = 'kvar_a0209'
# model = 'h13'
path = '/Users/chingchen/Desktop/data/'
# path = '/lfs/jiching/ScalingLaw_model/23summer/'
#path = '/lfs/jiching/thermo_chemical/'
path = '/lfs/jiching/thermal_conductivity/'
path = '/Volumes/Sam500/StagYYmodel/'
# path = '/Users/chingchen/Desktop/model/'
figpath = '/Users/chingchen/Desktop/figure/StagYY/'


gif = 1
mp4 = 1
end = 2000
if gif: 
    frames = []
    for shot in  range(1,end,5):
        img=figpath+model+'_'+'temperature_snapshot_'+str(shot)+'_field.png'
        new_frame = Image.open(img)
        frames.append(new_frame)
    frames[0].save(figpath+model+'_'+'temperature_png2gif.gif', format='GIF', append_images=frames[1:], 
                    save_all=True, duration=40, loop=0)
    frames = []
    for shot in  range(1,end,5):
        img=figpath+model+'_'+'basalt_snapshot_'+str(shot)+'_field.png'
        new_frame = Image.open(img)
        frames.append(new_frame)
    frames[0].save(figpath+model+'_'+'basalt_png2gif.gif', format='GIF', append_images=frames[1:], 
                  save_all=True, duration=40, loop=0)
    frames = []
    for shot in  range(1,end,5):
        img=figpath+model+'_'+'primordial_snapshot_'+str(shot)+'_field.png'
        new_frame = Image.open(img)
        frames.append(new_frame)
    frames[0].save(figpath+model+'_'+'primordial_png2gif.gif', format='GIF', append_images=frames[1:], 
                    save_all=True, duration=40, loop=0)
#-----------------------------creat mp4-----------------------------------------    
if mp4:
    clip = mp.VideoFileClip(figpath+model+'_'+'temperature_png2gif.gif')
    clip.write_videofile(figpath+'temperature_field_'+model+".mp4")
    clip = mp.VideoFileClip(figpath+model+'_'+'basalt_png2gif.gif')
    clip.write_videofile(figpath+'basalt_field_'+model+".mp4")
    clip = mp.VideoFileClip(figpath+model+'_'+'primordial_png2gif.gif')
    clip.write_videofile(figpath+'primordial_field_'+model+".mp4")