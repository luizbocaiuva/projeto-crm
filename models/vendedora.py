import os

class Vendedora:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

        self.session_path = f'./sessions/sessao_{id}'

    def __str__(self):
        return f'ID: {self.id} - Vendedora: {self.nome}'