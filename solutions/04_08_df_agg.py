def func(x):
    return np.sum(x**2)

df.groupby('species').agg(func)