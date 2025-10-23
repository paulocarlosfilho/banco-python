import csv
from pathlib import Path


#Criar o arquivo - Lembre sempre de mudar o nome. csv.py da erro.
ROOT_PATH = Path(__file__).parent
try:
    with open(ROOT_PATH / 'usuarios.csv', mode='w', newline='', encoding='utf-8') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida)
        escritor_csv.writerow(['Id', 'Nome', 'Idade', 'Cidade'])
        escritor_csv.writerow(['1', 'Alice', 30, 'São Paulo'])
        escritor_csv.writerow(['2', 'Bob', 25, 'Rio de Janeiro'])
except IOError as e:
    print(f"Erro ao escrever no arquivo CSV: {e}")




# Ler o arquivo em csv
try:
    with open(ROOT_PATH / 'usuarios.csv', mode='r', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except csv.Error as e:
    print(f"Erro ao ler o arquivo CSV: {e}")



# Forma de ler com o DictReader
try:
    with open(ROOT_PATH / 'usuarios.csv', newline='', encoding='utf-8') as arquivo_csv:
        dict_reader = csv.DictReader(arquivo_csv)
        for row in dict_reader:
            print(f"Nome: {row['Nome']}")
            print(f"Cidade: {row['Cidade']}")
            print(30 * "=")
except FileNotFoundError:
    print("Erro: O arquivo names.csv não foi encontrado.")
except csv.Error as e:
    print(f"Erro ao ler o arquivo CSV: {e}")