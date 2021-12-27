from src.MailServer import MailServer
from src.TemplateEngine import TemplateEngine

def isString(text):
    if isinstance(text,str):
        return True
    else:
        raise TypeError('Argument musi być typu string')

class Messenger:
    def __init__(self):
        self.template = TemplateEngine()
        self.server = MailServer()

    def send_message(self, email, text):
        if isString(email) and isString(text):
            return self.server.send_message(self.template.make_message(email, text))

    def get_message(self, email):
        if isString(email):
            return self.server.get_message(email)
