#!/bin/bash

# Configurações
set -e  # Encerra o script em caso de erro

echo -e "\n=== INICIANDO DEPLOY AUTOMÁTICO ===\n"

# 1. Verifica Node.js e Serverless
echo "Verificando dependências..."
if ! command -v node &> /dev/null || ! command -v serverless &> /dev/null; then
    echo "Erro: Node.js ou Serverless Framework não instalados." >&2
    exit 1
fi

# 2. Instala dependências Python
echo "Instalando dependências Python..."
pip install -r deps.txt

# 3. Configura AWS (opcional - use GitHub Secrets)
# export AWS_ACCESS_KEY_ID="SUA_ACCESS_KEY"
# export AWS_SECRET_ACCESS_KEY="SUA_SECRET_KEY"

# 4. Executa o deploy
echo -e "\nIniciando deploy com Serverless Framework..."
serverless deploy --stage prod --verbose || {
    echo "Erro durante o deploy" >&2
    exit 1
}

echo -e "\n=== DEPLOY CONCLUÍDO COM SUCESSO! ===\n"