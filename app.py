import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd

# Globals ----------------------------------------------------------------------
VEKTIR_LABS_LOGO = "https://storage.cloud.google.com/anvil_works_bucket/Website_Color_Logo_128.png"
VEKTIR_LABS_LOGO_TEXT = "https://storage.cloud.google.com/anvil_works_bucket/Logo-Text-Only.png"
VEKTIR_LABS_COM = "https://vektirlabs.com"

# App Main --------------------------------------------------------------------
app = Dash(
    title="Vektir Labs",
    external_stylesheets=[dbc.themes.LITERA]
)
server = app.server

# App styles ------------------------------------------------------------------
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "20rem",
    "padding": "1rem 1rem",
    "background-color": "#f8f9fa",
    "textAlign": "center",
    "border-right": "solid rgba(208,208,205,0.6)"
}

NAVBAR_STYLE = {
    "margin-left": "20rem",
    "margin-right": "1rem",
    "padding": "1rem 1rem",
}

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# App components --------------------------------------------------------------
navbar = dbc.NavbarSimple(
            children=[
                dbc.Col(html.Img(src=app.get_asset_url(VEKTIR_LABS_LOGO), height="30px")),
                dbc.DropdownMenu(
                    children=[
                        dbc.DropdownMenuItem("Client Apps", header=True),
                        dbc.DropdownMenuItem("Home", href="/"),
                        dbc.DropdownMenuItem("App 1", href="/App-1"),
                        dbc.DropdownMenuItem("App 2", href="/App-2"),
                    ],
                    nav=True,
                    in_navbar=True,
                    label="More Apps",
                    
                ),
                html.Hr(),
            ],
            brand="Client Name",
            brand_href="#",
            color="white",
            dark=False,
            style=NAVBAR_STYLE,
        )

sidebar = html.Div([
                html.A(
                    href=VEKTIR_LABS_COM,
                    children=[
                        html.Img(
                            alt="VektirLabs.com",
                            src=app.get_asset_url(VEKTIR_LABS_LOGO_TEXT),
                            height="60px"
                        )
                    ]
                ),
                html.Hr(),
            ], style=SIDEBAR_STYLE,
        )

content = html.Div(
            id="page-content",
            children=[], style=CONTENT_STYLE
        )  

url = dcc.Location(id='url')

# App Layout ------------------------------------------------------------------
app.layout = html.Div([
    url, 
    navbar, 
    sidebar, 
    content
])

# Callbacks -------------------------------------------------------------------
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the client home page!")
    elif pathname == "/App-1":
        return html.P("This is the content of App #1. Yay!")
    elif pathname == "/App-2":
        return html.P("This is the content of App #2. Yay!")
    
    # If the user tries to reach a different page, return a 404 message
    return html.Div([
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],className="p-3 bg-light rounded-3",
    )

# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)