# ☕ Coffee Shops Tia Rosa

Sistema de terminal desenvolvido em Python para simular o gerenciamento básico de uma cafeteria. O projeto pratica Programação Orientada a Objetos, organização em módulos e validação de entradas.

## ✨ Funcionalidades

- Cadastro de clientes com nome e telefone.
- Cadastro de produtos com nome, preço e descrição.
- Criação de pedidos associados a um cliente.
- Seleção de vários produtos por pedido.
- Cálculo e consulta do total dos pedidos.
- Validação básica de entradas e opções inválidas.

## 🧰 Tecnologias e conceitos

- **Python 3**
- Programação Orientada a Objetos (POO)
- Módulos e pacotes
- Listas e estruturas de controle
- Tratamento de exceções

## ▶️ Como executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/MIGUELHT1/sistema-coffee-shops-tia-rosa.git
   ```

2. Acesse a pasta:

   ```bash
   cd sistema-coffee-shops-tia-rosa
   ```

3. Execute pela raiz do projeto:

   ```bash
   python ATIVIDADEATIVA.py
   ```

   Também é possível executar com `python -m coffee_shop.main`.

Não são necessárias dependências externas. O projeto utiliza apenas a biblioteca padrão do Python.

## 📁 Estrutura do projeto

```text
sistema-coffee-shops-tia-rosa/
├── coffee_shop/
│   ├── __init__.py
│   ├── clientes.py
│   ├── data.py
│   ├── main.py
│   ├── models.py
│   ├── pedidos.py
│   └── produtos.py
├── .gitignore
├── ATIVIDADEATIVA.py
└── README.md
```

### Organização dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `models.py` | Classes Cliente, Produto e Pedido |
| `data.py` | Listas usadas para armazenar os dados durante a execução |
| `clientes.py` | Cadastro de clientes |
| `produtos.py` | Cadastro e validação de produtos |
| `pedidos.py` | Criação e consulta de pedidos |
| `main.py` | Menu principal da aplicação |
| `ATIVIDADEATIVA.py` | Arquivo de inicialização |

## ⚠️ Limitações atuais

Os dados ficam armazenados apenas em memória. Ao fechar o programa, clientes, produtos e pedidos são perdidos. O projeto ainda não utiliza banco de dados nem possui uma interface gráfica ou API.

## 🛣️ Próximas melhorias

- Persistência de dados com SQLite.
- Testes automatizados com `unittest` ou `pytest`.
- Separação entre regras de negócio e interface de terminal.
- Evolução futura para uma API REST.

## 👨‍💻 Autor

**Miguel Miranda** — estudante de Engenharia de Software, direcionando os estudos para desenvolvimento Backend.

[GitHub: @MIGUELHT1](https://github.com/MIGUELHT1)

---

<p align="center">Projeto de aprendizado em evolução.</p>
