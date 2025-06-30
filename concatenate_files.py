# get file names from folder

import os

# Ruta de la carpeta (usa '.' para la carpeta actual)
carpeta = 'ruta/a/tu/carpeta'  # ejemplo: 'C:/Users/Documents/CSV'

# Obtener todos los nombres de archivos en esa carpeta
archivos = os.listdir(carpeta)

# Filtrar solo los archivos (excluye subcarpetas si las hubiera)
archivos = [f for f in archivos if os.path.isfile(os.path.join(carpeta, f))]
#archivos = archivos[1:]

print(archivos)




# concatenate files

import pandas as pd
import os


# Leer y unir todos los archivos
dataframes = [pd.read_csv(os.path.join(carpeta, archivo)) for archivo in archivos]
df_final = pd.concat(dataframes, ignore_index=True)

# Guardar el archivo unido
df_final.to_csv(os.path.join(carpeta, 'archivo_unido2.csv'), index=False)

print("¡Los archivos fueron unidos exitosamente!")





# unir dos archivos

import pandas as pd

# Leer ambos archivos CSV
archivo1 = pd.read_csv('archivo_unido1.csv')
archivo2 = pd.read_csv('archivo_unido2.csv')

# Unir los archivos
archivo_final = pd.concat([archivo1, archivo2], ignore_index=True)

# Guardar en un nuevo archivo CSV
archivo_final.to_csv('archivo_COMPLETO.csv', index=False)

print("Los archivos fueron unidos exitosamente.")

