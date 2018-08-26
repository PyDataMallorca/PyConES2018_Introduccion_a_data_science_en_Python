cond1 = df['species'] == 'setosa'
cond2 = df['sepal length (cm)'] > 5.5
cond3 = df['petal length (cm)'] < 1.3

df[cond1 & (cond2 | cond3)]