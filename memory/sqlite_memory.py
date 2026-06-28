import sqlite3

conn = sqlite3.connect("memory.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT,
    query TEXT,
    response TEXT
)
""")

conn.commit()


def save_conversation(customer_name, query, response):

    cursor.execute(
        """
        INSERT INTO conversations(customer_name,query,response)
        VALUES(?,?,?)
        """,
        (customer_name, query, response)
    )

    conn.commit()


def get_previous_issue(customer_name):

    cursor.execute(
        """
        SELECT query
        FROM conversations
        WHERE customer_name=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (customer_name,)
    )

    result = cursor.fetchone()

    if result:
        return result[0]

    return "No previous issue found."