import rsa
import psycopg2

import note
import encrypter
public_key, private_key = rsa.newkeys(512)

body = "This is a test text to be encrypted."

conn = psycopg2.connect(database="postgres",
                        host="localhost",
                        user='postgres',
                        password='your_password',
                        port='5432')

def list_notes():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes;")
    print(cursor.fetchall())

def save_note(n:note.Note):
    cursor = conn.cursor()
    cursor.execute("INSERT into notes (body, author) VALUES (%s, %s)", (n.text, n.author))
    conn.commit()


def close_db():
    conn.close()


def main():
    print("Creating a new note")
    new_note = note.Note(body)
    five_encrypter = encrypter.Encrypter()
    new_note.text = five_encrypter.encrypt(new_note.text)
    save_note(new_note)
    list_notes()

main()
close_db()
