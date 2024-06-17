import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Función para convertir cadenas con sufijo 'K', 'M' o 'B' a valores numéricos
def convert_to_numeric(value):
    if 'K' in value:
        return float(value.replace('K', '')) * 1000
    elif 'M' in value:
        return float(value.replace('M', '')) * 1000000
    elif 'B' in value:
        return float(value.replace('B', '')) * 1000000000
    else:
        return float(value)

# Cargar datos y limpiar columnas numéricas
data = pd.read_csv("youtube.csv", converters={
    'TOTAL_NUMBER_OF_VIDEOS': convert_to_numeric,
    'SUBSCRIBERS': convert_to_numeric,
    'VIEWS': convert_to_numeric
})

# Ajuste de nombres de columnas para que coincidan con los del dataset
data.columns = ['RANK', 'Channel Name', 'TOTAL_NUMBER_OF_VIDEOS', 'SUBSCRIBERS', 'VIEWS', 'CATEGORY']

# Seleccionar solo las columnas numéricas para calcular la correlación
numeric_data = data[['TOTAL_NUMBER_OF_VIDEOS', 'SUBSCRIBERS', 'VIEWS']]
# 1. Mapa de calor de correlaciones
corr_ds = numeric_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr_ds, annot=True)
plt.title('Mapa de calor de correlaciones')
plt.show()

# 2. Distribución del número de videos subidos
plt.figure(figsize=(10, 6))
sns.histplot(data['TOTAL_NUMBER_OF_VIDEOS'], bins=50, kde=True)
plt.title('Distribución del número de videos subidos')
plt.xlabel('Total Videos')
plt.ylabel('Frecuencia')
plt.show()

# 3. Distribución del número de vistas
plt.figure(figsize=(10, 6))
sns.histplot(data['VIEWS'], bins=50, kde=True)
plt.title('Distribución del número de vistas')
plt.xlabel('Total Views')
plt.ylabel('Frecuencia')
plt.show()

# 4. Distribución del número de suscriptores
plt.figure(figsize=(10, 6))
sns.histplot(data['SUBSCRIBERS'], bins=50, kde=True)
plt.title('Distribución del número de suscriptores')
plt.xlabel('Total Subscribers')
plt.ylabel('Frecuencia')
plt.show()

# 5. Scatter plot de Suscriptores vs Vistas
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SUBSCRIBERS', y='VIEWS', data=data)
plt.title('Suscriptores vs Vistas')
plt.xlabel('Total Subscribers')
plt.ylabel('Total Views')
plt.show()

# 6. Scatter plot de Suscriptores vs Videos
plt.figure(figsize=(10, 6))
sns.scatterplot(x='SUBSCRIBERS', y='TOTAL_NUMBER_OF_VIDEOS', data=data)
plt.title('Suscriptores vs Videos')
plt.xlabel('Total Subscribers')
plt.ylabel('Total Videos')
plt.show()

# 7. Gráfico de barras de los 10 canales con más suscriptores
top_10_subs = data.nlargest(10, 'SUBSCRIBERS')
plt.figure(figsize=(10, 6))
sns.barplot(x='SUBSCRIBERS', y='Channel Name', data=top_10_subs)
plt.title('Top 10 canales con más suscriptores')
plt.xlabel('Total Subscribers')
plt.ylabel('Channel Name')
plt.show()

# 8. Gráfico de barras de los 10 canales con más vistas
top_10_views = data.nlargest(10, 'VIEWS')
plt.figure(figsize=(10, 6))
sns.barplot(x='VIEWS', y='Channel Name', data=top_10_views)
plt.title('Top 10 canales con más vistas')
plt.xlabel('Total Views')
plt.ylabel('Channel Name')
plt.show()

# 9. Gráfico de barras de los 10 canales con más videos
top_10_videos = data.nlargest(10, 'TOTAL_NUMBER_OF_VIDEOS')
plt.figure(figsize=(10, 6))
sns.barplot(x='TOTAL_NUMBER_OF_VIDEOS', y='Channel Name', data=top_10_videos)
plt.title('Top 10 canales con más videos subidos')
plt.xlabel('Total Videos')
plt.ylabel('Channel Name')
plt.show()
