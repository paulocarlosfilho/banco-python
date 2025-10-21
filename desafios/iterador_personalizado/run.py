import textwrap
import datetime
import functools

# Constantes globais
AGENCIA = "0001"
LIMITE_SAQUES = 3

# =========================================================================
# ITERADOR PERSONALIZADO (Novo Requisito DIO)
# =========================================================================

class ContaIterador:
    """
    Iterador personalizado que permite iterar sobre a lista de contas.
    Implementa __iter__ e __next__ para ser um iterador válido.
    """
    def __init__(self, contas):
        self._contas = contas
        self._index = 0

    def __iter__(self):
        # Retorna a instância do próprio iterador
        return self

    def __next__(self):
        # Verifica se ainda há contas
        if self._index < len(self._contas):
            conta = self._contas[self._index]
            self._index += 1
            
            # Retorna um formato básico de informação da conta
            return f"""\
Conta {self._index}:
Agência:\t{conta['agencia']}
C/C:\t\t{conta['numero']}
Titular:\t{conta['usuario']['nome']}
Saldo:\t\tR$ {conta['saldo']:.2f}
"""
        else:
            # Levanta StopIteration para sinalizar o fim da iteração
            raise StopIteration


# =========================================================================
# DECORADOR DE LOG
# =========================================================================

def log_transacao(funcao):
    """
    Decorador que registra (printa) a data, hora e o tipo de transação (nome da função).
    """
    @functools.wraps(funcao)
    def wrapper(*args, **kwargs):
        resultado = funcao(*args, **kwargs)
        agora = datetime.datetime.now()
        data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M:%S")
        nome_transacao = funcao.__name__.upper()

        print("=" * 30)
        print(f"LOG DE TRANSAÇÃO:")
        print(f"Tipo: {nome_transacao}")
        print(f"Data/Hora: {data_hora_formatada}")
        print("=" * 30)
        
        return resultado
        
    return wrapper


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
    print(textwrap.dedent(menu_texto)) 
    return input("=> Sua opção: ").lower()


# =========================================================================
# FUNÇÕES DE OPERAÇÃO BANCÁRIA
# =========================================================================

@log_transacao
def depositar(*, conta, valor):
    """Realiza um depósito."""
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'].append({"tipo": "d", "valor": valor})
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

@log_transacao
def sacar(*, conta, valor):
    """Realiza um saque."""
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
        conta['extrato'].append({"tipo": "s", "valor": valor})
        conta['numero_saques'] += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")


def gerar_relatorio(extrato, tipo_transacao=None):
    """
    Função Geradora que itera sobre as transações e filtra opcionalmente por tipo.
    """
    for transacao in extrato:
        if tipo_transacao is None or transacao['tipo'] == tipo_transacao:
            yield transacao


def exibir_extrato(conta, /):
    """Exibe o extrato e o saldo usando o Gerador de Relatórios."""
    extrato_lista = conta['extrato']
    saldo = conta['saldo']
    
    filtro = input("Deseja filtrar por [d] Depósito, [s] Saque, ou [n] Não filtrar? ").lower()
    
    if filtro not in ('d', 's'):
        filtro = None
    
    transacoes_geradas = gerar_relatorio(extrato_lista, filtro)
    
    print("\n============== EXTRATO ==============")
    if not extrato_lista:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in transacoes_geradas:
            tipo_display = "Depósito" if transacao['tipo'] == 'd' else "Saque"
            print(f"{tipo_display}:\t\tR$ {transacao['valor']:.2f}")

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
    print("\n--- SELEÇÃO DE CONTA ---")
    agencia = input("Informe a Agência (0001): ")
    
    try:
        numero = int(input("Informe o Número da Conta: "))
    except ValueError:
        print("\n@@@ Número de conta inválido. @@@")
        return None
    
    for conta in contas:
        if conta['agencia'] == agencia and conta['numero'] == numero:
            return conta
            
    print("\n@@@ Conta não encontrada. @@@")
    return None
    
@log_transacao
def criar_usuario(usuarios):
    """Cadastra um novo usuário (cliente)."""
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

@log_transacao
def criar_conta(*, agencia, numero_conta, usuarios, contas):
    """Cria uma nova conta corrente e a vincula a um usuário existente."""
    cpf = input("Informe o CPF do usuário para vincular à conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None

    nova_conta = {
        "agencia": agencia, 
        "numero": numero_conta, 
        "usuario": usuario,
        "saldo": 0,
        "limite": 500,
        "extrato": [],
        "numero_saques": 0
    }
    
    contas.append(nova_conta)
    print("\n=== Conta criada com sucesso! ===")
    print(f"Agência: {agencia} | Conta: {numero_conta}")
    return nova_conta


def listar_contas(contas):
    """
    Lista todas as contas cadastradas, usando o Iterador Personalizado.
    """
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada! @@@")
        return
        
    print("\n============ LISTA DE CONTAS ============")
    
    # Cria a instância do iterador
    iterador_contas = ContaIterador(contas) 
    
    # O for loop chama __iter__ e depois __next__ repetidamente
    for linha_conta in iterador_contas:
        print(textwrap.dedent(linha_conta))
        
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
                    depositar(conta=conta_selecionada, valor=valor) 
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
            conta_nova = criar_conta(agencia=AGENCIA, 
                                     numero_conta=numero_conta, 
                                     usuarios=usuarios, 
                                     contas=contas)
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