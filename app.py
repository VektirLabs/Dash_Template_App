import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, html, dcc
import plotly.express as px
import pandas as pd

# Main App --------------------------------------------------------------------
app = Dash(__name__)

# Data ------------------------------------------------------------------------
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Sidebar panel ---------------------------------------------------------------
backdrop_selector = html.Div(
    [
        dbc.Label("Backdrop:"),
        dbc.RadioItems(
            id="offcanvas-backdrop-selector",
            options=[
                {"label": "True (default)", "value": True},
                {"label": "False", "value": False},
                {"label": "Static (no dismiss)", "value": "static"},
            ],
            inline=True,
            value=True,
        ),
    ],
    className="mb-2",
)

offcanvas = html.Div(
    [
        backdrop_selector,
        dbc.Button(
            "Open backdrop offcanvas", id="open-offcanvas-backdrop", n_clicks=0
        ),
        dbc.Offcanvas(
            html.P("Here is some content..."),
            id="offcanvas-backdrop",
            title="Offcanvas with/without backdrop",
            is_open=False,
        ),
    ]
)

# App layout ------------------------------------------------------------------
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    offcanvas,
    backdrop_selector
])

# Callbacks -------------------------------------------------------------------
@app.callback(
    Output("offcanvas-backdrop", "backdrop"),
    [Input("offcanvas-backdrop-selector", "value")],
)
def select_backdrop(backdrop):
    return backdrop


@app.callback(
    Output("offcanvas-backdrop", "is_open"),
    Input("open-offcanvas-backdrop", "n_clicks"),
    State("offcanvas-backdrop", "is_open"),
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open

# Main ------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)