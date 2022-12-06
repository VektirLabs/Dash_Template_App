import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd
from components import sidebar as sb
from components import navbar as nb
from components import content as cb

# Main App --------------------------------------------------------------------
app = Dash(external_stylesheets=[dbc.themes.LITERA])

# App components --------------------------------------------------------------
navbar  = nb.get_navbar()
sidebar = sb.get_sidebar()
content = cb.get_page_content()
url = dcc.Location(id='url')

# App Layout ------------------------------------------------------------------
app.layout = html.Div([url, navbar, sidebar, content])

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