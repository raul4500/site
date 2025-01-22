from models.__init__ import *

# classe dos autores com suas próprias funções (CRUD)

class ClienteDao:
    @staticmethod
    def getCliente(id):
        return Cliente.query.get(id)

    @staticmethod
    def getAllClientes():
        return Cliente.query.all()

    @staticmethod
    def addCliente(nome, email, nascimento, rg, telefone):
        cliente = Cliente(nome=nome, email=email, nascimento=nascimento, rg=rg, telefone=telefone)
        db.session.add(cliente)
        db.session.commit()
        return cliente.toJson()

    @staticmethod
    def attCliente(id, nome, email, nascimento, rg, telefone):
        cliente = ClienteDao.getCliente(id)
        if cliente:
            cliente.nome = nome
            cliente.email = email
            cliente.nascimento = nascimento
            cliente.rg = rg
            cliente.telefone = telefone
            db.session.commit()
        return cliente.toJson()

    @staticmethod
    def delCliente(id):
        cliente = ClienteDao.getCliente(id)
        if cliente:
            db.session.delete(cliente)
            db.session.commit()