"""Operações relacionadas ao cadastro de produtos."""

from coffee_shop.data import produtos
from coffee_shop.models import Produto


def cadastrar_produto():
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("O nome do produto não pode ficar vazio.")
        return

    try:
        preco = float(input("Preço do produto: R$").replace(",", "."))
        if preco <= 0:
            print("O preço deve ser maior que zero.")
            return
    except ValueError:
        print("Preço inválido. Digite um número, por exemplo: 12.50.")
        return

    descricao = input("Descrição do produto: ").strip()
    produto = Produto(nome, preco, descricao)
    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso!")
