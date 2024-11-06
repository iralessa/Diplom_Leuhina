import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data  # Импортируем функцию load_data из файла data_loader.py

def plot_matplotlib():
    # Загрузка данных
    df = load_data()
    """
    1. Загружает данные о торгах с использованием функции load_data.
    2. Проверяет, что данные успешно загружены, и сообщает об ошибке, если DataFrame пуст.
    3. Добавляет скользящие средние на 5 и 10 дней в столбцы 'MA5' и 'MA10', если столбец 'CLOSE' присутствует в данных.
    4. Проверяет, что все необходимые столбцы ('TRADEDATE', 'CLOSE', 'MA5', 'MA10') присутствуют в данных.
    5. Строит график, отображая цену закрытия и скользящие средние на 5 и 10 дней.
    """
    # Проверка, что данные загружены корректно
    if df.empty:
        print("DataFrame пуст. Проверьте источник данных.")
        return  # Завершение функции, если данные не загружены
    else:
        print("DataFrame успешно загружен.")

    # Добавление скользящих средних в DataFrame, если их нет
    if 'CLOSE' in df.columns:
        df['MA5'] = df['CLOSE'].rolling(window=5).mean()
        df['MA10'] = df['CLOSE'].rolling(window=10).mean()
    else:
        print("Столбец 'CLOSE' отсутствует. Проверьте данные.")
        return

    # Проверка наличия необходимых столбцов после добавления
    required_columns = {'TRADEDATE', 'CLOSE', 'MA5', 'MA10'}
    if not required_columns.issubset(df.columns):
        print("Некоторые столбцы отсутствуют в данных даже после добавления MA5 и MA10.")
        return

    # Построение графика скользящих средних
    plt.figure(figsize=(14, 7))
    plt.plot(df['TRADEDATE'], df['CLOSE'], label='Цена закрытия', color='blue')
    plt.plot(df['TRADEDATE'], df['MA5'], label='MA 5 дней', color='orange', linestyle='--')
    plt.plot(df['TRADEDATE'], df['MA10'], label='MA 10 дней', color='green', linestyle=':')

    # Настройки графика
    plt.title('Скользящие средние - Matplotlib')
    plt.xlabel('Дата')
    plt.ylabel('Цена (RUB)')
    plt.legend()
    plt.grid(True)

    # Отображение графика
    plt.show()
