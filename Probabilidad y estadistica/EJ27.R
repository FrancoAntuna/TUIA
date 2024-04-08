install.packages("readxl")
install.packages("janitor")
install.packages("tidyverse")
install.packages("ggplot2")


library(readxl)
library(tidyverse)
library(janitor)
library(ggplot2)

setwd("C:\\Users\\Franco-SIM\\Desktop\\TUIA\\Probabilidad y estadistica")

hojas <- excel_sheets("Datos.xlsx")
datos <- readxl::read_excel("Datos.xlsx", sheet = hojas[7])

plot(datos$`Cantidad de mensajes breves`,
     type = 'l')

frecuencias <- tabyl(datos$`Cantidad de mensajes breves`)
colnames(frecuencias)

ggplot(frecuencias, aes(x = datos, y + n)) +
  geom_segment(aes(x=datos, xend=datos, y=0, yend=n)) +
  geom_point(color='deeppink3',size = 3) +
  theme_dark()
  
