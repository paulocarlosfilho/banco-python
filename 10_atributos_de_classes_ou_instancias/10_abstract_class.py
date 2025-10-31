from abc import ABC, abstractmethod


class ControleRemoto(ABC):

    @property
    @abstractmethod
    def marca(self):
        pass

    # Métodos abstratos que devem ser implementados pelas subclasses
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass


class ControleRemotoTv(ControleRemoto):
    def ligar(self):
        print("A TV está ligada.")

    def desligar(self):
        print("A TV está desligada.")

    @property
    def marca(self):
        return "Marca da TV é Samsung"


class ControleRemotoArCondicionando(ControleRemoto):
    def ligar(self):
        print("O ar condicionado está ligado.")

    def desligar(self):
        print("O ar condicionado está desligado.")

    @property
    def marca(self):
        return "Marca do ar condicionado é LG"


controle_tv = ControleRemotoTv()
controle_tv.ligar()
print(controle_tv.marca)
controle_tv.desligar()

print(30 * "=")  # Apenas para separar a saída

controle_ar = ControleRemotoArCondicionando()
controle_ar.ligar()
print(controle_ar.marca)
controle_ar.desligar()
