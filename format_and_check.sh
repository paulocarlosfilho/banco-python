#!/bin/bash
# Script de automação de qualidade de código (Isort, Black, Flake8)

# Verifica se um nome de arquivo foi passado como argumento
if [ -z "$1" ]; then
    echo "Uso: ./format_and_check.sh"
    exit 1
fi

ARQUIVO="$1"

echo "--- 1. ORGANIZANDO IMPORTS com ISORT em $ARQUIVO ---"
poetry run isort "$ARQUIVO"

echo "--- 2. FORMATANDO CÓDIGO com BLACK em $ARQUIVO ---"
poetry run black "$ARQUIVO"

echo "--- 3. VERIFICANDO A QUALIDADE com FLAKE8 em $ARQUIVO ---"
poetry run flake8 "$ARQUIVO"

echo "--- LIMPEZA DE CÓDIGO CONCLUÍDA! ---"



# pip inastall flake8 black isort

# flake8 --max-line-length=120 nomedoarquivo.py
# black -l 120 nomedoarquivo.py
# isort nomedoarquivo.py