from dao.__init__ import *

class ViagemRepository:
    def __init__(self):
        self.viagemDao = ViagemDao()

    def getAllViagens(self):
        return self.viagemDao.getAllViagens()

    def getViagem(self, id):
        return self.viagemDao.getViagem(id)

    def createViagem(self, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_disponiveis):
        return self.viagemDao.addViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_disponiveis)

    def updateViagem(self, id, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_disponiveis):
        return self.viagemDao.attViagem(id, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_disponiveis)

    def deleteViagem(self, id):
        return self.viagemDao.delViagem(id)
