plt.figure(figsize=(16,7))
# Dibujamos la evolución de f(x), frente a x
plt.plot(x_total,y_total, color = 'black', label = '', linestyle="dashed", marker="")  
plt.plot(set_ix, setosa, label = 'Setosa', linestyle="", marker="o",
         markersize=8, alpha=0.9, color="purple")
plt.plot(versicolor_ix, versicolor, label = 'Versicolor', linestyle="",
         marker="o", markersize=8, alpha=0.9)
plt.plot(virginica_ix, virginica, label = 'Virginica', linestyle="",
         marker="o", markersize=8, alpha=0.9, color="green")
# Destacamos los valores por encima de 0.9 colocándoles un marcador circular azul
plt.plot(x_total[y_total > 6.4], y_total[y_total > 6.4],
         'bo', label = 'Long. sépalo > 0.9cm', markersize=3, color="yellow")  

plt.axhspan(6.4, 8, alpha = 0.1)  # Colocamos una banda de color para los valores f(x) > 0.9
plt.ylim(4,9)  # Limitamos el eje x
plt.legend(loc="upper left")  # Colocamos la leyenda
plt.title(u'Longitud del sépalo de diferentes especies de iris')  # Colocamos el título del gráfico
plt.xlabel('Número de especimen')  # Colocamos la etiqueta en el eje x
plt.ylabel('Longitud del sépalo (cm)')  # Colocamos la etiqueta en el eje y
