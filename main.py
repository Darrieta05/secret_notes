import rsa
import psycopg2

import note
import encrypter
import db_manager
public_key, private_key = rsa.newkeys(512)

body = "This is a test text to be encrypted."


def main():
    print("Creating a new note")
    new_note = note.Note(body)
    five_encrypter = encrypter.Encrypter()
    new_note.text = five_encrypter.encrypt(new_note.text)
    db_manager.save_note(new_note)
    db_manager.list_notes()

db_manager.setup_db()
main()
