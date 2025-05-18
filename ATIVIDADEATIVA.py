clientes = []
produtos = []
pedidos = []

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
        self.total = sum([p.preco for p in itens])

def cadastrar_cliente():
    nome = input("Nome do cliente: ")
    telefone = input("Telefone do cliente: ")
    cliente = Cliente(nome, telefone)
    clientes.append(cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

def cadastrar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: R$"))
    descricao = input("Descrição do produto: ")
    produto = Produto(nome, preco, descricao)
    produtos.append(produto)
    print(f"Produto {nome} cadastrado com sucesso!")

def fazer_pedido():
    if not clientes or not produtos:
        print("Cadastre ao menos um cliente e um produto antes de realizar pedidos.")
        return
    print("Clientes:")
    for i, c in enumerate(clientes):
        print(f"[{i}] {c.nome}")
    cliente_numero = int(input("Escolha o numero do cliente: "))
    cliente = clientes[cliente_numero]

    itens = []
    while True:
        print("Produtos disponíveis:")
        for i, p in enumerate(produtos):
            print(f"[{i}] {p.nome} - R${p.preco:.2f}")
        opcao = input("Digite o numero do produto (ou 'fim' para encerrar): ")
        if opcao.lower() == 'fim':
            break
        try:
            produto = produtos[int(opcao)]
            itens.append(produto)
            print(f"Produto [{opcao}] adicionado.")
        except (ValueError, IndexError):
            print("inválido. Tente novamente.")
    if itens:
        pedido = Pedido(cliente, itens)
        pedidos.append(pedido)
        print(f"Pedido realizado com sucesso para {cliente.nome}!")
    else:
        print("Nenhum produto foi selecionado.")

def ver_pedidos():
    if not pedidos:
        print("Nenhum pedido realizado.")
        return
    for i, p in enumerate(pedidos):
        print(f"Pedido {i + 1} - Cliente: {p.cliente.nome} - Total: R${p.total:.2f}")

def menu():
    while True:
        print("\n=== COFFEE SHOPS TIA ROSA ===")
        print("1. Cadastrar cliente")
        print("2. Cadastrar produto")
        print("3. Fazer pedido")
        print("4. Ver pedidos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_produto()
        elif opcao == '3':
            fazer_pedido()
        elif opcao == '4':
            ver_pedidos()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
