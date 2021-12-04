#Name : Chirag Manchanda
#Roll no.: 101903257
#Batch : 3CO10

#Dashboard design for Most Popular Programming Languages since 2004

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# dataset from https://www.kaggle.com/muhammadkhalid/most-popular-programming-languages-since-2004 
#download datset first

df = pd.read_csv(r'Most Popular Programming Languages from 2004 to 2021.csv')

#df.head()
#df.columns

#dash layout

app = dash.Dash(__name__)                                       

app.layout = html.Div([
    html.H1('Programming Language popularity Dashboard'),          #styling component in dash
    html.H2('Select any language from dropdown'),
    dcc.Dropdown(                                                  #display drop down list(dash core component) 
        id='demo-dropdown',
        options=[
            {'label': 'Python', 'value': 'Python'},
            {'label': 'Go', 'value': 'Go'},
            {'label': 'C/C++', 'value': 'C/C++'},
            {'label': 'C#', 'value': 'C#'},
            {'label': 'PHP', 'value': 'PHP'},
            {'label': 'Dart', 'value': 'Dart'},
            {'label': 'Java', 'value': 'Java'},
            {'label': 'JavaScript', 'value': 'JavaScript'},
            {'label': 'Matlab', 'value': 'Matlab'},
            {'label': 'R', 'value': 'R'},
            {'label': 'Scala', 'value': 'Scala'},
            {'label': 'Swift', 'value': 'Swift'},
            {'label': 'TypeScript', 'value': 'TypeScript'},
        
        ],
        value='Python'                                           #default value fixed to python
    ),
    dcc.Graph(id="graph")                                       #output graph component
])


@app.callback(
    Output("graph", "figure"),                            # Whenever an input property changes, the function that the callback decorator wraps will get called automatically.
    [Input('demo-dropdown', 'value')])                    # The component_id and component_property keywords are optional
def update_value(value):
    fig = px.line(df, x='Date', y=value)                 #after chosing value from drop down list it's passed to update method and assigned to y axis                                                      
    return fig                                           # return figure to the running machine


app.run_server(debug=True)   
#run this in vs code or use False instead of true for jupyter and colab
#Dash includes "hot-reloading", this features is activated by default when you run your app with app.run_server(debug=True).
# This means that Dash will automatically refresh your browser when you make a change in your code.
#Visit http://127.0.0.1:8050/ in your web browser.
