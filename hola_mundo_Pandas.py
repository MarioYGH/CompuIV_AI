# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lkUt4zNtRxdVsbIqijbbvc-lVbsKj5ka
"""

import pandas as pd

df = pd.read_csv('/content/sample_data/california_housing_test.csv')
df.head(100) #Los primeros 5 registros que vienen por defecto, se puede poner un numero dentro para ver mas
df.tail(0) #los ultimos registros del data

from google.colab import drive
drive.mount('/content/drive')

print(df.total_rooms)
print(df['total rooms']) #una forma alternativa de ver los datos, si el nombre de una variable tiene punto es util
print(df.total_rooms.mean()) #contenido
print(df.total_rooms.max()) #max
print(df.total_rooms.min()) #min
print(df.total_rooms.std()) #desviacion estandar

df.dtypes #tipos de variables de las columnas
df.columns #listar nombre de colunnas
df.axes #Listar las etiquetas de la fila y nombres de columnas, ejes
df.ndim #numero de dimensiones
df.size #El total de datos
df.shape #dimensiones del dataframe
df.values #Return a Numpy representation of the DataFrame.
#esto ultimo se puede asignar a un arreglo arr = df.values

df.describe() #Metodo de objeto, describe todas las metricas, estadisticas descriptivas del frame

print(df.sample(10)) #devuelve una muetra aleatoria del marco de datos

df_claen = df.dropna() #Elimina todos los ejercicios vacios

df_age = df.groupby('housing_median_age')
df_age.mean()

df.head()
df_500k = df[df['median_house_value']>500000] #Regresa el valor del objeto con la condicion
df_500k.head(100)

#ordenar sort.values, se puede ordenar por dos columnas y su propia condicion ascending
df_sorted = df.sort_values(by='median_house_value',ascending=False).head()
df_sorted

#isnull() #retorna con datos nulos
