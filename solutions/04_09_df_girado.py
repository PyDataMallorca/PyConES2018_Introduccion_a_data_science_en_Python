df_girado = pd.DataFrame() # Creamos un DataFrame vacío

for row in df.index:
    df_girado[row] = df.loc[row, :] 

df_girado