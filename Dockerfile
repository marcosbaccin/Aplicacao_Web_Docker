# Use uma imagem base adequada para o seu aplicativo web
FROM python:3.9

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos de requisitos do projeto e instale as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do aplicativo
COPY . .

# Exponha a porta que o aplicativo irá ouvir
EXPOSE 5000

# Defina o comando para iniciar o servidor do aplicativo
CMD ["python", "app.py"]
