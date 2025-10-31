from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Class Method
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        hoje = date.today()
        idade = hoje.year - ano - ((hoje.month, hoje.day) < (mes, dia))
        return cls(nome, idade)

    # Static Method
    @staticmethod
    def e_maior_de_idade(idade):
        return idade >= 18


pessoa = Pessoa.criar_de_data_nascimento(1993, 8, 19, "João")

print(f"{pessoa.nome} - {pessoa.idade}")


if (Pessoa.e_maior_de_idade(pessoa.idade)) is False:
    print(f"{pessoa.nome} é menor de idade.")

else:
    print(f"{pessoa.nome} é Maior de idade.")
