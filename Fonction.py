#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 00:17:44 2021

@author: sirwolf
"""

from math import sqrt, degrees, atan, pi
import numpy as np
import matplotlib as plt
from mpl_toolkits import mplot3d


# =============================================================================
#Afficher les solutions de ax² + bx + c = 0 dans un plan (x: partie reel, y: partie imaginaire)


def calculSecondDegres(x, a, b, c): #Tu pourrais faire et une classe Fonction héritant de la <class 'function'>
#une classe Fonction2ndDeg héritant de Fonction
    return a*(x*x) + b*x + c

assert calculSecondDegres(10, 1, 2, 4) == 124

# ...

# =============================================================================
