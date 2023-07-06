import rsa

import note
import encrypter
public_key, private_key = rsa.newkeys(512)

body = "This is a test text to be encrypted."


def main():
    print("Creating a new note")
    new_note = note.Note(body)
    print(new_note)
    print(encrypter.Encrypter.encrypt(new_note.text))

main()

