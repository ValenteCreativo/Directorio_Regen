import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objects as go

# Leer el archivo CSV
df = pd.read_csv('/Users/valentinmartinez/Documents/TAAK STUDIO/Urbanika/Directorio_Ecotecnias/DirectorioFinal_EcotecUnam.csv')

# Convertir la columna de Ubicación en datos numéricos para el eje z
df['Ubicación_Num'] = pd.factorize(df['Ubicación'])[0]

# Convertir la Categoría en valores numéricos para los colores
df['Categoría_Num'] = pd.factorize(df['Categoría'])[0]

# Crear un scatter plot 3D con más información
fig = go.Figure(data=[go.Scatter3d(
    x=df['Categoría_Num'],
    y=df['Nombre'],
    z=df['Ubicación_Num'],
    mode='markers',
    marker=dict(
        size=12,
        color=df['Categoría_Num'],  # Color basado en la categoría numérica
        colorscale='Viridis',
        opacity=0.8
    ),
    text=df.apply(lambda row: f'Nombre: {row["Nombre"]}<br>Actividad: {row["Actividad"]}<br>Teléfono: {row["Teléfono"]}<br>Correo: {row["Correo"]}', axis=1)
)])

fig.update_layout(
    title='Visualización 3D de Ecotecnologías',
    scene=dict(
        xaxis_title='Categoría',
        yaxis_title='Nombre',
        zaxis_title='Ubicación (Num)'
    ),
    margin=dict(l=0, r=0, b=0, t=50)
)

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Directorio de Ecotecnologías'),
    dcc.Graph(
        id='3d-scatter-graph',
        figure=fig
    )
])

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True, port=8090)  # Cambiar el puerto
