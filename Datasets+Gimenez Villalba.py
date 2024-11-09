import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# Descripción de las variables interesantes del dataset Diabetes
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

# Descripción de las variables interesantes del dataset Netflix Titles
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
homicide_df = pd.read_csv(url_homicide, encoding='latin1')  # Solución al problema de decodificación

print("\n--- Dataset: Homicide Data ---")
print("\nPrimeras filas del dataset:")
print(homicide_df.head())

print("\nInformación del dataset:")
print(homicide_df.info())

print("\nEstadísticas descriptivas:")
print(homicide_df.describe())

print("\nValores nulos en cada columna:")
print(homicide_df.isnull().sum())

# Descripción de las variables interesantes del dataset Homicide Data
print("\nDescripción de variables interesantes del dataset Homicide Data:")
print("- victim_id: ID único de la víctima.")
print("- age: Edad de la víctima.")
print("- gender: Género de la víctima.")
print("- race: Raza de la víctima.")
print("- year: Año en que ocurrió el homicidio.")
print("- city: Ciudad donde ocurrió el homicidio.")
print("- state: Estado donde ocurrió el homicidio.")
print("- weapon: Arma utilizada en el homicidio.")

