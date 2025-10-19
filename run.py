import textwrap

# Constantes globais
AGENCIA = "0001"
LIMITE_SAQUES = 3

def menu():
    """Exibe o menu de opções para o usuário e lê a opção."""
    menu_texto = """
    =============== MENU ===============
    [d]    Depositar
    [s]    Sacar
    [e]    Extrato
    [nc]   Nova Conta
    [lc]   Listar Contas
    [nu]   Novo Usuário
    [q]    Sair
    """
    
    # Imprime o menu formatado
    print(textwrap.dedent(menu_texto)) 
    
    # Pede a opção e retorna, garantindo que o input é minúsculo
    return input("=> Sua opção: ").lower()


# =========================================================================
# FUNÇÕES DE OPERAÇÃO BANCÁRIA (Com regras de passagem de argumentos)
# =========================================================================

def depositar(conta, valor, /):
    """
    Realiza um depósito.
    Argumentos: Apenas por POSIÇÃO (positional only).
    """
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'] += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def sacar(*, conta, valor):
    """
    Realiza um saque.
    Argumentos: Apenas NOMEADOS (keyword only).
    """
    saldo = conta['saldo']
    limite = conta['limite']
    numero_saques = conta['numero_saques']
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        conta['saldo'] -= valor
        conta['extrato'] += f"Saque:\t\tR$ {valor:.2f}\n"
        conta['numero_saques'] += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def exibir_extrato(conta, /):
    """
    Exibe o extrato e o saldo.
    Argumentos: A conta por POSIÇÃO.
    """
    saldo = conta['saldo']
    extrato = conta['extrato']
    
    # Chamada interna para cumprir a regra original da imagem (para fins didáticos)
    _exibir_extrato_regra(saldo, extrato=extrato)


def _exibir_extrato_regra(saldo, /, *, extrato):
    """Função auxiliar para cumprir a regra de argumento posicional/nomeado."""
    print("\n============== EXTRATO ==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=====================================")


# =========================================================================
# FUNÇÕES DE CADASTRO E BUSCA
# =========================================================================

def filtrar_usuario(cpf, usuarios):
    """Busca um usuário na lista pelo CPF."""
    cpf_limpo = ''.join(filter(str.isdigit, cpf))
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf_limpo]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def recuperar_conta(contas):
    """Busca e retorna uma conta na lista pelo número."""
    # Como a agência é fixa ("0001"), apenas pedimos o número da conta
    print("\n--- SELEÇÃO DE CONTA ---")
    
    # Para ser didático, mantemos a agência no input, mas já sabemos o valor
    agencia = input("Informe a Agência (0001): ")
    
    try:
        numero = int(input("Informe o Número da Conta: "))
    except ValueError:
        print("\n@@@ Número de conta inválido. @@@")
        return None
    
    for conta in contas:
        # A conta do usuário tem que ter a agência e o número corretos
        if conta['agencia'] == agencia and conta['numero'] == numero:
            return conta
            
    print("\n@@@ Conta não encontrada. @@@")
    return None
    

def criar_usuario(usuarios):
    """
    Cadastra um novo usuário (cliente).
    Requisito: CPF único (apenas números).
    """
    cpf_input = input("Informe o CPF (somente números): ")
    cpf_limpo = ''.join(filter(str.isdigit, cpf_input))

    if filtrar_usuario(cpf_limpo, usuarios):
        print("\n@@@ Operação falhou! Já existe usuário com este CPF. @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    
    logradouro = input("Informe o logradouro (ex: Rua ABC): ")
    nro = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade_estado = input("Informe a cidade/sigla estado (ex: São Paulo/SP): ")

    endereco = f"{logradouro}, {nro} - {bairro} - {cidade_estado}"

    usuarios.append({
        "nome": nome, 
        "data_nascimento": data_nascimento, 
        "cpf": cpf_limpo, 
        "endereco": endereco
    })
    
    print("\n=== Usuário criado com sucesso! ===")


def criar_conta(agencia, numero_conta, usuarios, contas):
    """
    Cria uma nova conta corrente e a vincula a um usuário existente.
    NOTA: Inicializa a conta com seus próprios dados financeiros.
    """
    cpf = input("Informe o CPF do usuário para vincular à conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None

    # Inicializa a conta com seus próprios dados financeiros e limites
    nova_conta = {
        "agencia": agencia, 
        "numero": numero_conta, 
        "usuario": usuario,
        "saldo": 0,
        "limite": 500,
        "extrato": "",
        "numero_saques": 0
    }
    
    contas.append(nova_conta)
    print("\n=== Conta criada com sucesso! ===")
    print(f"Agência: {agencia} | Conta: {numero_conta}")
    return nova_conta


def listar_contas(contas):
    """Lista todas as contas cadastradas."""
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return
        
    print("\n============ LISTA DE CONTAS ============")
    # Usa o 'enumerate' para listar as contas de forma mais clara
    for i, conta in enumerate(contas, start=1):
        linha = f"""\
            Conta {i}:
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero']}
            Titular:\t{conta['usuario']['nome']}
            Saldo:\t\tR$ {conta['saldo']:.2f}
        """
        print(textwrap.dedent(linha))
    print("=========================================")


# =========================================================================
# FUNÇÃO PRINCIPAL
# =========================================================================

def main():
    """Função principal que gerencia o fluxo do programa."""
    
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            conta_selecionada = recuperar_conta(contas)
            if conta_selecionada:
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    depositar(conta_selecionada, valor) 
                except ValueError:
                    print("\n@@@ Valor de depósito inválido. @@@")

        elif opcao == "s":
            conta_selecionada = recuperar_conta(contas)
            if conta_selecionada:
                try:
                    valor = float(input("Informe o valor do saque: "))
                    sacar(conta=conta_selecionada, valor=valor)
                except ValueError:
                    print("\n@@@ Valor de saque inválido. @@@")

        elif opcao == "e":
            conta_selecionada = recuperar_conta(contas)
            if conta_selecionada:
                exibir_extrato(conta_selecionada)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            conta_nova = criar_conta(AGENCIA, numero_conta, usuarios, contas)
            if conta_nova:
                numero_conta += 1

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


# Iniciar o programa
if __name__ == "__main__":
    main()