import pandas as pd
import plotly.graph_objs as go
from data_loader import load_data
import plotly.io as pio


def plot_plotly():
    # Загрузка данных
    df = load_data()
    if df.empty or 'CLOSE' not in df.columns:
        print("Ошибка загрузки данных: DataFrame пуст или отсутствует столбец 'CLOSE'.")
        return

    # Вычисление скользящих средних
    df['MA5'] = df['CLOSE'].rolling(window=5).mean()
    df['MA10'] = df['CLOSE'].rolling(window=10).mean()

    # Построение графика
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=df['TRADEDATE'], y=df['CLOSE'], mode='lines', name='Цена закрытия', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['MA5'], mode='lines', name='MA 5 дней',
                             line=dict(color='orange', dash='dash')))
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['MA10'], mode='lines', name='MA 10 дней',
                             line=dict(color='green', dash='dot')))

    # Настройки макета
    fig.update_layout(
        title='Скользящие средние - Plotly',
        xaxis_title='Дата',
        yaxis_title='Цена (RUB)',
        template='plotly_white'
    )

    # Сохранение графика в HTML файл
    fig.write_html('plotly_graph.html')


# Запуск функции
plot_plotly()