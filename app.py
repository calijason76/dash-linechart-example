import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "US Population Growth for DC, MD, and VA: 1960 thru 2010"
mytitle = "DMV Area Population Statistics"
x_values = ['1960', '1970', '1980', '1990', '2000', '2010']
y1_values = [763956, 756510, 638333, 606900, 572059, 601723]
y2_values = [3970000, 4650000, 5350000, 6190000, 7080000, 8020000]
y3_values = [3100000, 3920000, 4220000, 4780000, 5300000, 5790000]
color1 = '#fc9403'
color2 = '#0307fc'
color3 = '#9003fc'
name1 = 'Washington, DC'
name2 = 'Virginia'
name3 = 'Maryland'
tabtitle = 'DMV Population'
sourceurl = 'https://www.multpl.com/united-states-population/table/by-year'
githublink = 'https://github.com/calijason76/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Grab My Code!', href=githublink, style={'text-align': 'center'}),
    html.Br(),
    html.A("My Numbers are Legit!", href=sourceurl, style={'text-align': 'center'}),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
