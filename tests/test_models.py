"""Testes unitários para os modelos do sistema."""

import unittest

from coffee_shop.models import Cliente, Pedido, Produto


class ClienteTests(unittest.TestCase):
    def test_cliente_armazenas_nome_e_telefone(self):
        cliente = Cliente("Ana", "61999990000")

        self.assertEqual(cliente.nome, "Ana")
        self.assertEqual(cliente.telefone, "61999990000")


class ProdutoTests(unittest.TestCase):
    def test_produto_armazenas_dados(self):
        produto = Produto("Café", 8.50, "Café coado")

        self.assertEqual(produto.nome, "Café")
        self.assertEqual(produto.preco, 8.50)
        self.assertEqual(produto.descricao, "Café coado")

    def test_descricao_pode_ser_opcional(self):
        produto = Produto("Pão de queijo", 6.00)

        self.assertEqual(produto.descricao, "")


class PedidoTests(unittest.TestCase):
    def test_pedido_calcula_total_dos_itens(self):
        cliente = Cliente("Ana", "61999990000")
        itens = [
            Produto("Café", 8.50),
            Produto("Pão de queijo", 6.00),
            Produto("Suco", 7.50),
        ]

        pedido = Pedido(cliente, itens)

        self.assertIs(pedido.cliente, cliente)
        self.assertEqual(pedido.itens, itens)
        self.assertAlmostEqual(pedido.total, 22.00)

    def test_pedido_sem_itens_tem_total_zero(self):
        cliente = Cliente("Ana", "61999990000")

        pedido = Pedido(cliente, [])

        self.assertEqual(pedido.total, 0)


if __name__ == "__main__":
    unittest.main()
