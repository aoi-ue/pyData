import plotly
plotly.tools.set_credentials_file(username='SandeepSingh', api_key='UnB6UI5RTJVMzzK4eQUx')
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame

import pandas as pd
from index import df, COUNTRY_SVOD, COUNTRY_TVOD

labels = ['ID SVOD', 'TH SVOD', 'PH_SVOD', 'SG_SVOD', 'IN_SVOD']
values = COUNTRY_SVOD
colors = ['#822B24', '#1B4F6A', '#36614F', '#A94B35', '#571F4E']

trace = go.Pie(labels=labels, values=values,
               hoverinfo='label+value', textinfo='label+percent', 
               textfont=dict(size=14),
               marker=dict(colors=colors, 
                           line=dict(color='#000000', width=2)))

py.iplot([trace], filename='styled_pie_chart')
