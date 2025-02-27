import numpy as np
import pandas as pd

###################################################################################

# Numpy es una librería de Python que permite trabajar con arrays y matrices de forma eficiente.

# Crea un array de 10 números enteros aleatorios entre 1 y 100.
array = np.random.randint(1, 101, 10)
print('numero aleatorios:', array)

# Convierte ese array en una matriz de 2x5.
matriz = array.reshape(2, 5)
print('matriz:', matriz)

# Calcula la media y la suma total de la matriz.
print('media:', matriz.mean())
print('suma:', matriz.sum())

# Extrae solo la primera fila de la matriz.
print('primera fila:', matriz[0])


###################################################################################

# Pandas es una biblioteca para manejar y analizar datos en estructuras tabulares, como hojas de cálculo o bases de datos. Se basa en NumPy y es clave en la manipulación de datos antes de aplicarlos a modelos de IA.

# 1️⃣ Instalación...

# 2️⃣ Estructuras de Datos en Pandas

# Crear una Serie
# Una Serie es como una lista de Python pero con etiquetas (índices personalizados).
datos = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(datos)

# Acceder a valores por índice
print(datos["b"])  # 20

# Crear un DataFrame manualmente
# Un DataFrame es una tabla bidimensional con filas y columnas, como una hoja de cálculo.
data = {
    "Nombre": ["Ana", "Juan", "Carlos"],
    "Edad": [25, 30, 35],
    "Ciudad": ["Madrid", "Barcelona", "Sevilla"]
}

df = pd.DataFrame(data)
print(df)


# 3️⃣ Cargar Datos desde Archivos CSV
# Normalmente, los datos vienen de archivos externos como CSV o Excel.

# df = pd.read_csv("archivo.csv")  # Cargar CSV
# df.to_csv("nuevo_archivo.csv", index=False)  # Guardar CSV sin índice

# 4️⃣ Exploración de Datos

print(df.head())  # Primeras 5 filas
print(df.tail())  # Últimas 5 filas
print(df.info())  # Información general del DataFrame
print(df.describe())  # Estadísticas básicas


# 5️⃣ Selección y Filtrado de Datos

# Seleccionar una columna
print(df["Nombre"])

# Filtrar filas con una condición
print(df[df["Edad"] > 30])

# Seleccionar múltiples columnas
print(df[["Nombre", "Ciudad"]])

# Seleccionar una fila por índice
print(df.iloc[1])  # Segunda fila

# 6️⃣ Modificación de Datos

df["Edad"] = df["Edad"] + 1  # Modificar valores
df["Salario"] = [2000, 2500, 3000]  # Agregar una nueva columna
df.drop("Ciudad", axis=1, inplace=True)  # Eliminar una columna

# Ejercicio Práctico

# Crea un DataFrame con 5 filas y 3 columnas (Nombre, Edad, Salario)
data = {
    "Nombre": ["Ana", "Juan", "Carlos", "Laura", "Pedro"],
    "Edad": [25, 30, 35, 40, 45],
    "Salario": [2000, 2500, 3000, 3500, 4000]
}

df = pd.DataFrame(data)

# Filtra solo las personas con salario mayor a 3000.
print(df[df["Salario"] > 3000])

# Agrega una columna Ciudad.
df["Ciudad"] = ["Madrid", "Barcelona", "Sevilla", "Valencia", "Bilbao"]

# Guarda el DataFrame en un archivo CSV.
# df.to_csv("empleados.csv", index=False)

###################################################################################

# Operaciones Avanzadas con Pandas 🚀

# 1️⃣ Manejo de Datos Nulos
# A veces, los datos tienen valores nulos (NaN). Pandas ofrece varias formas de manejar esto:
# Crear un DataFrame con valores nulos
data = {
    "Nombre": ["Ana", "Juan", "Carlos", np.nan],
    "Edad": [25, np.nan, 35, 40],
    "Salario": [3000, 2500, np.nan, 4000]
}
df = pd.DataFrame(data)
print(df)
# Verificar valores nulos
print(df.isnull())  # Muestra True donde hay valores nulos
print(df.isnull().sum())  # Cuenta valores nulos por columna
# Eliminar filas con valores nulos
df_limpio = df.dropna()
# Rellenar valores nulos con un número específico
df_filled = df.fillna({"Edad": df["Edad"].mean(), "Salario": 0})



# 2️⃣ Agrupación de Datos (groupby)
data = {
    "Departamento": ["Ventas", "Ventas", "TI", "TI", "RRHH"],
    "Empleado": ["Ana", "Juan", "Carlos", "Pedro", "Marta"],
    "Salario": [3000, 2500, 4000, 3500, 2800]
}
df = pd.DataFrame(data)
# Agrupar por departamento y calcular la media de salarios
salarios_por_depto = df.groupby("Departamento")["Salario"].mean()
print(salarios_por_depto)



# 3️⃣ Ordenar Datos
# Ordenar por salario descendente
df_sorted = df.sort_values(by="Salario", ascending=False)



# 4️⃣ Aplicar Funciones con apply()
# Puedes aplicar funciones personalizadas a cada fila o columna.
# Función para clasificar empleados según el salario
def clasificar(salario):
    return "Alto" if salario > 3000 else "Bajo"

df["Nivel"] = df["Salario"].apply(clasificar)
print(df)



# 5️⃣ Combinación de DataFrames (merge y concat)
# Si tienes datos en diferentes tablas, puedes combinarlos con merge (similar a SQL) o concat.
df1 = pd.DataFrame({"ID": [1, 2, 3], "Nombre": ["Ana", "Juan", "Carlos"]})
df2 = pd.DataFrame({"ID": [1, 2, 3], "Salario": [3000, 2500, 4000]})
# Unir por columna en común (ID)
df_completo = pd.merge(df1, df2, on="ID")
print(df_completo)


# Ejercicio Práctico

# Crea un DataFrame con datos de empleados (nombre, edad, salario, departamento)
data = {
    "Nombre": ["Ana", "Juan", "Carlos", "Laura", "Pedro"],
    "Edad": [25, 30, 35, 40, 45],
    "Salario": [2000, 2500, 3000, 3500, 4000],
    "Departamento": ["Ventas", "Ventas", "TI", "TI", "RRHH"]
}
df = pd.DataFrame(data)

# Filtra los empleados con salario mayor a 3000
df_filtrado = df[df["Salario"] > 3000]

# Agrupa los empleados por departamento y calcula el salario promedio
salario_promedio = df.groupby("Departamento")["Salario"].mean()

# Ordena los empleados por edad de mayor a menor
df_ordenado = df.sort_values(by="Edad", ascending=False)

# Aplica una función que etiquete los salarios como "Bajo", "Medio" o "Alto"
def clasificar(salario):
    if salario < 2500:
        return "Bajo"
    elif salario < 3500:
        return "Medio"
    else:
        return "Alto"

df["Nivel"] = df["Salario"].apply(clasificar)
