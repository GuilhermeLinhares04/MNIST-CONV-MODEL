from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import io

app = Flask(__name__)
model_cnn = load_model('pesos.h5')
model_linear = load_model('pesos_linear.h5')

# Função para preparar a imagem para ser usada no modelo
def prepare_image(image):
    if image.mode != 'L':
        image = image.convert('L')
    image = image.resize((28, 28))
    image = img_to_array(image)
    image = image.reshape((1, 28, 28, 1)).astype('float32') / 255
    return image

# Rota para prever o dígito usando o modelo CNN
@app.route('/predict_cnn', methods=['POST'])
def predict_cnn():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    prepared_image = prepare_image(image)
    prediction = model_cnn.predict(prepared_image)
    digit = np.argmax(prediction)

    return jsonify({'digit': int(digit)})

# Rota para prever o dígito usando o modelo linear
@app.route('/predict_linear', methods=['POST'])
def predict_linear():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read()))
    prepared_image = prepare_image(image)
    prediction = model_linear.predict(prepared_image)
    digit = np.argmax(prediction)

    return jsonify({'digit': int(digit)})

# Rota para a página inicial
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file provided', 400

        file = request.files['file']
        model_type = request.form['model_type']
        image = Image.open(io.BytesIO(file.read()))
        prepared_image = prepare_image(image)
        
        if model_type == 'cnn':
            prediction = model_cnn.predict(prepared_image)
        else:
            prediction = model_linear.predict(prepared_image)
            
        digit = np.argmax(prediction)
        
        return render_template('index.html', digit=digit, model_type=model_type)

    return render_template('index.html', digit=None, model_type=None)

if __name__ == '__main__':
    app.run(debug=True)
