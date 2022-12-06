import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd

# Globals ----------------------------------------------------------------------
VEKTIR_LOGO = "/assets/img/Website_Color_Logo.png"
VEKTIR_TEXT = "/assets/img/Logo-Text-Only.png"
VEKTIR_COM = "https://vektirlabs.com"

# Navbar -----------------|
NAVBAR_STYLE = {
    "margin-left": "20rem",
    "margin-right": "1rem",
    "padding": "1rem 1rem",
}

def get_navbar():
    return dbc.NavbarSimple(
            children=[
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