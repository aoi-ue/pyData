import plotly
plotly.tools.set_credentials_file(username='SandeepSingh', api_key='UnB6UI5RTJVMzzK4eQUx')
import plotly.plotly as py
import plotly.graph_objs as go
from IPython.display import IFrame

from panda import df, todaydate, new_end_lic_list, old_end_lic_list

#########################################################################################################
#Capturing the total hours for SVOD and TVOD

svod_td = [df[(df['vod_type'] == 'SVOD') & (df[i] >= todaydate)]['duration'].sum() for i in new_end_lic_list]
tvod_td = [df[(df['vod_type'] == 'TVOD') & (df[i] >= todaydate)]['duration'].sum() for i in new_end_lic_list]

#Creating separate data frames for the individual countries

svemp = []
tvemp = []

for i in old_end_lic_list:
    svemp.append(df[(df['vod_type'] == 'SVOD') & (df[i] >= todaydate)])
    
for i in old_end_lic_list:
    tvemp.append(df[(df['vod_type'] == 'TVOD') & (df[i] >= todaydate)])

ID_svoddf = svemp[0]
TH_svoddf = svemp[1]
PH_svoddf = svemp[2]
SG_svoddf = svemp[3]
IN_svoddf = svemp[4]

ID_tvoddf = tvemp[0]
TH_tvoddf = tvemp[1]
PH_tvoddf = tvemp[2]
SG_tvoddf = tvemp[3]
IN_tvoddf = tvemp[4]




### ID Hours

indo_sub_dub_list = ['ENG_SUB', 'BH_SUB', 'BH_DUB']
indo_svod_emp_list = []
indo_tvod_emp_list = []

