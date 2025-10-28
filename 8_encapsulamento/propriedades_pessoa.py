from datetime import date


class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        ano_atual = date.today().year
        return ano_atual - self._ano_nascimento


pessoa = Pessoa("Ana", 1993)

print(f"Nome :{pessoa.nome} \nIdade: {pessoa.idade}")
