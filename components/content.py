import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# Content section --------------------------------------------------------\
def get_page_content():
    return html.Div(
            id="page-content",
            children=[], style=CONTENT_STYLE
        )   