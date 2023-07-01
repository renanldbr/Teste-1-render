from dash import Dash
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template 

import pandas as pd
import numpy as np

import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv(r'assets/supermarket_sales.csv')

##### Botão Linkedin #####  
linkedin_btn = html.A(
    dbc.Button(
        html.Img(src='https://www.svgrepo.com/show/922/linkedin.svg',style={'width': '30px', 'height': '30px'}),
        color='link',
        class_name='mr-2'),
    href='https://www.linkedin.com/in/renanldbr',
    target='_brank'
)

##### Botão Github IO #####  
git_hub_io = html.A(
    dbc.Button(
        html.Img(src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png',style={'width': '30px', 'height': '30px'}),
        color='link',
        class_name='mr-2'),
    href='https://renanldbr.github.io/',
    target='_brank'
)

##### Botão Github #####  
git_hub = html.A(
    dbc.Button(
        html.Img(src='data:image/png;base64,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',style={'width': '30px', 'height': '30px'}),
        color='link',
        class_name='mr-2'),
    href='https://github.com/renanldbr',
    target='_brank'
)

app = Dash(__name__, external_stylesheets=[dbc.themes.ZEPHYR])
server = app.server

load_figure_template('zephyr')

app.layout = html.Div(
    dbc.Row([
        #coluna 1
        dbc.Col([
            dbc.Card([
            html.H1('RLdBr Labs',style={'font-style':'oblique 30deg', 'margin-top':'10px', 'textAlign':'center'}),
            html.Hr(),
            dcc.Checklist(df.City.unique(), df.City.unique(), inline=True, style={'margin-left':'10px'}, inputStyle={'margin-left':'5px', 'margin-right':'10px'}, id='checklist'),
            html.Hr(),
            dcc.RadioItems(['gross income', 'Rating'], 'Rating', inline=True, style={'margin-left':'10px'}, inputStyle={'margin-left':'5px'}, id='radioitems'),
            html.Hr(),
            html.H6('Wanna See More?', style={'textAlign':'center'}),
            dbc.Row([
                dbc.Col(linkedin_btn, lg=3, sm=10),
                dbc.Col(git_hub_io, lg=3, sm=10),
                dbc.Col(git_hub, lg=3, sm=10)
            ], justify='center')
            
            ],
            style={'height':'80vh', 'margin':'10px'})
            ], md=2),
        
        #coluna 2
        dbc.Col([
            dbc.Row([
                dbc.Col(dcc.Graph(id='grafico1'), lg=4, sm=12),
                dbc.Col(dcc.Graph(id='grafico2'), lg=4, sm=12),
                dbc.Col(dcc.Graph(id='grafico3'), lg=4, sm=12)
            ], style={'margin-top':'10px','display':'flex', 'flex-wrap': 'wrap'}),
            dbc.Row([dcc.Graph(style={'height':'35vh', 'margin-left':'15px', 'margin-top':'10px'}, id='grafico4')]),
            dbc.Row([dcc.Graph(style={'height':'35vh', 'margin-left':'15px', 'margin-top':'10px'}, id='grafico5')])
        ], md=9)
    ])

)

@app.callback(
    Output(component_id='grafico1', component_property='figure'),
    Output(component_id='grafico2', component_property='figure'),
    Output(component_id='grafico3', component_property='figure'),
    Output(component_id='grafico4', component_property='figure'),
    Output(component_id='grafico5', component_property='figure'),

    Input(component_id='checklist',component_property='value'),
    Input(component_id='radioitems', component_property='value'))

def funcoes(cidades, v_op):
    #função para os gráficos (v_op == 'gross income' ou v_op == 'Rating')
    operation = np.sum if v_op == 'gross income' else np.mean
    data_refreshed = df[df['City'].isin(cidades)]
    
    #P/ Grafico 1
    df_cities = data_refreshed.groupby('City')[v_op].apply(operation).to_frame().reset_index()

    #P/ Grafico 2
    df_payment = data_refreshed.groupby('Payment')[v_op].apply(operation).to_frame().reset_index()

    #P/ Grafico 3
    df_prod_line = data_refreshed.groupby(['Product line','City'])[v_op].apply(operation).to_frame().reset_index()
    
    #P/ Grafico 4
    df_gender = data_refreshed.groupby(['City','Gender'])[v_op].apply(operation).to_frame().reset_index()

    #P/ Grafico 5
    df_income_time = data_refreshed.groupby(['Date'])[v_op].apply(operation).to_frame().reset_index()

    grafico1 = px.bar(df_cities, x='City', y=v_op, color='City')
    grafico2 = px.bar(df_payment, x=v_op, y='Payment', orientation='h')
    grafico3 = px.bar(df_prod_line, x=v_op, y='Product line', color='City', orientation='h')
    grafico4 = px.bar(df_income_time, x='Date', y=v_op)
    grafico5 = px.bar(df_gender, x='Gender', y=v_op, color='City', barmode='group')
    
    for grafico in [grafico1, grafico2, grafico3, grafico5]:
        grafico.update_layout(template='zephyr')
        grafico.update_layout(margin=dict(l=0, r=20, t=20, b=20), height=200)

    return [grafico1, grafico2, grafico3, grafico4, grafico5]

if __name__=='__main__':
    app.run_server(debug=False)
