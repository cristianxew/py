import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Datos de ejemplo
# x = np.linspace(0, 10, 100)  # 100 puntos entre 0 y 10
# y = np.sin(x)

# # Crear gráfico
# plt.plot(x, y, label="Seno de x")
# plt.xlabel("X")
# plt.ylabel("Y")
# plt.title("Gráfico de una función seno")
# plt.legend()
# plt.show()
# Datos aleatorios
data = np.random.randn(1000)

# Crear histograma
# plt.hist(data, bins=30, color="blue", alpha=0.7)
# plt.xlabel("Valor")
# plt.ylabel("Frecuencia")
# plt.title("Histograma de datos aleatorios")
# plt.show()

# Crear un DataFrame con datos ficticios
# data = {
#     "Edad": np.random.randint(20, 60, 100),
#     "Salario": np.random.randint(2000, 10000, 100)
# }

# df = pd.DataFrame(data)

# # Gráfico de dispersión
# sns.scatterplot(x="Edad", y="Salario", data=df)
# plt.title("Relación entre Edad y Salario")
# plt.show()

# Datos de ejemplo
# categorias = ["A", "B", "C", "D"]
# valores = [10, 20, 15, 25]

# # # Crear DataFrame
# df = pd.DataFrame({"Categoría": categorias, "Valor": valores})

# # # Gráfico de barras
# # sns.barplot(x="Categoría", y="Valor", data=df)
# # plt.title("Gráfico de Barras")
# # plt.show()

# # Matriz de correlación
# sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
# plt.title("Matriz de Correlación")
# plt.show()

# Ejercicio Práctico

# Crea un DataFrame con 100 registros con columnas: Edad, Salario, HorasTrabajo
data = {
    "Edad": np.random.randint(20, 60, 100),
    "Salario": np.random.randint(2000, 10000, 100),
    "HorasTrabajo": np.random.randint(20, 40, 100)
}
# Haz un histograma de las edades
df = pd.DataFrame(data)
plt.hist(df["Edad"], bins=30, color="green", alpha=0.7)
plt.xlabel("Edad")
plt.ylabel("Frecuencia")
plt.title("Histograma de Edades")
plt.show()
# Crea un gráfico de dispersión entre Salario y HorasTrabajo
sns.scatterplot(x="Salario", y="HorasTrabajo", data=df)
plt.title("Relación entre Salario y Horas de Trabajo")
plt.show()
# Genera un gráfico de barras con la cantidad de personas por rango de edad
bins = [20, 30, 40, 50, 60]
df["RangoEdad"] = pd.cut(df["Edad"], bins=bins)
sns.countplot(x="RangoEdad", data=df)
plt.title("Cantidad de Personas por Rango de Edad")
plt.show()
# Calcula la matriz de correlación y crea un heatmap
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()
# Guarda el DataFrame en un archivo CSV
