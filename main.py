from visualize_plotly import plot_plotly
import webbrowser
from visualize_matplotlib import plot_matplotlib
from visualize_seaborn import plot_seaborn
from data_loader import load_data

df = load_data()

def main():
    print("Выберите способ визуализации:")
    print("1. Matplotlib")
    print("2. Seaborn")
    print("3. Plotly (откроется Jupyter Notebook)")
    choice = input("Введите номер (1/2/3): ")

    if choice == '1':
        plot_matplotlib()
    elif choice == '2':
        plot_seaborn()
    elif choice == '3':
        # Открытие Jupyter Notebook с графиком Plotly
        # Запустить в терминале команду jupyter notebook

        notebook_url = "http://127.0.0.1:8888/notebooks/visualize_plotly.ipynb"
        print(f"Открытие Jupyter Notebook по адресу: {notebook_url}")
        webbrowser.open(notebook_url)
    else:
        print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
