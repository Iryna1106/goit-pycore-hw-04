import sys
from pathlib import Path
from colorama import init, Fore, Style, Back

# Ініціалізація бібліотеки colorama для підтримки кольорового виведення
init(autoreset=True)

def print_directory_structure(directory, indent=""):
    try:
        # Перевірка, чи шлях є директорією
        if not directory.is_dir():
            print(f"{directory} не є директорією або не існує.")
            return
        
        # Отримуємо всі файли та папки в поточній директорії
        for path in directory.iterdir():
            if path.is_dir():
                # Виводимо папку з іншим кольором
                print(f"{indent}{Fore.BLUE}{path.name}/")
                # Рекурсивно виводимо вміст піддиректорій
                print_directory_structure(path, indent + "    ")
            else:
                # Виводимо файли
                print(f"{indent}{Fore.GREEN}{path.name}")
    
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    # Перевіряємо, чи було передано аргумент командного рядка
    if len(sys.argv) != 2:
        print("Використання: python script.py <шлях до директорії>")
        sys.exit(1)
    
    # Отримуємо шлях до директорії з аргументів командного рядка
    directory_path = Path(sys.argv[1])

    # Викликаємо функцію для відображення структури директорії
    print_directory_structure(directory_path)
