import io

import base64
import matplotlib                                
import matplotlib.pyplot as plt
import src.DASH.DadosParaDashboard as dados
from   dash import Dash, dcc, html,Output,Input
matplotlib.use('agg')

def Dados(): return dados.Data()
app = Dash()
app.layout = html.Div([
    html.H1(
        children = 'Dashboard Fortunas apartir de 2015'
    ),
    html.Div([
        dcc.Dropdown(
            id      = 'OpcoesDeAnos',
            options = dados.Anos(Dados()),
            value   = '2015',
            style   = {
                    'width':'100px',
                },
            )
    ]),
    html.Div([
        html.Img(
            id='GraphBar'
        )
    ],
        
    )
    
])

@app.callback(
    Output(component_id='GraphBar', component_property='src'),
    [Input('OpcoesDeAnos','value')]
)
def GraficoAnos(values):
    return dados.SetorAno(int(values),Dados())

    
if __name__ =='__main__': app.run_server(debug=True)