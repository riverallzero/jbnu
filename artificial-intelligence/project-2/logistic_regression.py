import numpy as np


def initialize_parameters(input_dim, output_dim):
    W = np.random.randn(input_dim, output_dim) * 0.01
    b = np.zeros((1, output_dim))
    return W, b


def softmax(z):
    exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)


def cross_entropy_loss(y_true, y_pred):
    return -np.mean(np.sum(y_true * np.log(y_pred + 1e-8), axis=1))


def one_hot_encoding(y, num_classes):
    return np.eye(num_classes)[y]


def predict(x, W, b):
    z = np.dot(x, W) + b
    return softmax(z)


def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual))


def StochasticGradientDescent(X_train, y_train, X_dev, y_dev, X_test, y_test, learning_rate=0.001, epochs=100, m=10, early_stopping_patience=10):
    input_dim, output_dim = X_train.shape[1], y_train.shape[1]
    W, b = initialize_parameters(input_dim, output_dim)

    best_loss = float('inf')
    patience_counter = 0

    for epoch in range(epochs):
        for i in range(0, X_train.shape[0], m):
            batch_X = X_train[i:i + m]
            batch_y = y_train[i:i + m]

            pred_y = predict(batch_X, W, b)

            dW = np.dot(batch_X.T, (pred_y - batch_y)) / m
            db = np.sum(pred_y - batch_y, axis=0, keepdims=True) / m

            W -= learning_rate * dW
            b -= learning_rate * db

        dev_pred_y = predict(X_dev, W, b)
        dev_loss = cross_entropy_loss(y_dev, dev_pred_y)

        if dev_loss < best_loss:
            best_loss = dev_loss
            patience_counter = 0
        else:
            patience_counter += 1

        if patience_counter >= early_stopping_patience:
            print('Early stopping triggered')
            break

        train_pred_y = predict(X_train, W, b)
        train_acc = accuracy_metric(np.argmax(y_train, axis=1), np.argmax(train_pred_y, axis=1))
        dev_acc = accuracy_metric(np.argmax(y_dev, axis=1), np.argmax(dev_pred_y, axis=1))
        test_pred_y = predict(X_test, W, b)
        test_acc = accuracy_metric(np.argmax(y_test, axis=1), np.argmax(test_pred_y, axis=1))

        print(f'Epoch {epoch + 1}/{epochs} | ACC Train={train_acc:.4f}, Dev={dev_acc:.4f}, Test={test_acc:.4f}')

    return W, b