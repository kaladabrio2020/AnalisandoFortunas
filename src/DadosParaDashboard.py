import pandas as pd
import plotly.express as px

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