for i in indo_sub_dub_list:
    a = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Current') & (ID_svoddf[i] == 'Live')]['duration'].sum()
    b = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Future') & (ID_svoddf[i] == 'Live')]['duration'].sum()
    c = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Current') & (ID_svoddf[i] == 'Not Live')]['duration'].sum()
    d = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Future') & (ID_svoddf[i] == 'Not Live')]['duration'].sum()
    e = ID_svoddf[(ID_svoddf['ID_TimePeriod'] == 'Expiring') & (ID_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Current') & (ID_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Future') & (ID_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Current') & (ID_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = ID_tvoddf[(ID_tvoddf['ID_TimePeriod'] == 'Future') & (ID_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = ID_tvoddf[(ID_tvoddf['ID_Expiring'] == 'Expiring') & (ID_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    indo_svod_emp_list.append(total)
    indo_tvod_emp_list.append(total2)

### TH Hours

thai_sub_dub_list = ['ENG_SUB', 'TH_SUB', 'TH_DUB']
thai_svod_emp_list = []
thai_tvod_emp_list = []

for i in thai_sub_dub_list:
    a = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Current') & (TH_svoddf[i] == 'Live')]['duration'].sum()
    b = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Future') & (TH_svoddf[i] == 'Live')]['duration'].sum()
    c = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Current') & (TH_svoddf[i] == 'Not Live')]['duration'].sum()
    d = TH_svoddf[(TH_svoddf['TH_TimePeriod'] == 'Future') & (TH_svoddf[i] == 'Not Live')]['duration'].sum()
    e = TH_svoddf[(TH_svoddf['TH_Expiring'] == 'Expiring') & (TH_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Current') & (TH_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Future') & (TH_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Current') & (TH_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = TH_tvoddf[(TH_tvoddf['TH_TimePeriod'] == 'Future') & (TH_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = TH_tvoddf[(TH_tvoddf['TH_Expiring'] == 'Expiring') & (TH_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    thai_svod_emp_list.append(total)
    thai_tvod_emp_list.append(total2)

### PH HOURS

ph_sub_dub_list = ['ENG_SUB']
ph_svod_emp_list = []
ph_tvod_emp_list = []

for i in ph_sub_dub_list:
    a = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Current') & (PH_svoddf[i] == 'Live')]['duration'].sum()
    b = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Future') & (PH_svoddf[i] == 'Live')]['duration'].sum()
    c = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Current') & (PH_svoddf[i] == 'Not Live')]['duration'].sum()
    d = PH_svoddf[(PH_svoddf['PH_TimePeriod'] == 'Future') & (PH_svoddf[i] == 'Not Live')]['duration'].sum()
    e = PH_svoddf[(PH_svoddf['PH_Expiring'] == 'Expiring') & (PH_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Current') & (PH_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Future') & (PH_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Current') & (PH_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = PH_tvoddf[(PH_tvoddf['PH_TimePeriod'] == 'Future') & (PH_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = PH_tvoddf[(PH_tvoddf['PH_Expiring'] == 'Expiring') & (PH_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    ph_svod_emp_list.append(total)
    ph_tvod_emp_list.append(total2)

### SG HOURS

sg_sub_dub_list = ['ENG_SUB', 'MAN_DUB']
sg_svod_emp_list = []
sg_tvod_emp_list = []

for i in sg_sub_dub_list:
    a = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Current') & (SG_svoddf[i] == 'Live')]['duration'].sum()
    b = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Future') & (SG_svoddf[i] == 'Live')]['duration'].sum()
    c = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Current') & (SG_svoddf[i] == 'Not Live')]['duration'].sum()
    d = SG_svoddf[(SG_svoddf['SG_TimePeriod'] == 'Future') & (SG_svoddf[i] == 'Not Live')]['duration'].sum()
    e = SG_svoddf[(SG_svoddf['SG_Expiring'] == 'Expiring') & (SG_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Current') & (SG_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Future') & (SG_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Current') & (SG_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = SG_tvoddf[(SG_tvoddf['SG_TimePeriod'] == 'Future') & (SG_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = SG_tvoddf[(SG_tvoddf['SG_Expiring'] == 'Expiring') & (SG_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    sg_svod_emp_list.append(total)
    sg_tvod_emp_list.append(total2)

### IN HOURS

in_sub_dub_list = ['ENG_SUB', 'HIN_SUB', 'TAM_SUB', 'TEL_SUB', 'HIN_DUB', 'TAM_DUB', 'TEL_DUB']
in_svod_emp_list = []
in_tvod_emp_list = []

for i in in_sub_dub_list:
    a = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Current') & (IN_svoddf[i] == 'Live')]['duration'].sum()
    b = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Future') & (IN_svoddf[i] == 'Live')]['duration'].sum()
    c = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Current') & (IN_svoddf[i] == 'Not Live')]['duration'].sum()
    d = IN_svoddf[(IN_svoddf['IN_TimePeriod'] == 'Future') & (IN_svoddf[i] == 'Not Live')]['duration'].sum()
    e = IN_svoddf[(IN_svoddf['IN_Expiring'] == 'Expiring') & (IN_svoddf[i] == 'Not Live')]['duration'].sum()
    
    a2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Current') & (IN_tvoddf[i] == 'Live')]['duration'].sum()
    b2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Future') & (IN_tvoddf[i] == 'Live')]['duration'].sum()
    c2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Current') & (IN_tvoddf[i] == 'Not Live')]['duration'].sum()
    d2 = IN_tvoddf[(IN_tvoddf['IN_TimePeriod'] == 'Future') & (IN_tvoddf[i] == 'Not Live')]['duration'].sum()
    e2 = IN_tvoddf[(IN_tvoddf['IN_Expiring'] == 'Expiring') & (IN_tvoddf[i] == 'Not Live')]['duration'].sum()
    
    total = [a, b, c, d, e]
    total2 = [a2, b2, c2, d2, e2]
    
    in_svod_emp_list.append(total)
    in_tvod_emp_list.append(total2)



def pie1(): 
    labels = ['ID SVOD', 'TH SVOD', 'PH_SVOD', 'SG_SVOD', 'IN_SVOD']
    values = svod_td
    colors = ['#822B24', '#1B4F6A', '#36614F', '#A94B35', '#571F4E']

    trace = go.Pie(labels=labels, values=values,
                   hoverinfo='label+value', textinfo='label+percent', 
                   textfont=dict(size=14),
                   marker=dict(colors=colors, 
                               line=dict(color='#000000', width=2)))

    return py.plot([trace], filename='styled_pie_chart')

def pie2(): 
    labels = ['ID TVOD', 'TH TVOD', 'PH_TVOD', 'SG_TVOD', 'IN_TVOD']
    values = tvod_td
    colors = ['#822B24', '#1B4F6A', '#36614F', '#A94B35', '#571F4E']

    trace = go.Pie(labels=labels, values=values,
                   hoverinfo='label+value', textinfo='label+percent', 
                   textfont=dict(size=14),
                   marker=dict(colors=colors, 
                               line=dict(color='#000000', width=2)))

    return py.iplot([trace], filename='styled_pie_chart')

xaxis = ['Current Live', 'Future Live', 'Current Not Live', 'Future Not Live', 'Expiring']
colorset = ['#177a47', '#571017', '#7516b5', '#520f80', '#e8e466', 
                    '#d18e21', '#2833d1', '#1c2494', '#4e56bf', '#2e3370']

def svodbar1():

    trace1 = go.Bar(
        x=xaxis,
        y=indo_svod_emp_list[0],
        marker=dict(color=colorset[0]),
        name='ID ENG SUB'
    )

    trace2 = go.Bar(
        x=xaxis,
        y=indo_svod_emp_list[1],
        marker=dict(color=colorset[1]),
        name='ID BH SUB'
    )

    trace3 = go.Bar(
        x=xaxis,
        y=thai_svod_emp_list[0],
        marker=dict(color=colorset[2]),
        name='TH ENG SUB'
    )
    
    trace4 = go.Bar(
        x=xaxis,
        y=thai_svod_emp_list[1],
        marker=dict(color=colorset[3]),
        name='TH TH SUB'
    )   
    
    trace5 = go.Bar(
        x=xaxis,
        y=ph_svod_emp_list[0],
        marker=dict(color=colorset[4]),
        name='PH ENG SUB'
    )      
        
    trace6 = go.Bar(
        x=xaxis,
        y=sg_svod_emp_list[0],
        marker=dict(color=colorset[5]),
        name='SG ENG SUB'
    )
    
    trace7 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[0],
        marker=dict(color=colorset[6]),
        name='IN ENG SUB'
    )  
    
    trace8 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[1],
        marker=dict(color=colorset[7]),
        name='IN HIN SUB'
    )  
    
    trace9 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[2],
        marker=dict(color=colorset[8]),
        name='IN TAM SUB'
    )  
    
    trace10 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[3],
        marker=dict(color=colorset[9]),
        name='IN TEL SUB'
    )  
        
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename='svod-stacked-bar')

def tvodbar1():

    trace1 = go.Bar(
        x=xaxis,
        y=indo_tvod_emp_list[0],
        marker=dict(color=colorset[0]),
        name='ID ENG SUB'
    )

    trace2 = go.Bar(
        x=xaxis,
        y=indo_tvod_emp_list[1],
        marker=dict(color=colorset[1]),
        name='ID BH SUB'
    )

    trace3 = go.Bar(
        x=xaxis,
        y=thai_tvod_emp_list[0],
        marker=dict(color=colorset[2]),
        name='TH ENG SUB'
    )
    
    trace4 = go.Bar(
        x=xaxis,
        y=thai_tvod_emp_list[1],
        marker=dict(color=colorset[3]),
        name='TH TH SUB'
    )   
    
    trace5 = go.Bar(
        x=xaxis,
        y=ph_tvod_emp_list[0],
        marker=dict(color=colorset[4]),
        name='PH ENG SUB'
    )      
        
    trace6 = go.Bar(
        x=xaxis,
        y=sg_tvod_emp_list[0],
        marker=dict(color=colorset[5]),
        name='SG ENG SUB'
    )
    
    trace7 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[0],
        marker=dict(color=colorset[6]),
        name='IN ENG SUB'
    )  
    
    trace8 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[1],
        marker=dict(color=colorset[7]),
        name='IN HIN SUB'
    )  
    
    trace9 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[2],
        marker=dict(color=colorset[8]),
        name='IN TAM SUB'
    )  
    
    trace10 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[3],
        marker=dict(color=colorset[9]),
        name='IN TEL SUB'
    )  
        
    data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename='tvod-stacked-bar')

