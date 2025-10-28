class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostart_saldo(self):
        return self._saldo


conta = Conta("01", 5000)
conta.depositar(500)
print(conta.nro_agencia)
print(conta.mostart_saldo())
