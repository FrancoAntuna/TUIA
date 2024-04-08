datos = read.delim("clipboard", dec = ",")
intervalos = read.delim("clipboard", dec = ",")

hist(datos$Duracion,
     breaks = 8, 
     main = "Histograma de frecuencias",
     col = "blue"
     )
