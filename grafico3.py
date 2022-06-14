# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:39:22 2022

@author: Aluno
"""


import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2])
y= np.array([99,86,87,88,111])
colors = np.array([0,10,20,30,40])
plt.scatter(x,y,c=colors,
            cmap="viridis")

plt.colorbar()
            
            
plt.show()