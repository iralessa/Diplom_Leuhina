import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from data_loader import load_data

def plot_seaborn():
    # Загрузка данных
    df = load_data()

    # Проверка, что данные загружены корректно
    if df.empty:
        print("DataFrame пуст. Проверьте источник данных.")
        return
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
    sns.lineplot(x='TRADEDATE', y='CLOSE', data=df, label='Цена закрытия', color='blue')
    sns.lineplot(x='TRADEDATE', y='MA5', data=df, label='MA 5 дней', color='orange', linestyle='--')
    sns.lineplot(x='TRADEDATE', y='MA10', data=df, label='MA 10 дней', color='green', linestyle=':')

    # Настройки графика
    plt.title('Скользящие средние - Seaborn')
    plt.xlabel('Дата')
    plt.ylabel('Цена (RUB)')
    plt.legend()
    plt.grid(True)

    # Отображение графика
    plt.show()

