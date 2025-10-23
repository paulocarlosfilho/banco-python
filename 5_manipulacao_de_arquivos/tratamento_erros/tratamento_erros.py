from pathlib import Path




#FileNotFoundError
try: 
    arquivo = open("meu_arquivo.txt")
except FileNotFoundError as e:
    print("Arquivo não encontrado. Verifique o nome do arquivo e tente novamente.")
    print()
    print(f"Detalhes do erro: {e}")
    (print())
else:
    conteudo = arquivo.read()
    print(conteudo)
    arquivo.close()
finally:
    print("Execução do bloco try-except-finally concluída.")






#Tentando abrir uma pasta como se fosse um arquivo
ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo-diretorio.py")
except FileNotFoundError as e:
    print(f"1 - Arquivo não encontrado: {e}")
except IsADirectoryError as e:
    print(f"2 - Não foi possível abrir o o arquivo: {e}")
except IOError as e:
    print(f"3 - Erro ao abrir o arquivo {e}")
except Exception as e:
    print(f"4 - Alguma coisa ocorreu ao tentar abrir o arquivo. {e}")
else:
    arquivo.close()