import requests
import pandas as pd


def load_data():
    url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/SBER.json?from=2023-01-01'
    response = requests.get(url)
    data = response.json()

    # Парсим данные из JSON и создаем DataFrame
    rows = data['history']['data']
    columns = data['history']['columns']
    df = pd.DataFrame(rows, columns=columns)

    # Преобразуем даты и добавляем вычисления для анализа
    df['TRADEDATE'] = pd.to_datetime(df['TRADEDATE'])
    df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')
    df['returns'] = df['CLOSE'].pct_change()
    df['MA20'] = df['CLOSE'].rolling(window=20).mean()
    df['MA50'] = df['CLOSE'].rolling(window=50).mean()

    return df