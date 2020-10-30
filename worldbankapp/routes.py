from worldbankapp import app
from flask import render_template
import pandas as pd
from wrangling_scripts.wrangling import data_wrangling

import plotly.graph_objs as go
import plotly, json

data = data_wrangling([0])
print(data)

country = data[0][0]
x_val = data[0][1]
y_val = data[0][2]

# graph_one = [go.Scatter(
#     x = data[0][1],
#     y = data[0][2],
#     mode = 'lines',
#     name = country
# )]

graph_one = []
for data_tuple in data:
    graph_one.append(go.Scatter(
    x = data_tuple[1],
    y = data_tuple[2],
    mode = 'lines',
    name = data_tuple[0]
    ))

layout_one = dict(title = 'Change in Hectares Arable Land <br> per Person 1990 to 2015',
            xaxis = dict(title = 'Year',
                autotick=False, tick0=1990, dtick=25),
            yaxis = dict(title = 'Hectares')
                )

figures = []
figures.append(dict(data=graph_one, layout=layout_one))

# Plot ids for the html id tag
ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

figuresJSON = json.dumps(figures, cls=plotly.utils.plotly.utils.PlotlyJSONEncoder)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', ids=ids, figuresJSON=figuresJSON)

@app.route('/project-one')
def project_one():
    return render_template('project_one.html')

@app.route('/virtual-reality')
def virtual_reality():
    return render_template('virtual_reality.html')

@app.route('/data-dashboard')
def data_dashboard():
    return render_template('data_dashboard.html')

@app.route('/about')
def about():
    return render_template('about.html')
