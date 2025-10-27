class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        return f"{self.ano} {self.marca} {self.modelo}"

    def __str__(self):
        return self.exibir_informacoes()


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def exibir_informacoes(self):
        info_veiculo = super().exibir_informacoes()
        return f"{info_veiculo}, Portas: {self.portas}"


class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, tipo):
        super().__init__(marca, modelo, ano)
        self.tipo = tipo

    def exibir_informacoes(self):
        info_veiculo = super().exibir_informacoes()
        return f"{info_veiculo}, Tipo: {self.tipo}"


class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, capacidade_carga):
        super().__init__(marca, modelo, ano)
        self.capacidade_carga = capacidade_carga

    def exibir_informacoes(self):
        info_veiculo = super().exibir_informacoes()
        return f"{info_veiculo}, Capacidade de Carga: {self.capacidade_carga} kg"


# Exemplo de uso
if __name__ == "__main__":

    carro = Carro("Toyota", "Corolla", 2020, 4)
    moto = Motocicleta("Honda", "CBR600RR", 2019, "Esportiva")
    caminhao = Caminhao("Volvo", "FH16", 2018, 20000)

    print(carro)
    print(moto)
    print(caminhao)

# Saída esperada:
# 2020 Toyota Corolla, Portas: 4
# 2019 Honda CBR600RR, Tipo: Esportiva
# 2018 Volvo FH16, Capacidade de Carga: 20000 kg
