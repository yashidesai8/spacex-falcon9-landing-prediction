# SpaceX Launch Records Dashboard (Dash + Plotly)
#
# Lets you pick a launch site (or "All Sites") and a payload mass range, and see the
# success-rate breakdown and the payload-vs-outcome relationship update live.
#
# To run: python SpaceX_Dash_Dashboard.py
# Then open the local URL it prints (something like http://127.0.0.1:8050) in your browser.

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# spacex_launch_geo.csv has all the columns this dashboard needs: Launch Site,
# Payload Mass (kg), Booster Version, and class (1 = successful landing, 0 = not).
spacex_df = pd.read_csv("spacex_launch_geo.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

app = dash.Dash(__name__)
app.title = "SpaceX Launch Records Dashboard"
server = app.server

unique_launch_sites = spacex_df['Launch Site'].unique().tolist()
site_options = [{'label': 'All Sites', 'value': 'All Sites'}]
site_options += [{'label': site, 'value': site} for site in unique_launch_sites]

app.layout = html.Div(children=[

    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),

    dcc.Dropdown(
        id='site_dropdown',
        options=site_options,
        placeholder='Select a Launch Site here',
        searchable=True,
        value='All Sites'
    ),
    html.Br(),

    html.Div(dcc.Graph(id='success-pie-chart')),
    html.Br(),

    html.P("Payload range (Kg):"),

    dcc.RangeSlider(
        id='payload_slider',
        min=0,
        max=10000,
        step=1000,
        marks={i: f'{i} kg' for i in range(0, 10001, 1000)},
        value=[min_payload, max_payload]
    ),

    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])


@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site_dropdown', component_property='value')
)
def update_pie_chart(site_dropdown):
    if site_dropdown == 'All Sites':
        df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(df, names='Launch Site', hole=.3, title='Total Success Launches By All Sites')
    else:
        df = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]
        fig = px.pie(df, names='class', hole=.3, title='Total Success Launches for Site ' + site_dropdown)
    return fig


@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [Input(component_id='site_dropdown', component_property='value'),
     Input(component_id='payload_slider', component_property='value')]
)
def update_scatter_chart(site_dropdown, payload_slider):
    low, high = payload_slider
    if site_dropdown == 'All Sites':
        df = spacex_df
    else:
        df = spacex_df.loc[spacex_df['Launch Site'] == site_dropdown]

    mask = (df['Payload Mass (kg)'] > low) & (df['Payload Mass (kg)'] < high)
    fig = px.scatter(
        df[mask], x="Payload Mass (kg)", y="class",
        color="Booster Version",
        size='Payload Mass (kg)',
        hover_data=['Payload Mass (kg)'],
        title='Payload vs. Outcome' + ('' if site_dropdown == 'All Sites' else f' for {site_dropdown}')
    )
    return fig


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8050)
