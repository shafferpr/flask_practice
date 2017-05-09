from flask import Flask,render_template,request,redirect
import requests
from bokeh.plotting import figure
from bokeh.embed import components
stock = 'aapl'

api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % stock
session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
raw_data = session.get(api_url)


plot = figure(tools=TOOLS,
              title='Data from Quandle WIKI set',
              x_axis_label='date',
              x_axis_type='datetime')

script, div = components(plot)
render_template('graph.html', script=script, div=div)
