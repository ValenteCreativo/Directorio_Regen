import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Cargar el CSV
df = pd.read_csv('/Users/valentinmartinez/Documents/TAAK STUDIO/Urbanika/Directorio_Ecotecnias/DirectorioFinal_EcotecUnam.csv')

# Inicializar la app Dash
app = dash.Dash(__name__)

# Estilos CSS personalizados
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Layout de la app
app.layout = html.Div(style={'backgroundColor': '#f7f7f7', 'padding': '10px', 'fontFamily': 'Montserrat'}, children=[
    html.Div(style={
        'background': 'linear-gradient(135deg, #38b6ff, #32de8a)', 
        'padding': '15px',  
        'color': 'white', 
        'textAlign': 'center', 
        'borderRadius': '6px',
        'boxShadow': '0px 2px 5px rgba(0, 0, 0, 0.1)',
        'marginBottom': '10px'
    }, children=[
        html.A([
            html.Img(src='https://i.ibb.co/VCDpZRT/Urbanika-Logo.png', style={'width': '100px', 'margin': '5px auto', 'display': 'block'})],
            href='#'
        ),
        html.H1(children='Urbanika ReFi Portfolio', style={'fontSize': '2em', 'fontWeight': 'bold'}) 
    ]),
    html.Div(style={'display': 'flex', 'flexDirection': 'row', 'gap': '10px'}, children=[
        html.Div(style={
            'width': '20%', 
            'padding': '8px', 
            'backgroundColor': '#a5d6a7', 
            'borderRadius': '6px', 
            'boxShadow': '0px 2px 5px rgba(0, 0, 0, 0.1)',
            'position': 'sticky',
            'top': '10px'
        }, children=[
            html.H2("Categorías", style={'fontSize': '1.1em', 'color': '#388e3c', 'marginBottom': '6px'}),
            dcc.Dropdown(
                id='dropdown-categorias',
                options=[{'label': cat, 'value': cat} for cat in df['Categoría'].unique()],
                placeholder="Selecciona una categoría",
                style={
                    'fontSize': '0.85em',
                    'borderRadius': '5px',
                    'boxShadow': '0px 2px 5px rgba(0, 0, 0, 0.1)',
                    'padding': '4px',
                    'marginBottom': '10px'
                }
            ),
            dcc.Input(
                id='search-box',
                type='text',
                placeholder='Buscar...',
                style={
                    'fontSize': '0.85em',
                    'padding': '8px',
                    'borderRadius': '5px',
                    'boxShadow': '0px 2px 5px rgba(0, 0, 0, 0.1)',
                    'width': '100%',
                    'marginBottom': '10px'
                }
            ),
            html.Div([
                html.P("Esta lista fue creada gracias a la información obtenida de las siguientes organizaciones:", style={'fontSize': '0.75em', 'color': '#616161'}),
                html.Ul(style={'fontSize': '0.75em', 'color': '#616161', 'lineHeight': '1.5', 'listStyleType': 'none', 'paddingLeft': '0'}, children=[
                    html.Li([html.Span("Secretaría de Desarrollo Económico, Jalisco: "), html.A("sedeco.jalisco.gob.mx", href="https://sedeco.jalisco.gob.mx/sites/sedeco.jalisco.gob.mx/files/directorio_de_proveedores_verdes.pdf", target='_blank')]),
                    html.Li([html.Span("Portal Ambiental: "), html.A("portalambiental.com.mx", href="https://www.portalambiental.com.mx/directorio", target='_blank')]),
                    html.Li([html.Span("Ecotec UNAM: "), html.A("ecotec.unam.mx", href="https://ecotec.unam.mx/ecoteca-inicio/directorio-organizaciones-ecotecnias", target='_blank')])
                ])
            ])
        ]),
        html.Div(id='info-categoria', style={
            'width': '75%', 
            'padding': '8px', 
            'backgroundColor': '#ffffff', 
            'borderRadius': '6px', 
            'boxShadow': '0px 2px 5px rgba(0, 0, 0, 0.1)',
            'fontSize': '0.95em',
            'color': '#424242',
            'textAlign': 'justify',
            'transition': 'all 0.3s ease',
            'lineHeight': '1.5'
        }, children=[
            html.P(
                "Urbanika es una iniciativa que busca sembrar las bases para la emergencia de ciudades inteligentes y autosostenibles, regidas por una economía circular y prácticas de urbanismo común. A través de este directorio, queremos facilitar el acceso a tecnologías regenerativas, ayudando a las personas y organizaciones a transformar su forma de vida hacia un modelo más sostenible. ¡Explora las categorías o busca una organización para conocer más sobre estas innovadoras soluciones!",
                style={'textAlign': 'center', 'fontSize': '1.1em', 'color': '#616161', 'marginBottom': '20px'}
            ),
            html.P(
                "Selecciona una categoría o realiza una búsqueda para ver los detalles.",
                style={'textAlign': 'center', 'fontSize': '1.1em', 'color': '#616161'}
            )
        ])
    ]),
    html.Div(style={'textAlign': 'center', 'marginTop': '20px'}, children=[
        html.P([
            "Para más información visitar: ",
            html.A("Urbanika.Notion.Site", href="https://urbanika.notion.site", style={'color': '#388e3c', 'textDecoration': 'underline'})  
        ])
    ])
])

