import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titan = pd.read_csv("titanic.csv")
print(titan.head(5))
print(titan.tail(5))
print(titan.sample(5))

print(titan.dtypes)
print(titan.describe())

print(titan.name.value_counts())

print(titan['age'].median())
x = titan['age']
y = titan['fare']
plt.xlabel('age')
plt.ylabel('fare')
plt.scatter(x,y)
plt.show()

x = titan['age']
plt.xlabel('age')
plt.ylabel('frequency')
plt.hist(x)
plt.show()

x = titan['sex']
y = titan['age']
plt.bar(x,y, color='red', width=0.8)
plt.show()