cond1 = df['species'] == 'versicolor'
cond2 = df['sepal length (cm)'] >= 5
cond3 = df['petal length (cm)'] >= 1.3
cond4 = df['petal length (cm)'] <= 3.5

df[cond1 & cond2 & cond3 & cond4]