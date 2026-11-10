# Coffee Shops Tia Rosa

![Testes automatizados](https://github.com/MIGUELHT1/sistema-coffee-shops-tia-rosa/actions/workflows/tests.yml/badge.svg)


Aplicação de terminal desenvolvida em Python para simular o gerenciamento básico de uma cafeteria. O projeto pratica Programação Orientada a Objetos, organização em módulos, validação de entradas e testes unitários.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Paradigma](https://img.shields.io/badge/Paradigma-POO-6C5CE7?style=flat-square)
![Testes](https://img.shields.io/badge/Testes-unittest-555555?style=flat-square)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

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
- Testes unitários com `unittest`
- Integração contínua com GitHub Actions

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

## Testes automatizados

Os testes unitários verificam os modelos de cliente, produto e pedido, incluindo o cálculo do valor total.

Execute todos os testes pela raiz do projeto:

```bash
python -m unittest discover -v
```

O GitHub Actions está configurado para executar essa suíte automaticamente em cada push para `main` e em pull requests direcionados à branch `main`. O resultado da primeira execução pode ser acompanhado na aba **Actions** do repositório.

## Estrutura do projeto

```text
sistema-coffee-shops-tia-rosa/
├── .github/
│   └── workflows/
│       └── tests.yml
├── coffee_shop/
│   ├── __init__.py
│   ├── clientes.py
│   ├── data.py
│   ├── main.py
│   ├── models.py
│   ├── pedidos.py
│   └── produtos.py
├── tests/
│   ├── __init__.py
│   └── test_models.py
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
| `tests/test_models.py` | Testes unitários dos modelos |
| `.github/workflows/tests.yml` | Automação da execução dos testes |

## Limitações conhecidas

- Os dados ficam armazenados apenas em memória e são perdidos ao encerrar o programa.
- O projeto ainda não utiliza banco de dados.
- A interface é executada somente pelo terminal.
- A cobertura atual de testes está concentrada nos modelos; os fluxos interativos ainda podem receber testes específicos.

## Próximas melhorias

- Adicionar persistência de dados com SQLite.
- Ampliar os testes para os fluxos de cadastro e pedidos.
- Separar melhor as regras de negócio da interface de terminal.
- Avaliar uma futura versão com API REST.

## Autor

**Miguel Miranda**  
Estudante de Engenharia de Software e interessado em oportunidades de estágio na área de tecnologia.

[GitHub: @MIGUELHT1](https://github.com/MIGUELHT1)

---

<sub>Projeto de estudo em evolução contínua.</sub>
