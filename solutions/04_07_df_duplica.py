cond = df['species'] == 'virginica'

df_virginica = df[cond]

df = df.append(df_virginica, ignore_index=True)

df.shape