def svodbar2():

    trace1 = go.Bar(
        x=xaxis,
        y=indo_svod_emp_list[2],
        marker=dict(color=colorset[0]),
        name='ID BH DUB'
    )

    trace2 = go.Bar(
        x=xaxis,
        y=thai_svod_emp_list[2],
        marker=dict(color=colorset[1]),
        name='TH TH DUB'
    )

    trace3 = go.Bar(
        x=xaxis,
        y=sg_svod_emp_list[1],
        marker=dict(color=colorset[2]),
        name='SG MAN DUB'
    )
    
    trace4 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[4],
        marker=dict(color=colorset[3]),
        name='IN HIN DUB'
    )   
    
    trace5 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[5],
        marker=dict(color=colorset[4]),
        name='IN TAM DUB'
    )      
        
    trace6 = go.Bar(
        x=xaxis,
        y=in_svod_emp_list[6],
        marker=dict(color=colorset[5]),
        name='IN TEL DUB'
    )
        
    data = [trace1, trace2, trace3, trace4, trace5, trace6]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename='svod-stacked-bar2')

def tvodbar2():

    trace1 = go.Bar(
        x=xaxis,
        y=indo_tvod_emp_list[2],
        marker=dict(color=colorset[0]),
        name='ID BH DUB'
    )

    trace2 = go.Bar(
        x=xaxis,
        y=thai_tvod_emp_list[2],
        marker=dict(color=colorset[1]),
        name='TH TH DUB'
    )

    trace3 = go.Bar(
        x=xaxis,
        y=sg_tvod_emp_list[1],
        marker=dict(color=colorset[2]),
        name='SG MAN DUB'
    )
    
    trace4 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[4],
        marker=dict(color=colorset[3]),
        name='IN HIN DUB'
    )   
    
    trace5 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[5],
        marker=dict(color=colorset[4]),
        name='IN TAM DUB'
    )      
        
    trace6 = go.Bar(
        x=xaxis,
        y=in_tvod_emp_list[6],
        marker=dict(color=colorset[5]),
        name='IN TEL DUB'
    )
        
    data = [trace1, trace2, trace3, trace4, trace5, trace6]
    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    return py.iplot(fig, filename='tvod-stacked-bar2')

