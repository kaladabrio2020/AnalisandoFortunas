from . import Graficos as gr
import pandas as pd

columns = [
    'nome', 'rank','ano', 'industria','setor',
    'sede_estado','sede_cidade','valor_de_mercado_mi', 'receite_mil',
    'lucro_mil', 'ativos_mil', 'funcionários','fundador_is_ceo','ceo_feminino','recém-chegado à Fortune 500','global_500'
]

def Data():
    data         = pd.read_csv(r'dataset/Fortune 500 Companies.csv',delimiter=',')
    data.columns = columns
    data.drop(columns = 'global_500',inplace=True)
    return data.loc[data['ano'] >= 2015]


def Anos(data:pd.DataFrame):
    lista = (data['ano'].value_counts().index).to_list()
    return lista

def SetorAno(Ano:int,data:pd.DataFrame):
    data = data.loc[data['ano'] == Ano]
    data = data.groupby(by='setor')['valor_de_mercado_mi'].sum()
    
    fig  = gr.PlotSetorAno(data.reset_index(),Ano)
    return fig
