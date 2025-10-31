class Passaro:
    def voar(self):
        return "O pássaro está voando."


class Pardal(Passaro):
    def voar(self):
        return super().voar()


class Avestruz(Passaro):
    def voar(self):
        return "O avestruz não pode voar."


class Aviao(Passaro):
    def voar(self):
        return "O avião está decolando."


def plano_de_voo(obj):
    obj.voar()


pardal = Pardal()
avestruz = Avestruz()
aviao = Aviao()


print(pardal.voar())
print(avestruz.voar())
print(aviao.voar())

aviao.plano_de_voo
