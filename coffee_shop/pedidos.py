"""Operações relacionadas à criação e consulta de pedidos."""

from coffee_shop.data import clientes, pedidos, produtos
from coffee_shop.models import Pedido


def fazer_pedido():
    if not clientes or not produtos:
        print("Cadastre ao menos um cliente e um produto antes de realizar pedidos.")
        return

    print("\nClientes cadastrados:")
    for indice, cliente in enumerate(clientes):
        print(f"[{indice}] {cliente.nome}")

    try:
        numero_cliente = int(input("Escolha o número do cliente: "))
        cliente = clientes[numero_cliente]
    except (ValueError, IndexError):
        print("Cliente inválido. Verifique o número informado.")
        return

    itens = []
    while True:
        print("\nProdutos disponíveis:")
        for indice, produto in enumerate(produtos):
            print(f"[{indice}] {produto.nome} - R$\{produto.preco:.2f}")

        opcao = input("Digite o número do produto ou 'fim' para encerrar: ").strip().lower()
        if opcao == "fim":
            break

        try:
            produto = produtos[int(opcao)]
            itens.append(produto)
            print(f"Produto {produto.nome} adicionado ao pedido.")
        except (ValueError, IndexError):
            print("Opção inválida. Tente novamente.")

    if not itens:
        print("Nenhum produto foi selecionado. Pedido não realizado.")
        return

    pedido = Pedido(cliente, itens)
    pedidos.append(pedido)
    print(f"Pedido realizado com sucesso para {cliente.nome}!")
    print(f"Total do pedido: R$\{pedido.total:.2f}")


def ver_pedidos():
    if not pedidos:
        print("Nenhum pedido realizado.")
        return

    print("\n=== PEDIDOS REALIZADOS ===")
    for indice, pedido in enumerate(pedidos, start=1):
        print(f"Pedido {indice} - Cliente: {pedido.cliente.nome} - Total: R$\{pedido.total:.2f}")
