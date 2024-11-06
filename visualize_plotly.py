import plotly.graph_objs as go
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.io as pio

# Устанавливаем рендер, чтобы график открывался в браузере
pio.renderers.default = 'notebook'

# Функция для построения графика с MA5 и MA10
def plot_plotly(df):
    """
    Строит график с использованием Plotly для отображения цены закрытия и скользящих средних MA5 и MA10.

    1. Проверяет, что данные DataFrame не пусты. Если данные пусты, выводится сообщение об ошибке.
    2. Создает график, добавляя:
       - Линию для цены закрытия (столбец 'CLOSE').
       - Линии для скользящих средних MA5 и MA10.
    3. Настроивает внешний вид графика:
       - Заголовок графика.
       - Подписи для осей X и Y.
       - Использует шаблон 'plotly_white' для оформления графика.
    """
    # Проверка, что данные не пустые
    if df.empty:
        print("DataFrame пуст. Проверьте источник данных.")
        return

    # Создание подграфика
    fig = make_subplots()

    # Линия цены закрытия
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['CLOSE'], mode='lines', name='Цена закрытия', line=dict(color='blue')))

    # Линии для MA5 и MA10
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['MA5'], mode='lines', name='MA 5 дней', line=dict(color='orange', dash='dash')))
    fig.add_trace(go.Scatter(x=df['TRADEDATE'], y=df['MA10'], mode='lines', name='MA 10 дней', line=dict(color='green', dash='dot')))

    # Настройки графика
    fig.update_layout(
        title='Скользящие средние plotly',
        xaxis_title='Дата',
        yaxis_title='Цена (RUB)',
        template='plotly_white'
    )

    # Отображение графика
    fig.show()