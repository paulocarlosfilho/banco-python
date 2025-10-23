from pathlib import Path
import chardet



ROOT_PATH = Path(__file__).parent

# Boa prática: Usar 'with' para abrir arquivos, garantindo que sejam fechados corretamente
try:
    with open(ROOT_PATH / "arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except IOError as e:
    print(f"Erro ao abrir o arquivo: {e}")



# Procure sempre usar o encoding adequado ao abrir arquivos de texto
try:
    with open(ROOT_PATH / "arquivo_utf8.txt", "w", encoding="utf-8") as arquivo:
        conteudo = arquivo.write("Aprendendo a manipular arquivos com boas práticas utilizando python.")
        print(conteudo)
except IOError as e:
    print(f"Erro ao abrir o arquivo: {e}")


#UnicodeDecodeError
try:
    with open(ROOT_PATH / "arquivo_utf8.txt", "r", encoding="ascii") as arquivo:
        print(arquivo.read())
except IOError as e:
    print(f"Erro ao abrir o arquivo: {e}")
except UnicodeDecodeError as e:
    print(f"Erro de decodificação: {e}")




# Boa prática: Detectar o encoding de um arquivo quando não se tem certeza do seu encoding
def detectar_encoding(caminho_arquivo: Path):
    """Lê os primeiros bytes de um arquivo para detectar o encoding."""

    # 1. Lê os primeiros 10.000 bytes (geralmente suficiente para detectar)
    with open(caminho_arquivo, 'rb') as f: # Abrir em modo binário ('rb') é crucial!
        dados_brutos = f.read(10000)

    # 2. Usa o algoritmo Chardet
    resultado = chardet.detect(dados_brutos)

    # 3. Exibe o resultado
    print(f"--- Resultado da Detecção ---")
    print(f"Encoding Detectado: {resultado['encoding']}")
    print(f"Confiança (0.0 a 1.0): {resultado['confidence']:.2f}")
    print("-" * 25)

    return resultado['encoding']
# --- Exemplo de Uso ---
# Supondo que você criou o arquivo_utf8.txt no passo anterior
ROOT_PATH = Path(__file__).parent
# Tenta detectar o arquivo que criamos como UTF-8
arquivo_para_testar = ROOT_PATH / "arquivo_utf8.txt"
if arquivo_para_testar.exists():
    detectar_encoding(arquivo_para_testar)
else:
    print(f"Erro: Arquivo '{arquivo_para_testar.name}' não encontrado para teste.")