@app.callback(
    Output('info-categoria', 'children'),
    [Input('dropdown-categorias', 'value'),
     Input('search-box', 'value')]
)
def update_content_and_hover(selected_category, search_value):
    if selected_category is None and search_value is None:
        return html.Div([
            html.P(
                "Urbanika es una iniciativa que busca sembrar las bases para la emergencia de ciudades inteligentes y autosostenibles, regidas por una economía circular y prácticas de urbanismo común. A través de este directorio, queremos facilitar el acceso a tecnologías regenerativas, ayudando a las personas y organizaciones a transformar su forma de vida hacia un modelo más sostenible. ¡Explora las categorías o busca una organización para conocer más sobre estas innovadoras soluciones!",
                style={'textAlign': 'center', 'fontSize': '1.1em', 'color': '#616161', 'marginBottom': '20px'}
            ),
            html.P(
                "Selecciona una categoría o realiza una búsqueda para ver los detalles.",
                style={'textAlign': 'center', 'fontSize': '1.1em', 'color': '#616161'}
            )
        ])
    
    filtered_df = df[df['Categoría'] == selected_category] if selected_category else df
    
    if search_value:
        filtered_df = filtered_df[filtered_df.apply(lambda row: search_value.lower() in row['Nombre'].lower(), axis=1)]
    
    category_info = html.Div([
        html.H2(f"Organizaciones en la categoría {selected_category}" if selected_category else "Resultados de búsqueda", style={
            'textAlign': 'center', 
            'fontSize': '1.6em', 
            'color': '#388e3c',
            'marginBottom': '10px'
        }),
        html.Ul(children=[
            html.Li(style={
                'marginBottom': '12px', 
                'padding': '8px', 
                'borderRadius': '6px', 
                'backgroundColor': '#f1f8e9', 
                'boxShadow': '0px 2px 5px rgba(0, 0, 0, 0.1)',
                'cursor': 'default'
            }, children=[
                html.P(f"Nombre: {row['Nombre']}", style={'fontWeight': 'bold', 'color': '#2e7d32'}),
                html.P(f"Ubicación: {row['Ubicación']}"),
                html.P(f"Actividad: {row['Actividad']}"),
                html.P(f"Teléfono: {row['Teléfono']}"),
                html.P(f"Correo: {row['Correo']}"),
                html.P([
                    "Sitio Web: ",
                    html.A(row['Sitio Web'], href=row['Sitio Web'], target='_blank', style={'color': '#388e3c', 'textDecoration': 'underline'})
                ]),
                html.A("Link", href=row['Link'], target="_blank", style={'color': '#388e3c', 'textDecoration': 'underline'})
            ]) for index, row in filtered_df.iterrows()
        ], style={'padding': '0', 'listStyleType': 'none'})
    ])
    
    return category_info

# Ejecutar la app
if __name__ == '__main__':
    app.run_server(debug=True)(port=8050)
