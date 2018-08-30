plt.figure(figsize=(10,5))

plt.hist(setosa, label = 'Setosa', rwidth=0.8, bins=10,  alpha=0.8, density=False, histtype='barstacked')
plt.hist(virginica, label = 'Virginica', rwidth=0.8, bins=11, alpha=0.8, density=False, histtype='barstacked')

plt.legend(loc="upper right")  # Colocamos la leyenda
plt.title(u'Longitud del pétalo de diferentes especies de iris')  # Colocamos el título del gráfico
plt.xlabel('Longitud del pétalo (cm)')  # Colocamos la etiqueta en el eje x
_ = plt.ylabel('Número de especimenes')  # Colocamos la etiqueta en el eje y