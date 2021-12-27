def isString(text):
    if isinstance(text, str):
        return True
    else:
        raise TypeError("Argument musi być typu string")


class Subscriber:

    def __init__(self):
        self.clients = []

    def add_client(self, firstname, lastname):
        if isString(firstname) and isString(lastname):
            self.clients.append({'firstname': firstname, 'lastname': lastname})
            return {'firstname': firstname, 'lastname': lastname}

    def delete_client(self, client_id):
        if isinstance(client_id, int):
            if 0 < client_id < len(self.clients):
                self.clients.pop(client_id)
                return client_id
            else:
                raise ValueError('Nie ma takiego klienta')
        else:
            raise TypeError('Argument musi być typu int')

    def send_message(self,text,client_id):
        if isString(text):
            if isinstance(client_id, int):
                if 0 < client_id < len(self.clients):
                    return f"Wysłano wiadomość do {client_id}"
                else:
                    raise ValueError('Nie ma takiego klienta')
            else:
                raise TypeError('Argument musi być typu int')
