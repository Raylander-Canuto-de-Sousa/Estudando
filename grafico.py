# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:39:20 2022

@author: Aluno
"""


import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7,2,17,2,6,4,11])

y= np.array([99,86,87,88,111,86,24,65,54,56])
plt.scatter(x, y,color = 'hotpink')

x= np.array([2,2,8,1,15,8,4,7,8,10])
x= np.array([100,105,84,105,90,12,34,67,24,89])
plt.scatter(x,y,color='#88c999')
            
            
plt.show()