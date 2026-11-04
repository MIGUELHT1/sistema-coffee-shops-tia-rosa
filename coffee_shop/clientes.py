"""Operações relacionadas ao cadastro de clientes."""

from coffee_shop.data import clientes
from coffee_shop.models import Cliente


def cadastrar_cliente():
    nome = input("Nome do cliente: ").strip()
    if not nome:
        print("O nome do cliente não pode ficar vazio.")
        return

    telefone = input("Telefone do cliente: ").strip()
    if not telefone:
        print("O telefone do cliente não pode ficar vazio.")
        return

    cliente = Cliente(nome, telefone)
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")
