from database import db
from sqlalchemy import*
from sqlalchemy.orm import*
from datetime import datetime

# Classe Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    nascimento = db.Column(db.Date, nullable=False)
    rg = db.Column(db.String(100), unique=True, nullable=False)
    telefone = db.Column(db.String(20))
    # Relacionamento: Um cliente pode ter várias reservas
    reservas = db.relationship('Reserva', backref='cliente', lazy=True)

    def __repr__(self):
        return f"<Cliente {self.nome}>"

    def toJson(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "nascimento": self.nascimento,
            "rg": self.rg,
            "telefone": self.telefone,
            "reservas": [reserva.toJson() for reserva in self.reservas]
        }
