# MNIST-CONV-MODEL

Este projeto representa uma rede de modelo convolucional para classificação de dígitos manuscritos do dataset MNIST. Para realizar a classificação, foi utilizado o framework TensorFlow com um servidor em Flask para servir a aplicação.

## Estrutura do projeto

O projeto está dividido em duas partes: a primeira é a criação do modelo de classificação, que está no arquivo `model_trainment.py`, e a segunda é a criação do servidor Flask, que está no arquivo `app.py`.

## Executando o projeto

Para executar o projeto, é necessário ter o Python instalado na máquina. Com o Python instalado, basta clonar este repositório e executar o comando `pip install -r requirements.txt` para instalar as dependências do projeto. Após a instalação das dependências, basta executar o comando `python app.py` para iniciar o servidor Flask. Com o servidor iniciado, basta acessar o endereço `http://127.0.0.1:5000` para acessar a aplicação.

## Rotas API

A aplicação possui duas rotas:

- `/predict` - Rota que recebe uma imagem e retorna a classificação da imagem.
- `/` - Rota principal da aplicação, que abre a página onde é possível fazer o upload de uma imagem para classificação.

## Vídeo de demonstração

Para ver um vídeo de demonstração da aplicação, acesse [este link](https://www.youtube.com/watch?v=3QJz1J7J1Zo)