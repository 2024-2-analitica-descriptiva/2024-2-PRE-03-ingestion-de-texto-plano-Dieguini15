"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
def pregunta_01():
    with open('clusters_report.txt', 'r') as file:
        lines = file.readlines()

    # Definir encabezados
    headers = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave']

    data = []
    temp_keywords = []
    last_row = None  # Inicializar last_row

    for line in lines:
        # Limpiar línea
        line = line.strip()
        if line == '':
            continue

        # Identificar líneas que inician un nuevo clúster
        if line[0].isdigit():
            # Si last_row tiene datos previos, agregarlo a la lista
            if last_row is not None:
                last_row[-1] = ' '.join(temp_keywords).replace('  ', ' ').strip()
                data.append(last_row)

            # Inicializar datos del nuevo clúster
            parts = line.split()
            cluster = int(parts[0])
            num_keywords = int(parts[1])
            percentage = float(parts[2].replace(',', '.').replace('%', ''))
            temp_keywords = [' '.join(parts[3:])]  # Inicializar palabras clave
            last_row = [cluster, num_keywords, percentage, '']
        else:
            # Continuar acumulando palabras clave para el clúster actual
            temp_keywords.append(line)

    # Agregar la última fila si hay datos pendientes
    if last_row is not None:
        last_row[-1] = ' '.join(temp_keywords).replace('  ', ' ').strip()
        data.append(last_row)

    # Crear DataFrame
    df = pd.DataFrame(data, columns=headers)

    # Formatear el campo de palabras clave
    df['principales_palabras_clave'] = (
        df['principales_palabras_clave']
        .str.replace(' ,', ',', regex=False)  # Eliminar espacios antes de comas
        .str.replace(',+', ',', regex=True)  # Corregir múltiples comas seguidas
        .str.replace('  +', ' ', regex=True)  # Eliminar espacios adicionales entre palabras
        .str.strip()  # Remover espacios al inicio y final
        .str.lstrip('%')  # Eliminar el carácter '%' al inicio
        .str.rstrip('.')  # Eliminar punto final, si existe
    )

    return df
print(pregunta_01())  
      
        
"""
Construya y retorne un dataframe de Pandas a partir del archivo
'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

- El dataframe tiene la misma estructura que el archivo original.
- Los nombres de las columnas deben ser en minusculas, reemplazando los
  espacios por guiones bajos.
- Las palabras clave deben estar separadas por coma y con un solo
  espacio entre palabra y palabra.


"""
