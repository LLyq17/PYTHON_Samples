#!/usr/bin/env python
# -*- coding: utf-8 -*-


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets

from matplotlib import pyplot as plt 
from goofit import *
import matplotlib.pyplot as plt
import numpy as np
import goofit as gf
import sys
import matplotlib
matplotlib.use('Agg')

#from matplotlib import axes
#from dalitz import makeSignalPdf, runToyFit

fig,ax = plt.subplots(figsize=(6,4))
#v = ax.imshow(arr, extent=ext,origin='lower')


r_pi= np.arange(0.0, 3.0, 0.05)
r_mass=np.arange(0.0, 3.0, 0.05)
r_width=np.arange(0.0, 3.0, 0.05)

#@interact(r_pi=3.0,r_mass=3.0,r_width=0.5)
def f(a=r_pi,b=r_pi,m1=r_mass,w1=r_width,m2=r_mass,w2=r_width):
    ar1.value,ai1.value= np.cos(a),np.sin(a)
    ar2.value,ai2.value=np.cos(b),np.sin(b)
    mass1.value,width1.value=m1,w1
    mass2.value,width2.value=m2,w2
    dplt=gf.DalitzPlotter(prod,dp)
    arr=dplt.make2D()
    arr=np.ma.array(arr,mask=arr==0)
    ax.clear()
    v=ax.imshow(arr,extent=ext,origin='lower')

#    plt.imshow(arr)
#plt.imshow(arr,cmap=plt.get_cmap('hot'),interpolation='nearest')
#    plt.colorbar(mappable=map)
#plt.colorbar(cax=None,ax=None,shrink=0.5) #half of the bar
 #   plt.show()



f(r_pi,r_pi,r_mass,r_width,r_mass,r_width)
'''
m12 = Observable("m12", 0, 3)
m13 = Observable("m13", 0, 3)
m12.numbins = 240
m13.numbins = 240
eventNumber = EventNumber("eventNumber")
signal =makeSignalPdf(m12,m13,eventNumber)

prodpdf=ProdPdf("prodpdf",[signal])
dplt=gf.DalitzPlotter(prodpdf,signal)

arr=dplt.make2D()
arr=np.ma.array(arr,mask=arr==0)
ax.clear()
ax.imshow(arr,origin='lower')


'''
