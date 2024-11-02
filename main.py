from lesson_7 import create_table, add_book, find_book_by_title, update_book_year, delete_book_by_title, close_connection


def main():          # Основное меню программы
    create_table()  
    while True:           # Создаём таблицу при запуске программы
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Искать книгу по названию")
        print("3. Обновить год издания книги")
        print("4. Удалить книгу по названию")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания книги: "))
            add_book(title, author, year)

        elif choice == '2':
            title = input("Введите название книги для поиска: ")
            find_book_by_title(title)

        elif choice == '3':
            title = input("Введите название книги для обновления: ")
            new_year = int(input("Введите новый год издания: "))
            update_book_year(title, new_year)

        elif choice == '4':
            title = input("Введите название книги для удаления: ")
            delete_book_by_title(title)

        elif choice == '5':
            print("Выход из программы.")
            close_connection()
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
