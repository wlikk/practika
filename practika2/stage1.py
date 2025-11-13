import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--package", type=str, required=True, help="Имя анализируемого пакета")
    parser.add_argument("-s", "--source", type=str, required=True, help="URL репозитория или путь к файлу")
    parser.add_argument("-t", "--test-mode", type=int, default=0, choices=[0, 1], help="Режим тестового репозитория (0/1)")
    parser.add_argument("-f", "--filter", type=str, default="", help="Подстрока для фильтрации пакетов")
    
    args = parser.parse_args()
    
    print("Параметры:")
    for key, value in vars(args).items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()
