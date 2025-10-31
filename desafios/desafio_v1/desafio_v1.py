# Módulos para Classes Abstratas e Datas
from abc import ABC, abstractmethod, abstractclassmethod, abstractproperty
from datetime import datetime

# ----------------------------------------------------------------------
# 1. CLASSES ABSTRATAS (Interfaces)
# ----------------------------------------------------------------------


class Cliente(ABC):
    """Define a interface base para todos os tipos de Clientes."""

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        # A lógica real da transação é delegada para o objeto Transacao
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta(ABC):
    """Define a interface base para todas as Contas Bancárias."""

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()  # Historico é uma classe separada

    # Método de Fábrica Abstrato: Obriga subclasses a criar um método 'nova_conta'
    @classmethod
    @abstractmethod
    def nova_conta(cls, cliente, numero):
        pass

    # Propriedades Abstratas (não obrigatórias aqui, mas boas para consistência)
    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    # Métodos Abstratos de Ação
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass


class Transacao(ABC):
    """Define a interface base para todas as Transações (Saque, Depósito, etc.)."""

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        # Obriga a ter um método para registrar a transação no histórico
        pass


# ----------------------------------------------------------------------
# 2. IMPLEMENTAÇÕES CONCRETAS
# ----------------------------------------------------------------------


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Historico:
    """Registra o histórico de transações de uma conta."""

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    # Implementação do Método de Fábrica (obrigatório pela Interface Conta)
    @classmethod
    def nova_conta(cls, cliente, numero):
        # A nova_conta pode ser simplificada aqui, dependendo da necessidade
        return cls(numero, cliente)

    # Implementação do método Sacar (obrigatório pela Interface Conta)
    def sacar(self, valor):
        saldo = self.saldo
        numero_saques = len(
            [t for t in self.historico.transacoes if t["tipo"] == Saque.__name__]
        )

        if valor > saldo:
            print("!!! Operação falhou! Saldo insuficiente.")
        elif valor > self._limite:
            print("!!! Operação falhou! Valor excede o limite de R$ 500.00.")
        elif numero_saques >= self._limite_saques:
            print("!!! Operação falhou! Número máximo de saques (3) excedido.")
        elif valor > 0:
            self._saldo -= valor
            self.historico.adicionar_transacao(
                Saque(valor)
            )  # Adiciona ao histórico AQUI
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("!!! Operação falhou! Valor de saque inválido.")
            return False

        return False

    # Implementação do método Depositar (obrigatório pela Interface Conta)
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.historico.adicionar_transacao(
                Deposito(valor)
            )  # Adiciona ao histórico AQUI
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            return True
        else:
            print("!!! Operação falhou! Valor de depósito inválido.")
            return False


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @classmethod
    def registrar(cls, conta):
        # A transação Saque aqui registra a si mesma no histórico
        conta.sacar(cls.valor)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    @classmethod
    def registrar(cls, conta):
        # A transação Deposito aqui registra a si mesma no histórico
        conta.depositar(cls.valor)


# ----------------------------------------------------------------------
# 3. TESTE (EXEMPLO DE USO)
# ----------------------------------------------------------------------

print("--- TESTE DE POO E HERANÇA ---")

# 1. Criação do Cliente e da Conta
cliente_teste = PessoaFisica("Ana Silva", "01/01/1990", "123.456.789-00", "Rua POO, 1")
conta_cc = ContaCorrente.nova_conta(cliente_teste, numero=1001)
cliente_teste.adicionar_conta(conta_cc)

print(f"Cliente: {cliente_teste.nome} | Endereço: {cliente_teste.endereco}")
print(f"Conta: {conta_cc.agencia}-{conta_cc.numero}")

# 2. Realizando Transações
conta_cc.depositar(500)
conta_cc.sacar(100)
conta_cc.sacar(100)

# 3. Exibindo Saldo e Histórico
print(f"\nSaldo Atual: R$ {conta_cc.saldo:.2f}")

print("\n=== Relatório do Histórico ===")
for transacao in conta_cc.historico.transacoes:
    print(f"- {transacao['tipo']}: R$ {transacao['valor']:.2f}")
