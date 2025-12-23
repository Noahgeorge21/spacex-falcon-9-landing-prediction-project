import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

# -------------------------------------------------
# Read the SpaceX launch data
# -------------------------------------------------
spacex_df = pd.read_csv("spacex_launch_dash.csv")

# -------------------------------------------------
# Initialize Dash app
# -------------------------------------------------
app = Dash(__name__)

# -------------------------------------------------
# App Layout
# -------------------------------------------------
app.layout = html.Div(children=[

    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center'}
    ),

    # -------------------------------------------------
    # TASK 1: Launch Site Dropdown
    # -------------------------------------------------
    dcc.Dropdown(
        id='site-dropdown',
        options=[
            {'label': 'All Sites', 'value': 'ALL'},
            {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
            {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
            {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
            {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
        ],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),

    html.Br(),

    # -------------------------------------------------
    # TASK 2: Success Pie Chart
    # -------------------------------------------------
    dcc.Graph(id='success-pie-chart'),

    html.Br(),

    html.P("Payload range (Kg):"),

    # -------------------------------------------------
    # TASK 3: Payload Range Slider
    # -------------------------------------------------
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        marks={
            0: '0',
            2500: '2500',
            5000: '5000',
            7500: '7500',
            10000: '10000'
        },
        value=[0, 10000]
    ),

    html.Br(),

    # -------------------------------------------------
    # TASK 4: Success vs Payload Scatter Plot
    # -------------------------------------------------
    dcc.Graph(id='success-payload-scatter-chart')

])

# -------------------------------------------------
# TASK 2 CALLBACK: Pie Chart
# -------------------------------------------------
@app.callback(
    Output('success-pie-chart', 'figure'),
    Input('site-dropdown', 'value')
)
def update_pie_chart(selected_site):

    if selected_site == 'ALL':
        success_df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            success_df,
            names='Launch Site',
            title='Total Successful Launches by Site'
        )
    else:
        filtered_df = spacex_df[spacex_df['Launch Site'] == selected_site]
        fig = px.pie(
            filtered_df,
            names='class',
            title=f'Success vs Failure for {selected_site}'
        )

    return fig

# -------------------------------------------------
# TASK 4 CALLBACK: Scatter Plot
# -------------------------------------------------
@app.callback(
    Output('success-payload-scatter-chart', 'figure'),
    [
        Input('site-dropdown', 'value'),
        Input('payload-slider', 'value')
    ]
)
def update_scatter_chart(selected_site, payload_range):

    low, high = payload_range

    filtered_df = spacex_df[
        (spacex_df['Payload Mass (kg)'] >= low) &
        (spacex_df['Payload Mass (kg)'] <= high)
    ]

    if selected_site != 'ALL':
        filtered_df = filtered_df[
            filtered_df['Launch Site'] == selected_site
        ]

    fig = px.scatter(
        filtered_df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Payload vs Launch Outcome'
    )

    return fig

# -------------------------------------------------
# Run the app
# -------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
