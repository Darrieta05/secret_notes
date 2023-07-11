import psycopg2

import note


def setup_db():
    # connecting to postgres database
    try:
        conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user='postgres',
                        password='your_password',
                        port='5432')
        cur = conn.cursor()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error when connecting to DB - ", error)

    return conn, cur


def list_notes():
    conn, cur = setup_db()
    cur.execute("SELECT * FROM notes;")
    print(cur.fetchall())

def save_note(n:note.Note):
    conn, cur = setup_db()
    cur.execute("INSERT into notes (body, author) VALUES (%s, %s)", (n.text, n.author))
    conn.commit()



