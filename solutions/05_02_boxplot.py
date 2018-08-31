plt.boxplot([setosa, virginica, versicolor], sym = 'ko', whis = 1.5)  # El valor por defecto para los bigotes es 1.5*IQR pero lo escribimos explícitamente
plt.xticks([1,2,3], ['Setosa', 'Virginica', 'Versicolor'], size = 'small', color = 'k')  # Colocamos las etiquetas para cada distribución
plt.ylabel(u'Longitud de sépalo (cm)')
plt.title("Longitudes de pétalo de diferentes especies")