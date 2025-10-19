# Sistema Bancário Modularizado em Python

Este projeto é a evolução de um sistema bancário simples, implementado em Python, com o objetivo de demonstrar a modularização de código através de funções e a utilização avançada de argumentos em Python (Posicionais e Nomeados) e **baseado** no projeto no GitHub da DIO. (https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)

O sistema suporta múltiplos clientes e múltiplas contas correntes, e segue regras de negócio e de implementação rigorosas, conforme os requisitos do desafio.

## 🚀 Funcionalidades

O sistema oferece as seguintes operações através de um menu interativo:

- **Novo Usuário (`nu`):** Cadastro de clientes (usuários) com validação de CPF único.
- **Nova Conta (`nc`):** Criação de uma conta corrente (Agência fixa: `0001`) vinculada a um usuário existente.
- **Depositar (`d`):** Adiciona valor ao saldo da conta selecionada.
- **Sacar (`s`):** Retira valor do saldo, respeitando limites de valor e o limite diário de 3 saques.
- **Extrato (`e`):** Exibe o histórico de movimentações e o saldo atual da conta selecionada.
- **Listar Contas (`lc`):** Apresenta um resumo de todas as contas cadastradas no sistema.
- **Sair (`q`):** Encerra a aplicação.

## 🛠️ Requisitos Técnicos e Implementação Avançada

O grande diferencial deste projeto é o uso estratégico de argumentos para enforcecer (forçar) a forma como as funções devem ser chamadas.

| Função | Assinatura | Tipo de Argumento | Objetivo |
| :--- | :--- | :--- | :--- |
| `depositar()` | `def depositar(conta, valor, /)` | Posicional-Only (`/`) | Garante que `conta` e `valor` sejam passados **apenas pela ordem**, melhorando a legibilidade e impedindo chamadas com `valor=...`. |
| `sacar()` | `def sacar(*, conta, valor)` | Keyword-Only (`*`) | Garante que `conta` e `valor` sejam passados **apenas pelo nome**, tornando a intenção do código explícita. |
| `exibir_extrato()` | `def exibir_extrato(saldo, /, *, extrato)` | Misto (`/` e `*`) | Demonstra a combinação de argumentos posicionais obrigatórios (`saldo`) e nomeados obrigatórios (`extrato`). |

### Estrutura de Dados

O sistema utiliza listas e dicionários para armazenar os dados em memória:

| Entidade | Estrutura | Campos Chave |
| :--- | :--- | :--- |
| **Usuário** | Dicionário em Lista | `nome`, `data_nascimento`, `cpf` (único, apenas números), `endereco`. |
| **Conta** | Dicionário em Lista | `agencia` (`0001`), `numero` (sequencial), `usuario` (referência ao objeto usuário), `saldo`, `extrato`, `numero_saques`. |