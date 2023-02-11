from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc

from recycle_app.recyclingchart import RecyclingChart
from recycle_app.recyclingdata import RecyclingData


# Prepare the data set
data = RecyclingData()
area = "London"
data.process_data_for_area(area)

# Create the figures
rc = RecyclingChart(data)
fig_rc = rc.create_chart(area)

# Create a Dash app (using bootstrap).
app = Dash(
    external_stylesheets=[dbc.themes.LUX],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)

# Create the app layout using Bootstrap fluid container
app.layout = dbc.Container(
    fluid=True,
    children=[
        html.Br(),
        # First row here, this does not use a dbc.Row(dbc.Col()) since the effect is the same without it
        html.H1("Waste and recycling"),
        html.P(
            "Turn London waste into an opportunity – by reducing waste, reusing and recycling more of it.",
            className="lead",
        ),
        # As above but using a dbc.Row(dcb.Col()) so you can see the syntax difference
        dbc.Row(
            dbc.Col(
                children=[
                    html.H2("How does your area compare?"),
                    html.P(
                        "Select an area to see how it compares to the average for England",
                        className="lead",
                    ),
                ]
            )
        ),
        # Second row here
        dbc.Row(
            [
                # This is for the London area selector and the statistics panel.
                dbc.Col(
                    width=3,
                    children=[
                        html.H4("Select Area"),
                        dcc.Dropdown(
                            id="area-select",
                            options=[
                                {"label": x, "value": x}
                                for x in data.area_list
                            ],
                            value="London",
                        ),
                        html.Br(),
                        html.Div(id="stats-card"),
                    ],
                ),
                # Add the second column here. This is for the figure.
                dbc.Col(
                    width=9,
                    children=[
                        html.H2("Recycling"),
                        dcc.Graph(id="recycle-chart", figure=fig_rc),
                    ],
                ),
            ]
        ),
    ],
)


@app.callback(Output("recycle-chart", "figure"), Input("area-select", "value"))
def update_recycling_chart(area_select):
    fig_rc = rc.create_chart(area_select)
    return fig_rc


@app.callback(Output("stats-card", "children"), Input("area-select", "value"))
def render_stats_panel(area_select):
    # Get the statistics
    data.process_data_for_area(area_select)
    comp_to_eng = f"{data.compare_to_eng:,.0f}"
    comp_to_prev_year = f"{data.change_area:,.0f}"
    best_period = f"{data.best_period}"
    recycling_rate = f"with recycling rate {data.best_rate:,.0f}%"

    # Generate the bootstrap format card with the statistics
    card = dbc.Card(
        className="bg-dark text-light",
        children=[
            dbc.CardBody(
                [
                    html.H4(
                        area_select, id="card-name", className="card-title"
                    ),
                    html.Br(),
                    html.H6("Compared to England:", className="card-title"),
                    html.H4(comp_to_eng, className="card-text text-light"),
                    html.Br(),
                    html.H6(
                        "Compared to previous year:", className="card-title"
                    ),
                    html.H4(
                        comp_to_prev_year, className="card-text text-light"
                    ),
                    html.Br(),
                    html.H6("Best period:", className="card-title"),
                    html.H4(best_period, className="card-text text-light"),
                    html.H6(recycling_rate, className="card-title text-light"),
                    html.Br(),
                ]
            )
        ],
    )
    return card


# Merged version
"""
@app.callback(
    Output("stats-card", "children"),
    Output("recycle-chart", "figure"),
    [Input("area-select", "value")])
def render_stats_chart(area_select):
    data.process_data_for_area(area_select)
    comp_to_eng = f'{data.compare_to_eng:,.0f}'
    comp_to_prev_year = f'{data.change_area:,.0f}'
    best_period = f'{data.best_period}'
    recycling_rate = f'with recycling rate {data.best_rate:,.0f}%'
    card = dbc.Card(className="bg-dark text-light", children=[
        dbc.CardBody([
            html.H4(area_select, id="card-name", className="card-title"),
            html.Br(),
            html.H6("Compared to England:", className="card-title"),
            html.H4(comp_to_eng, className="card-text text-light"),
            html.Br(),
            html.H6("Compared to previous year:", className="card-title"),
            html.H4(comp_to_prev_year, className="card-text text-light"),
            html.Br(),
            html.H6("Best period:", className="card-title"),
            html.H4(best_period, className="card-text text-light"),
            html.H6(recycling_rate, className="card-title text-light"),
            html.Br()
        ])
    ])
    fig_rc = rc.create_chart(area_select)
    return card, fig_rc
"""

if __name__ == "__main__":
    app.run_server(debug=True)
