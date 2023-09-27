import numpy as np
import core

def f1(x):
    core.f_eval+=1
    return 2*x*x-8*x+4

def g1(x):
    core.g_eval+=1
    return 4*x-8

def f2(x):
    return x*x - 1

def g2(x):
    return 2*x

def f3(x):
    if x>700:
        return 1.0
    elif x<-700:
        return -1.0
    else:
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))

def g3(x):
    if x>700:
        return 0.0
    elif x<-700:
        return 0.0
    else:
        return 4*np.exp(2*x)/(np.exp(2*x)+1)**2;

def f4(x):
    return np.cos(x)+np.sin(x*x)-0.5

def g4(x):
    return 2*x*np.cos(x*x)-np.sin(x)