import matplotlib.pyplot as plt
from data_loader import load_data

df = load_data()

def plot_matplotlib():
    # Скользящие средние
    plt.figure(figsize=(10, 6))
    plt.plot(df['TRADEDATE'], df['CLOSE'], label='Цена закрытия', color='blue')
    plt.plot(df['TRADEDATE'], df['MA20'], label='MA 20 дней', linestyle='--', color='orange')
    plt.plot(df['TRADEDATE'], df['MA50'], label='MA 50 дней', linestyle='-.', color='green')
    plt.title('Скользящие средние - Matplotlib')
    plt.xlabel('Дата')
    plt.ylabel('Цена (RUB)')
    plt.legend()
    plt.show()

    # Гистограмма доходностей
    plt.figure(figsize=(10, 6))
    plt.hist(df['returns'].dropna(), bins=50, color='skyblue', edgecolor='black')
    plt.title('Распределение доходностей - Matplotlib')
    plt.xlabel('Доходность')
    plt.ylabel('Частота')
    plt.show()