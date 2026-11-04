"""Ponto de entrada e menu principal da aplicação."""

from coffee_shop.clientes import cadastrar_cliente
from coffee_shop.pedidos import fazer_pedido, ver_pedidos
from coffee_shop.produtos import cadastrar_produto


def menu():
    while True:
        print("\n=== COFFEE SHOPS TIA ROSA ===")
        print("1. Cadastrar cliente")
        print("2. Cadastrar produto")
        print("3. Fazer pedido")
        print("4. Ver pedidos")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_produto()
        elif opcao == "3":
            fazer_pedido()
        elif opcao == "4":
            ver_pedidos()
        elif opcao == "5":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção de 1 a 5.")


if __name__ == "__main__":
    menu()
