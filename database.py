import sqlite3


DATABASE_NAME = "bmi_history.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bmi_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            bmi REAL NOT NULL,
            category TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_record(name, weight, height, bmi, category):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bmi_records
        (name, weight, height, bmi, category)
        VALUES (?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category))

    connection.commit()
    connection.close()


def get_records(name):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT weight, height, bmi, category, date
        FROM bmi_records
        WHERE name = ?
        ORDER BY date
    """, (name,))

    records = cursor.fetchall()

    connection.close()

    return records


if __name__ == "__main__":
    create_database()
    print("Database created successfully.")