class bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        return "Biiiiiiiii!"

    def parar(self):
        return "A bicicleta parou."

    def correr(self):
        return "A bicicleta está em movimento. Rapida como um Foguete!!!!!!"

    def trocar_marcha(self, numero_marcha):
        print("Trocando Marcha...")

        def _trocar_marcha():
            if self > self.marchas:
                print("Marcha trocada")
            else:
                print("Não foi possivel trocar a marcha.")

    # Não esquecer - Metodo para ajustar a representação em string do objeto
    def __str__(self):
        return f"{self.__class__.__name__.capitalize()}: {', '.join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"


caloi = bicicleta("vermelha", "mountain bike", 2021, 1500.00)

print(
    f"Detalhes da bicicleta: Cor - {caloi.cor}"
    f", Modelo - {caloi.modelo}"
    f", Ano - {caloi.ano}"
    f", Valor - {caloi.valor}"
    f"\n {caloi.buzinar()}"
    f"\n {caloi.correr()}"
    f"\n {caloi.trocar_marcha(1)}"
    f"\n {caloi.parar()}"
)
print(caloi)
