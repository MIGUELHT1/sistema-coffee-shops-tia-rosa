"""Modelos que representam os dados do sistema."""


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Produto:
    def __init__(self, nome, preco, descricao=""):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao


class Pedido:
    def __init__(self, cliente, itens):
        self.cliente = cliente
        self.itens = itens
        self.total = sum(produto.preco for produto in itens)
