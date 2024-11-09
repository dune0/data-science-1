import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
1) Consigna

Identificar 3 datasets que cumplan con las siguientes condiciones: a) al menos 2000 filas y b) al menos 15 columnas. Pueden buscar en las siguientes fuentes: Github, Kaggle, Google Dataset Search (también puede ser un archivo propio).
Crear una cuenta de GitHub y hostearlo ahí.
Cargar los archivos correspondientes por medio de la librería Pandas.
Describir las variables potencialmente interesantes en cada archivo teniendo en cuenta el contexto del caso..

"""
# Dataset 1: Diabetes
url_diabetes = "https://raw.githubusercontent.com/dune0/data-science-1/main/diabetes.csv"
diabetes_df = pd.read_csv(url_diabetes)

print("\n--- Dataset: Diabetes ---")
print("\nPrimeras filas del dataset:")
print(diabetes_df.head())

print("\nInformación del dataset:")
print(diabetes_df.info())

print("\nEstadísticas descriptivas:")
print(diabetes_df.describe())

print("\nValores nulos en cada columna:")
print(diabetes_df.isnull().sum())

# Descripción de las variables interesantes
print("\nDescripción de variables interesantes del dataset Diabetes:")
print("- Pregnancies: Número de embarazos.")
print("- Glucose: Nivel de glucosa en sangre.")
print("- BloodPressure: Presión arterial.")
print("- Insulin: Nivel de insulina en sangre.")
print("- BMI: Índice de masa corporal.")
print("- DiabetesPedigreeFunction: Factor de riesgo genético de diabetes.")
print("- Age: Edad de la paciente.")
print("- Outcome: Resultado (0 = no tiene diabetes, 1 = tiene diabetes).")


# Dataset 2: Netflix Titles
url_netflix = "https://raw.githubusercontent.com/dune0/data-science-1/main/netflix_titles.csv"
netflix_df = pd.read_csv(url_netflix)

print("\n--- Dataset: Netflix Titles ---")
print("\nPrimeras filas del dataset:")
print(netflix_df.head())

print("\nInformación del dataset:")
print(netflix_df.info())

print("\nEstadísticas descriptivas:")
print(netflix_df.describe())

print("\nValores nulos en cada columna:")
print(netflix_df.isnull().sum())

# Descripción de las variables interesantes
print("\nDescripción de variables interesantes del dataset Netflix Titles:")
print("- show_id: ID único para cada título.")
print("- type: Tipo de contenido (película o serie).")
print("- title: Título del contenido.")
print("- director: Director del contenido.")
print("- cast: Actores principales del contenido.")
print("- release_year: Año de estreno.")
print("- rating: Calificación de la película o serie.")
print("- duration: Duración (en minutos para películas, en episodios para series).")


# Dataset 3: Homicide Data
url_homicide = "https://raw.githubusercontent.com/dune0/data-science-1/main/homicide-data.csv"
homicide_df = pd.read_csv(url_homicide, encoding='latin1')  # Se agrega esta línea para problemas de decodificación

# Mostrar las primeras filas del dataset
print("\n--- Dataset: Homicide Data ---")
print("\nPrimeras filas del dataset:")
print(homicide_df.head())

# Información del dataset
print("\nInformación del dataset:")
print(homicide_df.info())

# Estadísticas descriptivas
print("\nEstadísticas descriptivas:")
print(homicide_df.describe())

# Valores nulos
print("\nValores nulos en cada columna:")
print(homicide_df.isnull().sum())

# Descripción de las variables interesantes
print("\nDescripción de variables interesantes del dataset Homicide Data:")
print("- victim_id: ID único de la víctima.")
print("- victim_age: Edad de la víctima.")  # Se corrige la columna 'victim_age'
print("- victim_sex: Género de la víctima.")  # Se usa 'victim_sex' en lugar de 'gender'
print("- victim_race: Raza de la víctima.")
print("- year: Año en que ocurrió el homicidio.")
print("- city: Ciudad donde ocurrió el homicidio.")
print("- state: Estado donde ocurrió el homicidio.")
print("- weapon: Arma utilizada en el homicidio.")

"""
2) Consigna

Elegirás uno de los datasets de la anterior actividad “Elección de Potenciales Datasets e importe con la librería Pandas”. 
Posteriormente, en la misma notebook realizarás 3 gráficos diferentes con Matplotlib y 3 con Seaborn. 
Debe usarse al menos un parámetro adicional (grid, hue, etc) que enriquezca la legibilidad de los charts. 
Finalmente, cada gráfico será interpretado con el fin de obtener insights relevantes que permitan dar respuesta a la pregunta problema.

"""
# Limpiar las columnas relevantes antes de graficar
homicide_df['victim_age'] = pd.to_numeric(homicide_df['victim_age'], errors='coerce')  # Convertir edad a numérico
homicide_df = homicide_df.dropna(subset=['victim_sex'])  # Eliminar filas con valores nulos en 'victim_sex'

# 1. Gráfico de distribución de las edades de las víctimas
plt.figure(figsize=(10, 6))
sns.histplot(homicide_df['victim_age'].dropna(), kde=True, color='skyblue', bins=30)
plt.title('Distribución de las Edades de las Víctimas')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# 2. Gráfico de distribución por género
plt.figure(figsize=(8, 5))
sns.countplot(data=homicide_df, x='victim_sex', hue='victim_sex', palette='Set2', legend=False)
plt.title('Distribución de Homicidios por Género')
plt.xlabel('Género')
plt.ylabel('Número de Homicidios')
plt.grid(True)
plt.show()

# 3. Gráfico de homicidios por tipo de disposición
plt.figure(figsize=(12, 6))
sns.countplot(data=homicide_df, x='disposition', hue='disposition', palette='coolwarm', order=homicide_df['disposition'].value_counts().index, legend=False)
plt.title('Homicidios por Tipo de Disposición')
plt.xlabel('Tipo de Disposición')
plt.ylabel('Número de Homicidios')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# 4. Gráfico de homicidios por estado
plt.figure(figsize=(14, 6))
sns.countplot(data=homicide_df, x='state', hue='state', palette='magma', order=homicide_df['state'].value_counts().index, legend=False)
plt.title('Homicidios por Estado')
plt.xlabel('Estado')
plt.ylabel('Número de Homicidios')
plt.xticks(rotation=90)
plt.grid(True)
plt.show()

# 5. Gráfico de tendencias de homicidios por año
plt.figure(figsize=(10, 6))
sns.lineplot(data=homicide_df, x='reported_date', y=homicide_df.groupby('reported_date').size(), marker='o', color='green')
plt.title('Tendencia de Homicidios por Año')
plt.xlabel('Año')
plt.ylabel('Número de Homicidios')
plt.grid(True)
plt.show()

# 6. Boxplot para comparar las edades de las víctimas por género
plt.figure(figsize=(8, 5))
sns.boxplot(data=homicide_df, x='victim_sex', y='victim_age', hue='victim_sex')
plt.title('Distribución de Edades por Género')
plt.xlabel('Género')
plt.ylabel('Edad de la Víctima')
plt.grid(True)
plt.show()
