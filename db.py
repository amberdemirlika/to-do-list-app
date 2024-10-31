import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS tasks;
        """
    )
    conn.execute(
        """
        CREATE TABLE tasks (
          id INTEGER PRIMARY KEY NOT NULL,
          category TEXT,
          date TEXT,
          title TEXT,
          description TEXT,
          status TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    tasks_seed_data = [
        ("Personal", "2024-1-11","Grocery Shopping", "Buy groceries for the week", "Pending"),
        ("Exercise", "2024-29-10", "Working Out", "Go to the gym", "Completed" ),
        ("Academic", "2024-30-10", "Exam Review", "Study for Chemistry exam", "Pending"),
        ("Work", "2024-03-11", "Finish Report", "Complete monthly report", "Pending"),
    ]
    conn.executemany(
        """
        INSERT INTO tasks (category, date, title, description, status)
        VALUES (?,?,?,?,?)
        """,
        tasks_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()

def tasks_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM tasks
        """
    ).fetchall()
    return [dict(row) for row in rows]

def tasks_create(category, date, title, description , status):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO tasks (category, date, title, description, status)
        VALUES (?, ?, ?, ?, ?)
        RETURNING *
        """,
        (category, date, title, description , status),
    ).fetchone()
    conn.commit()
    return dict(row)

def tasks_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM tasks
        WHERE id = ?
        """,
        (id,),
    ).fetchone()
    return dict(row)

def tasks_update_by_id(id, category, date, title, description ,status):
    conn = connect_to_db()
    row = conn.execute(
        """
        UPDATE tasks SET category = ?, date = ?, title = ?, description = ?, status =?
        WHERE id = ?
        RETURNING *
        """,
        (category, date, title, description , status, id),
    ).fetchone()
    conn.commit()
    return dict(row)


if __name__ == "__main__":
    initial_setup()