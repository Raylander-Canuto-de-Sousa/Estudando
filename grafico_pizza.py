# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 20:50:11 2022

@author: Aluno
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35,25,25,15])
mylabels = ["Maca","Bananas","Cerejas","Kiwi"]

plt.pie(y,labels = mylabels)
plt.legend(loc="center right", bbox_to_anchor=(1.25, 0.5))
plt.show()
