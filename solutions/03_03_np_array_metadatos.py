a = np.random.randn(10, 2)

print("forma: ", a.shape)
print("# dimensiones: ", a.ndim)
print("# elementos: ", a.size)
print("El número de elementos es igual a multiplicar "
      "todos los elementos de la forma (Shape): ",
      np.multiply(*a.shape) == a.size)
print("Tamaño de cada elemento en bytes: ", a.itemsize)
print("# bytes en el array: ", a.nbytes)
print("El número de bytes del array es igual al número de "
      "elementos por el tamaño de cada elemento: ",
      a.itemsize * a.size == a.nbytes)
print("FLAGS: ", a.flags, sep="\n")