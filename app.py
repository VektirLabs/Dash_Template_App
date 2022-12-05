import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd

# Main App --------------------------------------------------------------------
app = Dash(external_stylesheets=[dbc.themes.LITERA])

# Set Up ----------------------------------------------------------------------
VEKTIR_LOGO = "/assets/img/Website_Color_Logo.png"
VEKTIR_TEXT = "/assets/img/Logo-Text-Only.png"

# Sidebar
sidebar = html.Div([
    dbc.Offcanvas(
        html.P("Welcome to Vektir Labs"),
        id="offcanvas-backdrop",
        title="Vektir Labs",
        is_open=False,
    ),
])

# Navbar 
navbar = dbc.Row(
    children=[
        dbc.Col(html.P(''),width=2),
        dbc.Col(html.Img(src=VEKTIR_TEXT, height="60px",),className='text-center',width=8),
        dbc.Col([
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("App List", header=True),
                    dbc.DropdownMenuItem("App 1", href="#"),
                    dbc.DropdownMenuItem("App 2", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="Apps",
            )
            
            ],width=2,),
        html.P(''),
        html.Hr(),
    ]
    ,style={"margin":"10", "background":"white"}
)

# Data ------------------------------------------------------------------------
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# App layout ------------------------------------------------------------------
app.layout = html.Div(
    children=[
        navbar,
        # sidebar,
        dbc.Row([
            dbc.Col(
                html.Div([
                    dcc.Graph(
                        id='example-graph',
                        figure=fig
                        )
                ], style={'margin':20, 'textAlign': 'center'}),width=12), 
        ]),
    ]
)

# Callbacks -------------------------------------------------------------------
# Sidebar toggle
# @app.callback(
#     Output("offcanvas-backdrop", "is_open"),
#     Input("open-offcanvas-backdrop", "n_clicks"),
#     State("offcanvas-backdrop", "is_open"),
# )
# def toggle_offcanvas(n1, is_open):
#     if n1:
#         return not is_open
#     return is_open

# Navbar toggle
# @app.callback(
#     Output("navbar-collapse", "is_open"),
#     [Input("navbar-toggler", "n_clicks")],
#     [State("navbar-collapse", "is_open")],
# )
# def toggle_navbar_collapse(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)