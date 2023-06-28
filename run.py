import pandas as pd
from pandasgui import show
df = pd.read_csv('cars.csv')

show(df.describe())

# Ver las primeras filas del DataFrame
df.head()

# Ver las últimas filas del DataFrame
df.tail()

# Obtener información sobre el DataFrame
df.info()

# Obtener estadísticas descriptivas del DataFrame
df.describe()

# Seleccionar columnas específicas
df['Name']

# Filtrar filas basado en condiciones
df[df['Age'] > 30]

# Agregar una nueva columna
df['Nationality'] = 'USA'

# Eliminar una columna
df = df.drop('Nationality', axis=1)

# Ordenar el DataFrame por una columna específica
df = df.sort_values('Age')

# Agrupar y resumir datos
df.groupby('Nationality')['Age'].mean()

# Fusionar dos DataFrames
merged_df = pd.merge(df1, df2, on='ID')

# Aplicar una función a una columna
df['Age'] = df['Age'].apply(lambda x: x + 1)

# Aplicar una función a cada elemento del DataFrame
df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
