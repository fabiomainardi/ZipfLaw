# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:22:36 2015

@author: fabiomainardi
"""
import random


def ZipfObs(alpha, minval, n):#returns n observations of power law with exp alpha
   assert(minval>0 and minval<1)
   assert(alpha>1)
   obs=[]
   for i in range(n):
       r=random.uniform(0,1)
       x= minval*pow(1-r,1/(1-alpha))
       obs.append(x)
  
   return obs
   
#example
data=ZipfObs(2.5,0.001,100000)

#estimate alpha from data

def EstimateAlpha(data):
    m=sum(data)/len(data)
    minval=min(data)
    alpha=(2*m-minval)/(m-minval)
    return alpha

#example
print(EstimateAlpha(data))

