class Estudante:

    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Matrícula: {self.matricula} Escola {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Ana", 1)
aluno_2 = Estudante("Bruno", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"

aluno_3 = Estudante("Carla", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
