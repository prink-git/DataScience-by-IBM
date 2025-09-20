import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the dropdown menu options
dropdown_options = [
    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
]

# List of years
year_list = [i for i in range(1980, 2024, 1)]

# Layout of the app
app.layout = html.Div([
    html.H1('US Domestic Airline Flights Performance',
            style={'textAlign': 'center', 'color': '#503D36', 'fontSize': 24}),
    
    html.Div([
        dcc.Dropdown(
            id='dropdown-statistics',
            options=dropdown_options,
            placeholder='Select a report type',
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlign': 'center'}
        )
    ], style={'display': 'flex', 'justifyContent': 'center'}),

    html.Div([
        html.Div([html.H2('Choose Year:', style={'marginRight': '2em'})]),
        dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            placeholder="Select a year",
            style={'width': '80%', 'padding': '3px', 'fontSize': '20px', 'textAlign': 'center'},
            disabled=True
        )
    ], style={'display': 'flex', 'justifyContent': 'center'}),

    html.Div([html.Div(id='output-container', className='chart-grid', style={'display': 'flex', 'flexDirection': 'column'})])
])

# Enable/disable year dropdown
@app.callback(
    Output('select-year', 'disabled'),
    Input('dropdown-statistics', 'value')
)
def update_input_container(selected_statistic):
    return selected_statistic != 'Yearly Statistics'

# Generate graphs
@app.callback(
    Output('output-container', 'children'),
    [Input('dropdown-statistics', 'value'),
     Input('select-year', 'value')]
)
def update_output_container(selected_statistic, input_year):
    if selected_statistic == 'Recession Period Statistics':
        recession_data = data[data['Recession'] == 1]

        # Plot 1
        yearly_rec = recession_data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        R_chart1 = dcc.Graph(figure=px.line(yearly_rec, x='Year', y='Automobile_Sales',
                                            title='Automobile Sales Over Recession Years'))

        # Plot 2
        average_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        R_chart2 = dcc.Graph(figure=px.bar(average_sales, x='Vehicle_Type', y='Automobile_Sales',
                                           title='Average Vehicle Sales by Type During Recession'))

        # Plot 3
        exp_rec = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(figure=px.pie(exp_rec, values='Advertising_Expenditure', names='Vehicle_Type',
                                           title='Advertising Expenditure Share by Vehicle Type During Recession'))

        # Plot 4
        unemp_data = recession_data.groupby(['unemployment_rate', 'Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
        R_chart4 = dcc.Graph(figure=px.bar(unemp_data, x='unemployment_rate', y='Automobile_Sales', color='Vehicle_Type',
                                           title='Effect of Unemployment Rate on Vehicle Type and Sales'))

        return [
            html.Div([html.Div(R_chart1), html.Div(R_chart2)], style={'display': 'flex'}),
            html.Div([html.Div(R_chart3), html.Div(R_chart4)], style={'display': 'flex'})
        ]

    elif input_year and selected_statistic == 'Yearly Statistics':
        yearly_data = data[data['Year'] == input_year]

        # Plot 1
        yas = data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(yas, x='Year', y='Automobile_Sales',
                                            title='Average Yearly Automobile Sales Over the Years'))

        # Plot 2
        mas = data.groupby('Month')['Automobile_Sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(figure=px.line(mas, x='Month', y='Automobile_Sales',
                                            title='Total Monthly Automobile Sales'))

        # Plot 3
        avr_vdata = yearly_data.groupby('Vehicle_Type')['Automobile_Sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata, x='Vehicle_Type', y='Automobile_Sales',
                                           title=f'Average Vehicles Sold by Vehicle Type in {input_year}'))

        # Plot 4
        exp_data = yearly_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(figure=px.pie(exp_data, values='Advertising_Expenditure', names='Vehicle_Type',
                                           title='Total Advertisement Expenditure by Vehicle Type'))

        return [
            html.Div([html.Div(Y_chart1), html.Div(Y_chart2)], style={'display': 'flex'}),
            html.Div([html.Div(Y_chart3), html.Div(Y_chart4)], style={'display': 'flex'})
        ]

    return html.Div("No valid input provided.")

# Run the Dash app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)

