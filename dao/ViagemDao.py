from models import Viagem, db

class ViagemDao:
    @staticmethod
    def getViagem(id):
        return Viagem.query.get(id)

    @staticmethod
    def getAllViagens():
        return Viagem.query.all()

    @staticmethod
    def addViagem(destino, data_inicio, data_fim, preco, qtd_assentos, assentos_disponiveis):
        viagem = Viagem(destino=destino, data_inicio=data_inicio, data_fim=data_fim, preco=preco, qtd_assentos=qtd_assentos, assentos_disponiveis=assentos_disponiveis)
        db.session.add(viagem)
        db.session.commit()
        return viagem.toJson()

    @staticmethod
    def attViagem(id, destino, data_inicio, data_fim, preco, qtd_assentos, assentos_disponiveis):
        viagem = ViagemDao.getViagem(id)
        if viagem:
            viagem.destino = destino
            viagem.data_inicio = data_inicio
            viagem.data_fim = data_fim
            viagem.preco = preco
            viagem.aqt_assentos = qtd_assentos
            viagem.assentos_disponiveis = assentos_disponiveis
            db.session.commit()
        return viagem.toJson()

    @staticmethod
    def delViagem(id):
        viagem = ViagemDao.getViagem(id)
        if viagem:
            db.session.delete(viagem)
            db.session.commit()
        return viagem.toJson()
