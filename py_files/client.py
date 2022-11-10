
class Client:
    def __init__(self, name='', password='', age=0, document=''):
        self.__name = name
        self.__password = password
        self.__age = age
        self.__document = document
        self.__clients = []

    @property
    def name(self):
        return self.__name

    @property
    def password(self):
        return self.__password

    @property
    def age(self):
        return self.__age

    @property
    def document(self):
        return self.__document

    @property
    def clients(self):
        return self.__clients

    @name.setter
    def name(self, name):
        self.__name = name

    @password.setter
    def password(self, password):
        self.__password = password

    @age.setter
    def age(self, age):
        self.__age = age

    @document.setter
    def document(self, document):
        self.__document = document

    @clients.setter
    def clients(self, clients):
        self.__clients = clients

    def add_client(self, name, password, age, document):
        self.name = name
        self.password = password
        self.age = age
        self.document = document
        client = Client(name, password, age, document)
        self.clients.append(client)

    def client_list(self):
        for client in self.clients:
            print(f'Nome: {client.name}\nIdade: {client.age}\nDocumento: {client.document}')