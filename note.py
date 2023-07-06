class Note:
    text:str
    password:str
    author:str
    encrypted_status: bool


    def __init__(self, message):
        self.text = message
        self.encrypted_status = False
        self.author = "Daniel"

    def __str__(self):
        return "{} - {}".format(self.text, self.author)
