class Animal:
    def __init__(self, nro_patas, *args, **kwargs):
        self.nro_patas = nro_patas

        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{k} = {v}' for k, v in self.__dict__.items()])}"

    def miau_falar(self):
        return "Miaaaaaaaaaaaaaaaaaaaaaauu porra. u.u"


class Albino:
    def __init__(self, *args, albino=False, **kwargs):
        self.albino = albino
        super().__init__(*args, **kwargs)


# --- Classes Intermediárias ---
class Mamifero(Animal):
    def __init__(self, cor_pelo, *args, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(*args, **kwargs)


class Ave(Animal):
    def __init__(self, cor_bico, *args, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(*args, **kwargs)


# --- Subclasses ---
class Gato(Mamifero):
    pass


class GatoAlbino(Albino, Mamifero):
    pass


class Ornintorrinco(Albino, Mamifero):
    pass


# --- Exemplo de uso ---
gato_normal = Gato(cor_pelo="Preto", nro_patas=4)
print(f"Gato Normal: {gato_normal} {gato_normal.miau_falar()}")


gato_albino = GatoAlbino(cor_pelo="Branco", nro_patas=4, albino=True)
print(f"Gato Albino: {gato_albino}")

ornintorrinco = Ornintorrinco(
    cor_pelo="Marrom", nro_patas=4, cor_bico="Amarelo", albino=False
)
print(f"Ornintorrinco: {ornintorrinco}")
