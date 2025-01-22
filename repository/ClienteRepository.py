from dao.__init__ import *

class ClienteRepository:
    def __init__(self):
        self.clienteDao = ClienteDao()

    def getAllClientes(self):
        return self.clienteDao.getAllClientes()

    def getCliente(self, id):
        return self.clienteDao.getCliente(id)

    def createCliente(self, nome, email, nascimento, rg, telefone):
        return self.clienteDao.addCliente(nome, email, nascimento, rg, telefone)

    def updateCliente(self, id, nome, email, nascimento, rg, telefone):
        return self.clienteDao.attCliente(id, nome, email, nascimento, rg, telefone)

    def deleteCliente(self, id):
        return self.clienteDao.delCliente(id)