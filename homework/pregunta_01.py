"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import re

def depurar(line):
    
    cadena_1=r"^(\d+)\s+(\d+)\s+(\d+)([,.])(\d+)([ ,.%]+)(.+)"
    cadena_2 = r"\s{2,5}"
    d = re.search(cadena_1, line)
    line = d.group(1) + ';' + d.group(2) + ';' + d.group(3) + '.' + d.group(5) + ';' + d.group(7)
    line = re.sub(cadena_2, ' ', line)
    
    return line

def pregunta_01():
    with open('clusters_report.txt', 'r') as file:
      dataset = file.readlines()
    cabecera = dataset[:2]
    data = dataset[4:]
    data = [line.replace('\n', "") for line in data]
    data = [line.strip() for line in data]  
    list_1 = []
    i = 0
    line = ""
    while i< len(data):
        if data[i] != "":
            line = line +' '+ data[i]
        else:
            list_1.append(line)
            line = ""
        i += 1
    data = [line.strip() for line in list_1]    
    data = list(map(depurar, data))
    data = [text.split(';') for text in data]
    data = [[int(i[0]), int(i[1]), float(i[2]), i[3].replace('.', '')] for i in data]
    cabecera = [line.replace('\n', "") for line in cabecera]
    cabecera = [line.lower() for line in cabecera]
    cabecera = [line.strip() for line in cabecera]  
    patron = r"\s{2,5}"
    cabecera = [re.sub(patron, ';', line) for line in cabecera]
    cabecera = '; '.join(cabecera)
    cabecera = cabecera.split(';') 
    cabecera = [cabecera[0], cabecera[1] + cabecera[4], cabecera[2] +" "+ cabecera[5], cabecera[3]]
    cabecera = [line.replace(' ', '_') for line in cabecera]
    df = pd.DataFrame(data, columns = cabecera)
    return df

      
        
"""
Construya y retorne un dataframe de Pandas a partir del archivo
'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

- El dataframe tiene la misma estructura que el archivo original.
- Los nombres de las columnas deben ser en minusculas, reemplazando los
  espacios por guiones bajos.
- Las palabras clave deben estar separadas por coma y con un solo
  espacio entre palabra y palabra.


"""
