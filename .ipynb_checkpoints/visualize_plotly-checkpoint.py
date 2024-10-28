import plotly.graph_objects as go
import plotly.express as px
from data_loader import load_data

df = load_data()

def plot_plotly():
    # Скользящие средние
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['CLOSE'], mode='lines', name='Цена закрытия', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['MA20'], mode='lines', name='MA 20 дней', line=dict(color='orange', dash='dash')))
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['MA50'], mode='lines', name='MA 50 дней', line=dict(color='green', dash='dot')))
    fig.update_layout(title='Скользящие средние - Plotly', xaxis_title='Дата', yaxis_title='Цена (RUB)')
    fig.show()

    # Гистограмма доходностей
    fig = px.histogram(df, x='returns', nbins=50, title='Распределение доходностей - Plotly')
    fig.show()