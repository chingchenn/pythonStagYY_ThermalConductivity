#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:01:34 2024

@author: chingchen
"""

import numpy as np
import matplotlib.pyplot as plt

labelsize=15
bwith=2
ksurf = 3.0
depth = np.linspace(0,1)
fig,(ax) = plt.subplots(1,1,figsize=(4,7))
for kD in [1,2.18,4,10]:
    k_d = 1 + (kD-1)*depth
    k_cond = ksurf*k_d
    ax.plot(k_cond,depth,lw=3,color='navy')
ax.set_ylabel('ice layer thickness (km)',fontsize = labelsize)
ax.minorticks_on()
# ax.tick_params(which='minor', length=5, width=2, direction='in')
ax.tick_params(labelsize=labelsize,width=3,length=10,right=True, top=True,direction='in',pad=15)
ax.set_xlim(0,30)
ax.set_ylim(1,0)
ax.grid()
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(bwith)


# for n in [0,0.5,0.8]:
#     k_T = 