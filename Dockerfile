# Usa uma imagem base do Python como ponto de partida
FROM python:3.10

# Define o diretório de trabalho como /app
WORKDIR /app

# Copia o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código do projeto para o contêiner
COPY . .

# Expõe a porta 8000 do contêiner
EXPOSE 8000

# Comando para executar o servidor do Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]