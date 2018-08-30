plt.figure(figsize=(14, 6))
plt.tricontourf(sw_all, pw_all, pl_all)  # Pintamos las triangulaciones con contornos de color
plt.tricontour(sw_all, pw_all, pl_all, colors = 'k')  # Pintamos las líneas de contorno en color negro
plt.scatter(sw_all, pw_all, c="r", alpha=0.5)  # Pintamos la posición de las estaciones de medida.
plt.title(u'Mapa de contorno de longitud del pétalo')  # Colocamos el título del gráfico
plt.xlabel('Anchura del sépalo (cm)')  # Colocamos la etiqueta en el eje x
plt.ylabel('Anchura del pétalo (cm)')  # Colocamos la etiqueta en el eje y