# MNIST-CONV-MODEL

Este projeto apresenta um modelo de rede neural convolucional (CNN) e um modelo linear para classificação de dígitos manuscritos do dataset MNIST. Para realizar a classificação, foi utilizado o framework TensorFlow com um servidor em Flask para servir a aplicação.

## Estrutura do projeto

O projeto está dividido em duas partes: a primeira é a criação dos modelos de classificação, sendo o arquivo `cnn_trainment.py` o código que cria e treina o modelo CNN, e o arquivo `linear_trainment`o que cria e treina o modelo linear. A segunda parte é a criação do servidor Flask, que está no arquivo `app.py`, e a página HTML `index.html` que permite o upload de uma imagem e a escolha do modelo para fazer a predição. <br>

Além disso, o projeto conta com o arquivo `requirements.txt` que contém as dependências do projeto, e a pasta `other_models` que contém outros modelos CNN treinados com épocas diferentes.

## Executando o projeto

Para executar o projeto, é necessário ter o Python instalado na máquina. Com o Python instalado, basta clonar este repositório e executar o comando `pip install -r requirements.txt` para instalar as dependências do projeto. Após a instalação das dependências, basta executar o comando `python app.py` para iniciar o servidor Flask. Com o servidor iniciado, basta acessar o endereço `http://127.0.0.1:5000` para acessar a aplicação.

## Documentação API

### Rota /predict_cnn

- **Descrição**: Prediz o dígito de uma imagem usando o modelo convolucional.
- **Método**: POST
- **Parâmetros**:
  - `file`: Arquivo de imagem.
- **Retorno**: JSON com o dígito previsto.

### Rota /predict_linear

- **Descrição**: Prediz o dígito de uma imagem usando o modelo linear.
- **Método**: POST
- **Parâmetros**:
  - `file`: Arquivo de imagem.
- **Retorno**: JSON com o dígito previsto.

### Rota /

- **Descrição**: Página HTML para upload de uma imagem e escolha do modelo.
- **Método**: GET, POST
- **Parâmetros** (POST):
  - `file`: Arquivo de imagem.
  - `model_type`: Tipo de modelo (`cnn` ou `linear`).
- **Retorno**: Página HTML com o dígito previsto.

## Comparação entre os modelos

O modelo convolucional obteve uma acurácia de 99,92% no dataset sendo treinado com 100 épocas em aproximadamente 23 minutos, enquanto o modelo linear obteve uma acurácia de 97,82% com o mesmo número de épocas e foi treinado em aproximadamente 7 minutos. 

A diferença de acurácia entre os modelos se deve ao fato de que o modelo convolucional é capaz de capturar padrões espaciais nas imagens, enquanto o modelo linear não é capaz de fazer isso. Já a diferença de tempo de treinamento se deve ao fato de que o modelo convolucional é mais complexo e possui mais parâmetros do que o modelo linear.

Por fim, com relação ao tempo de inferência, que é o tempo que o modelo leva para fazer a predição de uma imagem, o modelo linear é mais rápido do que o modelo convolucional, pois possui menos parâmetros e operações a serem realizadas. Já o tempo de inferência do modelo convolucional é consequentemente mais lento do que o modelo linear, pois possui mais camadas e operações a serem realizadas.

## Vídeo de demonstração

Para ver um vídeo de demonstração da aplicação, acesse [este link](https://youtu.be/jop9_6xGU2A)