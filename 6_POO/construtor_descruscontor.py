class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print(f"Faleceu o cachorro {self.nome}.")

    def latir(self):
        return f"Au au"


def criar_cachorro():
    c = cachorro("Toto", "Branco e Preto", acordado=False)
    print(c.latir())


# del c

criar_cachorro()
