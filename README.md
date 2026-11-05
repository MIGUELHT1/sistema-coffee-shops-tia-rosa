# Coffee Shops Tia Rosa

Aplicação de terminal desenvolvida em Python para simular o gerenciamento básico de uma cafeteria. O projeto foi criado para praticar Programação Orientada a Objetos, organização em módulos e validação de entradas.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Paradigma](https://img.shields.io/badge/Paradigma-POO-6C5CE7?style=flat-square)
![Status](https://img.shields.io/badge/Status-Projeto%20de%20estudo-555555?style=flat-square)

</div>

## Funcionalidades

- Cadastro de clientes com nome e telefone.
- Cadastro de produtos com nome, preço e descrição.
- Criação de pedidos associados a um cliente.
- Seleção de vários produtos por pedido.
- Cálculo e consulta do total dos pedidos.
- Validação básica de entradas e opções inválidas.

## Tecnologias e conceitos

- **Python 3**
- Programação Orientada a Objetos (POO)
- Módulos e pacotes
- Listas e estruturas de controle
- Tratamento de exceções

## Como executar

**Requisitos:** Python 3 instalado. Não são necessárias dependências externas.

1. Clone o repositório:

   ```bash
   git clone https://github.com/MIGUELHT1/sistema-coffee-shops-tia-rosa.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd sistema-coffee-shops-tia-rosa
   ```

3. Inicie a aplicação:

   ```bash
   python ATIVIDADEATIVA.py
   ```

   Como alternativa, execute:

   ```bash
   python -m coffee_shop.main
   ```

## Estrutura do projeto

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

### Responsabilidade dos módulos

| Arquivo | Responsabilidade |
|---|---|
| `models.py` | Classes Cliente, Produto e Pedido |
| `data.py` | Armazenamento dos dados durante a execução |
| `clientes.py` | Cadastro de clientes |
| `produtos.py` | Cadastro e validação de produtos |
| `pedidos.py` | Criação e consulta de pedidos |
| `main.py` | Menu principal da aplicação |
| `ATIVIDADEATIVA.py` | Ponto de entrada alternativo |

## Limitações conhecidas

- Os dados ficam armazenados apenas em memória e são perdidos ao encerrar o programa.
- O projeto ainda não utiliza banco de dados.
- A interface é executada somente pelo terminal.
- Não há testes automatizados documentados neste momento.

## Próximas melhorias

- Adicionar persistência de dados com SQLite.
- Criar testes automatizados com `unittest` ou `pytest`.
- Separar melhor as regras de negócio da interface de terminal.
- Avaliar uma futura versão com API REST.

## Autor

**Miguel Miranda**  
Estudante de Engenharia de Software e interessado em oportunidades de estágio na área de tecnologia.

[GitHub: @MIGUELHT1](https://github.com/MIGUELHT1)

---

<sub>Projeto de estudo em evolução contínua.</sub>
