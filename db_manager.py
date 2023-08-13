import sqlite3

import note

db_file = "notes.db"

notes_sql = """ CREATE TABLE IF NOT EXISTS notes (
                id integer PRIMARY KEY,
                body text,
                author text
                ); """


def db_connection():
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except(Exception, sqlite3.Error) as error:
        print("Error when connecting to DB - ", error)

def setup_db():
    # connecting to postgres database
    try:
        conn = db_connection() 
        create_table_if_not_exist(conn, notes_sql)
        # create all tables if they don't exist already

    except (Exception, sqlite3.Error) as error:
        print("Error when setting up DB - ", error)

    return "Database setup successful "

def create_table_if_not_exist(conn:sqlite3.Connection, create_table_sql):
    # Create a table in the database if it doesn't exist already
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except(Exception, sqlite3.DatabaseError) as error:
        print("Encountered error when creating a table - " , error)


def list_notes():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM notes;")
    print(cur.fetchall())

def save_note(n:note.Note):
    insert_note_sql = """INSERT into notes (body, author)
                        VALUES (?, ?);"""
    cur = db_connection()
    cur.execute(insert_note_sql, (n.text, n.author))
    cur.commit()

def update_note(n_id:int, body):
    update_sql = """UPDATE notes
                    SET body = ?
                    WHERE id = ?;"""
    cur = db_connection()
    cur.execute(update_sql, body, n_id)
    cur.commit()

def get_note(id:int):
    select_one_note_sql = """SELECT * from notes
                            WHERE id == ?"""
    conn = db_connection()
    cur = conn.cursor()
    cur.execute(select_one_note_sql, id)
    return cur.fetchone()