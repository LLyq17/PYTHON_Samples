#!/usr/bin/env python
# -*- coding: utf-8 -*-

from goofit import *
import matplotlib.pyplot as plt
import numpy as np
import goofit as gf
import sys
import cv2
#import matplotlib
#matplotlib.use('Agg')



fig,ax = plt.subplots(figsize=(6,4))


_mD0       = 1.86484
_mD02      = _mD0 * _mD0
_mD02inv   = 1. / _mD02
piPlusMass = 0.13957018
piZeroMass = 0.1349766

m12 = Observable("m12", 0, 3)
m13 = Observable("m13", 0, 3)
m12.numbins = 240
m13.numbins = 240
eventNumber = EventNumber("eventNumber")


mass1 = Variable("m1", 1.08, 0.01, 0.1, 2.7)
width1 = Variable("w1", 0.01, 0.01, 0.0001, 0.2)
mass2 = Variable("m2", 0.8, 0.01, 0.1, 2.7)
width2 = Variable("w2", 0.15, 0.01, 0.0001, 0.2)
ar1=Variable("ar1", 0.565, 0.001, 0, 0)
ai1=Variable("ai1", 0.565, 0.001, 0, 0)
ar2=Variable("ar2", 0.565, 0.001, 0, 0)
ai2=Variable("ai2", 0.565, 0.001, 0, 0)


def makeSignalPdf(m12, m13, eventNumber, eff = None, fitMasses = False):

    constantOne  = Variable("constantOne", 1)
    constantZero = Variable("constantZero", 0)

    dtop0pp = DecayInfo3()
    dtop0pp.motherMass   = _mD0
    dtop0pp.daug1Mass    = piZeroMass
    dtop0pp.daug2Mass    = piPlusMass
    dtop0pp.daug3Mass    = piPlusMass
    dtop0pp.meson_radius = 1.5




    rho1 = Resonances.RBW("rhom",
                        ar1,
                        ai1,
                        mass1,
                        width1,
                        1,
                        PAIR_12)

    rho2 = Resonances.RBW("rho0",
                        ar2,
                        ai2,
                        mass2,
                        width2,
                        1,
                        PAIR_13)

    dtop0pp.resonances = (rho1,rho2)

    if not fitMasses:
        for res in dtop0pp.resonances:
            res.setParameterConstantness(False)

    if not eff:
        # By default create a constant efficiency.
        observables = (m12,m13,)
        offsets = (constantZero,constantZero,)
        coefficients = (constantOne,)
        eff = PolynomialPdf("constantEff", observables, coefficients, offsets, 0)

    d = Amp3Body("signalPDF", m12, m13, eventNumber, dtop0pp, eff)
    return d

#r_pi= np.arange(0.0, 0.5*np.pi, 0.05)
#r_mass=np.arange(0.0, 0.5*np.pi, 0.05)
#r_width=np.arange(0.0, 0.5*np.pi, 0.05)
#r_pi = np.linspace(0, 0.5 * np.pi, 500)
#r_mass=np.linspace(0, 2.7, 500)
#r_width=np.linspace(0, 2.7, 500)

def recall_nothing(x):
    pass


image = np.zeros((200, 300,3), dtype=np.float64)
cv2.namedWindow('Image')

cv2.createTrackbar('a', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('b', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('m1', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('w1', 'Image', 0, 100, recall_nothing)
cv2.createTrackbar('m2', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('w2', 'Image', 0, 100, recall_nothing)

#cv2.imshow('Image', plt)
#cv2.waitKey(0)
#a = cv2.getTrackbarPos('a', 'Image')
#b = cv2.getTrackbarPos('b', 'Image')
#m1 = cv2.getTrackbarPos('m1', 'Image')
#w1 = cv2.getTrackbarPos('w1', 'Image')
#m2 = cv2.getTrackbarPos('m2', 'Image')
#w2 = cv2.getTrackbarPos('w2', 'Image')

#image[:] = [b,b,b]


#def f(a=r_pi,b=r_pi,m1=r_mass,w1=r_width,m2=r_mass,w2=r_width):
#def f(a,b,m1,w1,m2,w2):
def main():    
    a = cv2.getTrackbarPos('a', 'Image')
    b = cv2.getTrackbarPos('b', 'Image')
    m1 = cv2.getTrackbarPos('m1', 'Image')
    w1 = cv2.getTrackbarPos('w1', 'Image')
    m2 = cv2.getTrackbarPos('m2', 'Image')
    w2 = cv2.getTrackbarPos('w2', 'Image')
   # cv2.imshow('Image', image)
   # cv2.waitKey(0)  

    ar1.value=np.cos(a*0.001)
    ai1.value=np.sin(a*0.001)
    ar2.value=np.cos(b*0.001)
    ai2.value=np.sin(b*0.001)
    mass1.value=m1*0.005
    width1.value=w1*0.001
    mass2.value=m2*0.005
    width2.value=w2*0.001

    signal =makeSignalPdf(m12,m13,eventNumber)
    prodpdf=ProdPdf("prodpdf",[signal])
    dplt=gf.DalitzPlotter(prodpdf,signal)

    arr=dplt.make2D()
    extent = dplt.getExtent()
    arr=np.ma.array(arr,mask=arr==0)
#    ax.clear()
   # cv2.imshow('Image', arr)
   # cv2.waitKey(0)
   # plt.imshow(arr,extent=extent,origin='lower')
   # plt.colorbar(cax=None,ax=None,shrink=0.5)
 #   cv2.imshow('Image', arr)
 #   cv2.waitKey(0)
    image[:] = [b,b,b] 
   # plt.savefig('RBW_pdf_plot.png')
    #plt.show()
    cv2.imshow('Image', arr)
    cv2.waitKey(0)   
#f(-0.3*np.pi,-0.3*np.pi,0.8,0.25,0.8,0.2)
#f(a,b,m1,w1,m2,w2)
#f(r_pi,r_pi,r_mass,r_width,r_mass,r_width)
if __name__ == '__main__':
    sys.exit(main())
