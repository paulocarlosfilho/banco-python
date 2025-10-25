#!/bin/bash
# ===============================================================
# SCRIPT DE INICIALIZAÇÃO ROBUSTO COM POETRY
# 1. Garante que o Poetry esteja instalado.
# 2. Configura e inicia a aplicação.
# ===============================================================

PYTHON_SCRIPT="desafios/desafio_v1/desafio_v1.py"
POETRY_BIN="$HOME/.local/bin/poetry"

echo "--- 1. VERIFICANDO INSTALAÇÃO DO POETRY ---"

# Verifica se o executável do Poetry existe
if [ ! -f "$POETRY_BIN" ]; then
    echo "Poetry não encontrado. Instalando..."
    
    # Executando o curl para instalar o Poetry
    sudo apt update
    sudo apt install curl
    
    # Executa o instalador oficial do Poetry
    curl -sSL https://install.python-poetry.org | python3 -
    
    # O instalador do Poetry NÃO adiciona o binário ao PATH automaticamente.
    # É preciso recarregar o shell ou adicioná-lo manualmente.
fi

# Garante que o diretório do Poetry esteja no PATH para a sessão atual do script
export PATH="$HOME/.local/bin:$PATH"

# Verifica se o comando 'poetry' agora está disponível
if ! command -v poetry &> /dev/null
then
    echo "ERRO: A instalação do Poetry falhou ou o PATH não foi configurado corretamente."
    exit 1
fi

echo "--- 2. CONFIGURANDO AMBIENTE E DEPENDÊNCIAS (VIA POETRY) ---"

# Instala o projeto e todas as dependências do pyproject.toml
poetry install 

echo "--- 3. INICIANDO APLICAÇÃO PYTHON: $PYTHON_SCRIPT ---"
echo "---------------------------------------------------"

# Executa o script Python dentro do ambiente virtual isolado
poetry run python3 "$PYTHON_SCRIPT"

echo "--- Aplicação Encerrada. ---"