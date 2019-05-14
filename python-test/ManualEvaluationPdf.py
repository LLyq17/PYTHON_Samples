#!/usr/bin/env python
# -*- coding: utf-8 -*-

from goofit import *
import matplotlib.pyplot as plt
import numpy as np
import goofit as gf
import sys
#import matplotlib
#matplotlib.use('Agg')



fig,ax = plt.subplots(figsize=(6,4))


_mDs       = 1.96828
_mDs2      = _mDs * _mDs
_mDs2inv   = 1. / _mDs2
piPlusMass = 0.13957018
piZeroMass = 0.1349766

m12 = Observable("m12", 0, 3.5)
m13 = Observable("m13", 0, 3.5)
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
    dtop0pp.motherMass   = _mDs
    dtop0pp.daug1Mass    = piPlusMass
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



def f(r1,i1,m1,w1,r2,i2,m2,w2):
    ar1.value=r1
    ai1.value=i1
    ar2.value=r2
    ai2.value=i2
    mass1.value=m1
    width1.value=w1
    mass2.value=m2
    width2.value=w2

    signal =makeSignalPdf(m12,m13,eventNumber)
    prodpdf=ProdPdf("prodpdf",[signal])
    dplt=gf.DalitzPlotter(prodpdf,signal)

    arr=dplt.make2D()
    extent = dplt.getExtent()
    arr=np.ma.array(arr,mask=arr==0)
    ax.clear()
    plt.imshow(arr,extent=extent,origin='lower')
    plt.colorbar(cax=None,ax=None,shrink=0.5)

    plt.savefig('RBW_pdf_plot.png')
    plt.show()

f(1.0,0,1.2755,0.1867,1.0,0,1.2755,0.1867)

#f(r_pi,r_pi,r_mass,r_width,r_mass,r_width)


