import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'Nom': ['Alice', 'Bob', 'Charlie', 'David' ,'Eva'], 'Age': [25, 30, 35, 28, 22]}

tab = pd.DataFrame(data)

print(tab)

moyenne_age = np.mean(tab['Age'])

print(moyenne_age)

plt.bar(tab['Nom'], tab['Age'])
plt.xlabel('Nom')
plt.xlabel('Age')
plt.title('age des personnes')
plt.show()
