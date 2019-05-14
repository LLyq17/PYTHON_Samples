#!/usr/bin/env python
# -*- coding: utf-8 -*-

from goofit import *
import matplotlib.pyplot as plt
import numpy as np
import goofit as gf
import matplotlib
matplotlib.use('Agg')

from dalitz import makeSignalPdf


fig,ax = plt.subplots()
m12 = Observable("m12", 0, 3.)
m13 = Observable("m13", 0, 3.)
m12.numbins = 240
m13.numbins = 240
eventNumber = EventNumber("eventNumber")
signal =makeSignalPdf(m12,m13,eventNumber)

prodpdf=ProdPdf("prodpdf",[signal])
dplt=gf.DalitzPlotter(prodpdf,signal)

arr=dplt.make2D()
extent = dplt.getExtent()
arr=np.ma.array(arr,mask=arr==0)#background
ax.clear()
plt.imshow(arr,extent=extent,origin='lower')
plt.colorbar(cax=None,ax=None,shrink=0.5)
plt.savefig("dalitz_pdf_eval.png")
plt.show()
