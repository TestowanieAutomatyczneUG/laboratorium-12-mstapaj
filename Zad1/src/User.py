import requests

class User:

    def getData(self):
        data=requests.get('https://randomuser.me/api/')
        return data.text

    def getName(self):
        pass

    def getLocation(self):
        pass

    def getContact(self):
        pass

