from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from datetime import datetime

class Viagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destino = db.Column(db.String(100), nullable=False)
    data_inicio = db.Column(db.Date, nullable=False)
    data_fim = db.Column(db.Date, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    qtd_assentos = db.Column(db.Integer, nullable=False)
    assentos_disponiveis = db.Column(db.JSON, nullable=False)
    # Relacionamento: Uma viagem pode ter várias reservas
    reservas = db.relationship('Reserva', backref='viagem', lazy=True)

    def __repr__(self):
        return f"<Viagem {self.destino}>"

    def toJson(self):
        return {
            "id": self.id,
            "destino": self.destino,
            "data_inicio": self.data_inicio.strftime('%Y-%m-%d'),
            "data_fim": self.data_fim.strftime('%Y-%m-%d'),
            "preco": self.preco,
            "qtd_assentos": self.qtd_assentos,
            "assentos_disponiveis": self.assentos_disponiveis,
            "reservas": [reserva.toJson() for reserva in self.reservas]
        }
    