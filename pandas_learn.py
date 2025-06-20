import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students_data.csv')
print(df.to_string())


df = df[df['Age'] >= 18]
print(df.duplicated())
df.plot()
plt.show()
plt.savefig("my_plot.png")