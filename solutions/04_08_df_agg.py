def func(x):
    return sum(x**2)

df.groupby('species').agg(func)