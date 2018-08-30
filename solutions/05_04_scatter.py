plt.figure(figsize=(14, 6))
plt.scatter(pl_all, sl_all, c=species, s=pw_all * 75, alpha=0.7)
plt.grid()
plt.title(u'Longitud del pétalo vs. longitud del sépalo')  # Colocamos el título del gráfico
plt.xlabel('Longitud del pétalo (cm)')  # Colocamos la etiqueta en el eje x
plt.ylabel('Longitud del sépalo (cm)')  # Colocamos la etiqueta en el eje y