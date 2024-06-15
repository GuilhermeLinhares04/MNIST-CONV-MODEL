from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical
import time

# Carrega o dataset MNIST
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((60000, 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Defini o modelo
model = Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compila o modelo
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Treina o modelo
start_time = time.time()
history = model.fit(train_images, train_labels, epochs=100, batch_size=64, validation_split=0.2)
training_time = time.time() - start_time

# Avalia o modelo
test_loss, test_accuracy = model.evaluate(test_images, test_labels)

# Salva os pesos
model.save('pesos_linear.h5')

print(f"Tempo de treinamento: {training_time:.2f} segundos")
print(f"Acurácia no teste: {test_accuracy:.4f}")
