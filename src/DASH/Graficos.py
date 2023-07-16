import io
import base64
import pandas as pd
import seaborn as sea
import plotly.express as px
import plotly.graph_objects as go
import matplotlib
import matplotlib.pyplot    as plt

matplotlib.use('agg')


def PlotSetorAno(data:pd.DataFrame , Ano:int):

    # fig = go.Figure()
    # fig.add_trace(
    #     go.Bar(
    #         x    = data['valor_de_mercado_mi'].values,
    #         y    = data['setor'].values,    
    #         text = data['valor_de_mercado_mi'].values, 
    #         orientation = 'h',
    #         width = 1
    #     )
    # )

    # fig.update_layout(
    #     height    = 750 ,
    #     hovermode = "x unified",

    #     )
    fig = plt.figure(figsize=(14, 5))
    plt.bar(x=[1,2,3,4],height=[10,10,10,10])
    # Save it to a temporary buffer.
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    fig_bar_matplotlib = f'data:image/png;base64,{fig_data}'

    # Build the Plotly figure


    return fig_bar_matplotlib