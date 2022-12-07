import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd

# Globals ----------------------------------------------------------------------
VEKTIR_LABS_LOGO = "https://github.com/VektirLabs/Dash_Template_App/blob/v1.0/assets/img/Website_Color_Logo.png"
VEKTIR_LABS_LOGO_TEXT = "https://storage.cloud.google.com/anvil_works_bucket/Logo-Text-Only.png"
VEKTIVEKTIR_LABS_COM = "https://vektirlabs.com"


# Sidebar ----------------|
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
def get_sidebar():
    return html.Div([
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
