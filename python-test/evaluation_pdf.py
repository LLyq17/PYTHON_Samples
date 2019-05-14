#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, division
from matplotlib import pyplot as plt
from goofit import *
import matplotlib.pyplot as plt
import numpy as np
import goofit as gf
import sys
import matplotlib
matplotlib.use('Agg')

from matplotlib import axes

print_goofit_info()

fig,ax = plt.subplots(figsize=(6,4))
fig,ax1 = plt.subplots()


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
width1 = Variable("w1", 0.01, 0.01, 0.0001, 0.1)
mass2 = Variable("m2", 1.08, 0.01, 0.1, 2.7)
width2 = Variable("w2", 0.01, 0.01, 0.0001, 0.1)
ar1=Variable("ar1", 0.565, 0.001, 0, 0)
ai1=Variable("ai1", 0.565, 0.001, 0, 0)
ar2=Variable("ar2", 0.565, 0.001, 0, 0)
ai2=Variable("ai2", 0.565, 0.001, 0, 0)




def makeSignalPdf(m12, m13, eventNumber, eff = None, fitMasses = False):
    # Constants used in more than one PDF component.
    # motherM = Variable("motherM", _mD0)
    # chargeM = Variable("chargeM", piPlusMass)
    # neutrlM = Variable("neutrlM", piZeroMass)
    # massSum = Variable("massSum", _mD0 *_mD0 + 2 * piPlusMass * piPlusMass + piZeroMass * piZeroMass) # = 3.53481

    constantOne  = Variable("constantOne", 1)
    constantZero = Variable("constantZero", 0)

    #mass1 = Variable("m1", 0.7758, 0.01, 0.1, 2.7)
    #width1 = Variable("w1", 0.0015, 0.01, 0.001, 2.7)
    #mass2 = Variable("m2", 0.7758, 0.01, 0.1, 2.7)
    #width2 = Variable("w2", 0.1503, 0.01, 0.1, 2.7)
    #ar1=Variable("ar1", 0.565, 0.001, 0, 0)
    #ai1=Variable("ai1", 0.565, 0.001, 0, 0)
    #ar2=Variable("ar2", 0.565, 0.001, 0, 0)
    #ai2=Variable("ai2", 0.565, 0.001, 0, 0)

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




'''
signal =makeSignalPdf(m12,m13,eventNumber)
prodpdf=ProdPdf("prodpdf",[signal])
dplt=gf.DalitzPlotter(prodpdf,signal)

arr=dplt.make2D()
arr=np.ma.array(arr,mask=arr==0)
ax.clear()
ax.imshow(arr,origin='lower')
plt.show()
'''
#r_pi= np.arange(0.0, 0.5*np.pi, 0.05)
#r_mass=np.arange(0.0, 0.5*np.pi, 0.05)
#r_width=np.arange(0.0, 0.5*np.pi, 0.05)
#r_pi = np.linspace(0, 0.5 * np.pi, 500)
#r_mass=np.linspace(0, 2.7, 500)
#r_width=np.linspace(0, 2.7, 500)
#a=np.linspace(0, 0.5 * np.pi, 500)
#b=np.linspace(0, 0.5 * np.pi, 500)

#r_pi=Variable("r_pi", 0.565, 0.001, 0, 0.5 * np.pi)
#r_mass=Variable("r_mass", 0.565, 0.001, 0, 2.7)
#r_width=Variable("r_width", 0.565, 0.001, 0, 2.7)



def f(a,b,m1,w1,m2,w2):
    signal =makeSignalPdf(m12,m13,eventNumber)
    #prodpdf=ProdPdf("prodpdf",[signal])
    #mass1.value,width1.value=m1,w1
    #mass2.value,width2.value=m2,w2
    ar1.value=np.cos(a)
    ai1.value=np.sin(a)
    ar2.value=np.cos(b)
    ai2.value=np.sin(b)
    mass1.value=m1
    width1.value=w1
    mass2.value=m2
    width2.value=w2
    #ar1.value,ai1.value= np.cos(a),np.sin(a)
    #ar2.value,ai2.value=np.cos(b),np.sin(b)
    #mass1.value,width1.value=m1,w1
    #mass2.value,width2.value=m2,w2
    #ar1.setValue(np.cos(a))
    #ai1.setValue(np.sin(a))
    #ar2.setValue(np.cos(b))
    #ai2.setValue(np.sin(b))
    #mass1.setValue(m1)
    #width1.setValue(w1)
    #mass2.setValue(m2)
    #width2.setValue(w2)
    #ar1._goofit.Indexable(np.cos(a))
    #ai1._goofit.Indexable(np.sin(a))
    #ar2._goofit.Indexable(np.cos(b))
    #ai2._goofit.Indexable(np.sin(b))
    #mass1._goofit.Indexable(m1)
    #width1._goofit.Indexable(w1)
    #mass2._goofit.Indexable(m2)
    #width2._goofit.Indexable(w2)

    #signal =makeSignalPdf(m12,m13,eventNumber)
    prodpdf=ProdPdf("prodpdf",[signal])
    dplt=gf.DalitzPlotter(prodpdf,signal)

    arr=dplt.make2D()
    arr=np.ma.array(arr,mask=arr==0)
    ax.clear()
    ax.imshow(arr,origin='lower')
    ax1.plot(a,'_')
    plt.show()
    

f(0.3,0.3,1.1,0.02,1.1,0.02)

#f(r_pi,r_pi,r_mass,r_width,r_mass,r_width)
#f(a=r_pi,b=r_pi,m1=r_mass,w1=r_width,m2=r_mass,w2=r_width)



