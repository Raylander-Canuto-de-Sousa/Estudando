

import pandas as pd 
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/Aluno/Desktop/athlete_events.csv')
masculinos = dados.loc[dados['Sex']=='M']
masculinos.head()
a = masculinos['Height']
p = masculinos['Weight']
plt.scatter(a,p)
plt.show()


