import sqlite3

conn = sqlite3.connect("library.db")  # Подключение к базе данных и создание таблицы
cursor = conn.cursor()

def create_table():    # Функция для создания таблицы books
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        year INTEGER NOT NULL
                    )''')
    conn.commit()

def add_book(title, author, year):   # Функция для добавления книги
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    print(f"Книга '{title}' добавлена.")

def find_book_by_title(title):    # Функция для поиска книги по названию
    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))
    book = cursor.fetchone()
    if book:
        print(f"Найдена книга: ID: {book[0]}, Название: {book[1]}, Автор: {book[2]}, Год издания: {book[3]}")
    else:
        print("Книга не найдена.")

def update_book_year(title, new_year):    # Функция для обновления года издания книги по названию
    cursor.execute("UPDATE books SET year = ? WHERE title = ?", (new_year, title))
    conn.commit()
    print(f"Год издания книги '{title}' обновлен до {new_year}.")

def delete_book_by_title(title):      # Функция для удаления книги по названию
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    conn.commit()
    print(f"Книга '{title}' удалена.")

def close_connection():   # Закрытие соединения с базой данных
    conn.close()
