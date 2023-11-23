import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(input_size + 1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        return self.activation(summation)

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)
# Échantillons A
samples_A = {
    "inputs": np.array([[0.1, 0.2], [0.8, 0.9], [0.7, 0.3]]),
    "labels": np.array([1, 1, 0])
}

# Échantillons B
samples_B = {
    "inputs": np.array([[0.1, 0.2], [0.8, 0.9], [0.7, 0.3], [0.3, 0.6]]),
    "labels": np.array([1, 1, 0, 0])
}

# Échantillons C
samples_C = {
    "inputs": np.array([[0.1, 0.2], [0.8, 0.9], [0.7, 0.3], [0.8, 0.1], [0.7, 0.6], [0.2, 0.5]]),
    "labels": np.array([1, 1, 0, 0, 1, 1])
}

# Échantillons logiques
samples_logic = {
    "AND": {
        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        "labels": np.array([0, 0, 0, 1])
    },
    "OR": {
        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        "labels": np.array([0, 1, 1, 1])
    },
    "XOR": {
        "inputs": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
        "labels": np.array([0, 1, 1, 0])
    }
}

# Fonction pour entraîner et tester un perceptron avec un ensemble de données
def train_and_test_perceptron(samples):
    inputs = samples["inputs"]
    labels = samples["labels"]

    perceptron = Perceptron(input_size=2)
    perceptron.train(inputs, labels)

    print("Prédictions:")
    for i, input_data in enumerate(inputs):
        prediction = perceptron.predict(input_data)
        print(f"Input: {input_data} - Prédiction: {prediction} - Réel: {labels[i]}")

# Entraînement et test avec les échantillons A, B, C et les opérations logiques
print("Échantillons A:")
train_and_test_perceptron(samples_A)

print("\nÉchantillons B:")
train_and_test_perceptron(samples_B)

print("\nÉchantillons C:")
train_and_test_perceptron(samples_C)

print("\nÉchantillons logiques:")
for logic_gate, data in samples_logic.items():
    print(f"\n{logic_gate}:")
    train_and_test_perceptron(data)
