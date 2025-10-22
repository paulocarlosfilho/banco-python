import pickle
import os # Módulo para verificar a existência do arquivo

# 1. Objeto Python que queremos armazenar (serializar)
dados_do_banco = {
    "contas_ativas": [
        {"agencia": "0001", "numero": 1, "saldo": 1500.00},
        {"agencia": "0001", "numero": 2, "saldo": 500.00}
    ],
    "ultima_transacao": "22-10-2025"
}

nome_arquivo_binario = "dados_banco.bin"

# --------------------------
# PARTE 1: ESCREVER O ARQUIVO BINÁRIO (Serialização)
# --------------------------
print(f"1. Gravando dados no arquivo binário: {nome_arquivo_binario}")

# O modo 'wb' significa 'write binary' (escrever binário)
with open(nome_arquivo_binario, 'wb') as arquivo:
    # pickle.dump() transforma o objeto Python em uma sequência de bytes e a escreve no arquivo
    pickle.dump(dados_do_banco, arquivo)
    
print("   -> Gravação concluída. O arquivo é binário e não legível por humanos.")


# --------------------------
# PARTE 2: LER O ARQUIVO BINÁRIO (Desserialização)
# --------------------------
if os.path.exists(nome_arquivo_binario):
    print(f"\n2. Lendo dados do arquivo binário: {nome_arquivo_binario}")

    # O modo 'rb' significa 'read binary' (ler binário)
    with open(nome_arquivo_binario, 'rb') as arquivo:
        # pickle.load() lê a sequência de bytes e reconstrói o objeto Python
        dados_recuperados = pickle.load(arquivo)

    print("   -> Dados recuperados com sucesso!")
    print("\n   Conteúdo original do objeto Python:")
    print(f"   Contas: {dados_recuperados['contas_ativas']}")
    print(f"   Última Data: {dados_recuperados['ultima_transacao']}")
    
else:
    print(f"O arquivo {nome_arquivo_binario} não foi encontrado.")

# --------------------------
# PARTE 3: LIMPEZA (Opcional)
# --------------------------
# os.remove(nome_arquivo_binario)
# print(f"\n3. Arquivo {nome_arquivo_binario} removido.")



#Pegando o arquivo acima
nome_arquivo_binario = "dados_banco.bin"

# O modo 'rb' é essencial para ler arquivos binários
with open(nome_arquivo_binario, 'rb') as arquivo:
    # pickle.load() lê os bytes e reconstrói o dicionário
    dados_recuperados = pickle.load(arquivo)

print("Dados recuperados do arquivo binário:")
print(dados_recuperados)
print(type(dados_recuperados))