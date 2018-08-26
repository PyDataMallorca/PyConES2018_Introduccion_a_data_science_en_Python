cond = df['species'] == 'virginica'

df_virginica = df[cond]

print(df_virginica['sepal width (cm)'].mean(), df_virginica['sepal width (cm)'].std())