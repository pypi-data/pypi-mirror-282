import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display_author_info():
    print("Made by Avinion\nTelegram: @akrim\n")

def get_language():
    while True:
        lang = input("Choose language (E/R) / Выберите язык (E/R): ").strip().lower()
        if lang in ['e', 'r']:
            return lang
        else:
            print("Invalid choice. Please enter E or R / Неверный выбор. Пожалуйста, введите E или R.")

def get_text(lang):
    if lang == 'e':
        return input("Please enter the text to convert: ")
    else:
        return input("Пожалуйста, введите текст для конвертации: ")

def get_conversion_option(lang):
    options = {
        'e': [
            "1: UPPERCASE",
            "2: lowercase",
            "3: Title Case",
            "4: Capitalize Each Word",
            "5: Toggle Case",
            "6: Staircase Case",
            "7: Sentence Case"
        ],
        'r': [
            "1: БОЛЬШИЕ БУКВЫ",
            "2: маленькие буквы",
            "3: Заглавные Слова",
            "4: Каждое Слово С Большой Буквы",
            "5: Переключение Регистр",
            "6: Лестничный Регистр",
            "7: В виде предложения"
        ]
    }
    
    for option in options[lang]:
        print(option)
    
    if lang == 'e':
        prompt = "Choose an option: "
    else:
        prompt = "Выберите вариант: "
        
    while True:
        choice = input(prompt).strip()
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            return int(choice)
        else:
            if lang == 'e':
                print("Invalid choice. Please enter a number between 1 and 7.")
            else:
                print("Неверный выбор. Пожалуйста, введите число от 1 до 7.")

def convert_text(text, option):
    if option == 1:
        return text.upper()
    elif option == 2:
        return text.lower()
    elif option == 3:
        return text.title()
    elif option == 4:
        return ' '.join(word.capitalize() for word in text.split())
    elif option == 5:
        return ''.join([char.lower() if char.isupper() else char.upper() for char in text])
    elif option == 6:
        return ''.join(char.upper() if i % 2 == 0 else char.lower() for i, char in enumerate(text))
    elif option == 7:
        return text.capitalize()

def main():
    display_author_info()
    lang = get_language()
    
    while True:
        text = get_text(lang)
        option = get_conversion_option(lang)
        converted_text = convert_text(text, option)
        print(f"\n{converted_text}\n")
        
        if lang == 'e':
            cont = input("Continue? (Y/N): ").strip().lower()
        else:
            cont = input("Продолжить? (Y/N): ").strip().lower()
        
        if cont == 'n':
            break
        clear_console()
        display_author_info()

if __name__ == "__main__":
    main()
