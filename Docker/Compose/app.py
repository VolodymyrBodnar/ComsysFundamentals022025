import psycopg2

# Налаштування підключення до PostgreSQL (змінні середовища можна передавати через Docker Compose)
DB_NAME = "mydb"
DB_USER = "user"
DB_PASSWORD = "password"
DB_HOST = "db"
DB_PORT = "5432"

# Підключення до бази даних
try:
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()

    # Створення таблиці
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        );
    """)
    print("Таблиця створена успішно!")

    # Додавання тестових даних
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Іван", 25))
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Марія", 30))

    # Фіксуємо зміни
    conn.commit()
    print("Дані додано успішно!")

    # Виводимо всі записи з таблиці
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Закриваємо підключення
    cur.close()
    conn.close()

except Exception as e:
    print(f"Помилка підключення до бази даних: {e}")
