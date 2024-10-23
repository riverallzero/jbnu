import numpy as np


class MLP:
    def __init__(self, layers):
        self.layers = layers
        self.weights = []
        self.biases = []
        self._initialize_weights()

    def _initialize_weights(self):
        for i in range(len(self.layers) - 1):
            self.weights.append(np.random.randn(self.layers[i], self.layers[i + 1]) * 0.01)
            self.biases.append(np.zeros((1, self.layers[i + 1])))

    def forward(self, X):
        self.z = []
        self.a = [X]
        for i in range(len(self.weights)):
            self.z.append(np.dot(self.a[-1], self.weights[i]) + self.biases[i])
            self.a.append(self._relu(self.z[-1]))
        return self.a[-1]

    def _relu(self, x):
        return np.maximum(0, x)

    def _relu_derivative(self, x):
        return (x > 0) * 1

    def backward(self, X, y, learning_rate):
        m = X.shape[0]
        dz = self.a[-1] - y  # Output layer error
        for i in reversed(range(len(self.weights))):
            dw = np.dot(self.a[i].T, dz) / m
            db = np.sum(dz, axis=0, keepdims=True) / m
            self.weights[i] -= learning_rate * dw
            self.biases[i] -= learning_rate * db
            if i > 0:  # Skip update for input layer
                dz = np.dot(dz, self.weights[i].T) * self._relu_derivative(self.z[i - 1])

    def fit(self, X_train, y_train, X_dev, y_dev, X_test, y_test, epochs, m, learning_rate, early_stopping_patience):
        best_weights = self.weights
        best_biases = self.biases
        best_dev_acc = 0
        patience = 0

        for epoch in range(epochs):
            permutation = np.random.permutation(X_train.shape[0])
            X_train = X_train[permutation]
            y_train = y_train[permutation]

            for i in range(0, X_train.shape[0], m):
                X_batch = X_train[i:i + m]
                y_batch = y_train[i:i + m]
                self.forward(X_batch)
                self.backward(X_batch, y_batch, learning_rate)

            train_predictions = self.predict(X_train)
            dev_predictions = self.predict(X_dev)
            test_predictions = self.predict(X_test)
            train_acc = accuracy_metric(np.argmax(y_train, axis=1), train_predictions)
            dev_acc = accuracy_metric(np.argmax(y_dev, axis=1), dev_predictions)
            test_acc = accuracy_metric(np.argmax(y_test, axis=1), test_predictions)

            print(f'Epoch {epoch + 1}/{epochs} | ACC Train={train_acc:.4f}, Dev={dev_acc:.4f}, Test={test_acc:.4f}')

            if dev_acc > best_dev_acc:
                best_dev_acc = dev_acc
                best_weights = self.weights
                best_biases = self.biases
                patience = 0
            else:
                patience += 1

            if patience == early_stopping_patience:
                print('Early stopping triggered')
                break

        self.weights = best_weights
        self.biases = best_biases

    def predict(self, X):
        a = self.forward(X)
        return np.argmax(a, axis=1)
      
