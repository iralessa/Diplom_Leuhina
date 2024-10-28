import requests
import pandas as pd

def load_data():
    # Задаем URL для загрузки данных с сервера Московской биржи
    url = 'https://iss.moex.com/iss/history/engines/stock/markets/shares/boards/TQBR/securities/SBER.json?from=2024-01-01'

    try:
        # Получаем данные по API
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешность запроса
        data = response.json()

        # Проверяем наличие данных и заголовков
        if 'history' in data and 'data' in data['history'] and 'columns' in data['history']:
            rows = data['history']['data']
            columns = data['history']['columns']
            df = pd.DataFrame(rows, columns=columns)
        else:
            print("Данные отсутствуют в ответе сервера.")
            return pd.DataFrame()  # Возвращаем пустой DataFrame при отсутствии данных

        # Преобразуем столбцы к нужным типам
        df['TRADEDATE'] = pd.to_datetime(df['TRADEDATE'], errors='coerce')
        df['CLOSE'] = pd.to_numeric(df['CLOSE'], errors='coerce')

        # Фильтрация для удаления строк с отсутствующими данными
        df = df.dropna(subset=['TRADEDATE', 'CLOSE'])

        # Добавляем расчетные столбцы для анализа
        df['returns'] = df['CLOSE'].pct_change()  # Дневная доходность
        df['MA5'] = df['CLOSE'].rolling(window=5).mean()  # Скользящее среднее на 5 дней
        df['MA10'] = df['CLOSE'].rolling(window=10).mean()  # Скользящее среднее на 10 дней

        return df

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе данных: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame в случае ошибки подключения