from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model = load_model('pesos.h5')

# Função para preparar a imagem para ser usada no modelo
def prepare_image(image):
    if image.mode != 'L':
        image = image.convert('L')
    image = image.resize((28, 28))
    image = img_to_array(image)
    image = image.reshape((1, 28, 28, 1)).astype('float32') / 255
    return image

# Rota para fazer a predição
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    prepared_image = prepare_image(image)
    prediction = model.predict(prepared_image)
    digit = np.argmax(prediction)

    return jsonify({'digit': int(digit)})

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file provided', 400

        file = request.files['file']
        image = Image.open(io.BytesIO(file.read()))
        prepared_image = prepare_image(image)
        prediction = model.predict(prepared_image)
        digit = np.argmax(prediction)

        return render_template('index.html', digit=digit)

    return render_template('index.html', digit=None)

if __name__ == '__main__':
    app.run(debug=True)
