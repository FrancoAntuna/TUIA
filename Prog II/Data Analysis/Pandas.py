import matplotlib.pyplot as plt
import os
import csv
import pandas as pd

"""
lista_precios = []
precio_por_barrio = {}

here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here,'listings.csv')
with open(filename, encoding='utf-8') as File:
    next(File)
    reader = csv.reader(File, delimiter=',')
    for fila in reader:
        precio = float(fila[9].replace('$', '').replace(',',''))
        lista_precios.append(precio)
        #por barrio
        barrio = fila[5] # neighbourhood
        if barrio in precio_por_barrio:
            precio_por_barrio[barrio].append(precio)
        else:
            precio_por_barrio[barrio] = [precio]

plt.hist(lista_precios)

"""
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here,'listings.csv')
data = pd.read_csv(filename)

print(data.head(2))
