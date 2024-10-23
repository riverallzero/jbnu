import numpy as np
import pickle
from sklearn import datasets


def load_local_dataset(filename):
    with open(filename, 'rb') as f:
        dataset = pickle.load(f)

    train_data = dataset['train']
    dev_data = dataset['dev']
    test_data = dataset['test']

    train_dataset = (np.array(train_data[0]), np.array(train_data[1]))
    dev_dataset = (np.array(dev_data[0]), np.array(dev_data[1]))
    test_dataset = (np.array(test_data[0]), np.array(test_data[1]))

    return train_dataset, dev_dataset, test_dataset


def predict(x, W, b):
    return np.dot(x, W) + b


def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def StochasticGradientDescent(X_train, y_train, X_dev, y_dev, X_test, y_test, learning_rate=0.001, epochs=100, m=10, early_stopping_patience=10):
    num_samples, num_features = X_train.shape
    W = np.zeros((num_features, 1))
    b = 0

    best_mse = float('inf')
    patience_counter = 0

    for epoch in range(epochs):
        for i in range(0, num_samples, m):
            end = i + m if i + m < num_samples else num_samples
            batch_X = X_train[i:end]
            batch_y = y_train[i:end].reshape(-1, 1)

            pred_y = predict(batch_X, W, b)
            error = pred_y - batch_y

            W_gradient = np.dot(batch_X.T, error) / m
            b_gradient = np.sum(error) / m

            W -= learning_rate * W_gradient
            b -= learning_rate * b_gradient

        pred_train_y = predict(X_train, W, b)
        pred_dev_y = predict(X_dev, W, b)
        pred_test_y = predict(X_test, W, b)

        train_mse = mean_squared_error(y_train, pred_train_y)
        dev_mse = mean_squared_error(y_dev, pred_dev_y)
        test_mse = mean_squared_error(y_test, pred_test_y)

        if dev_mse < best_mse:
            best_mse = dev_mse
            patience_counter = 0
        else:
            patience_counter += 1

        print(f'Epoch {epoch + 1}/{epochs} | MSE Train={train_mse:.4f}, Dev={dev_mse:.4f}, Test={test_mse:.4f}')

        if patience_counter == early_stopping_patience:
            print('Early stopping triggered')
            break

    return W, b


def main():
    # ============================================================================
    # HYPER-PARAMETER
    # ============================================================================
    learning_rate = 0.001
    epochs = 100
    m = 10
    early_stopping_patience = 10

    # ============================================================================
    # 1. Random Data Local File
    # ============================================================================
    print('1. Random Data Local File')
    train_dataset, dev_dataset, test_dataset = load_local_dataset('myrandomdataset.pkl')

    X_train, y_train = train_dataset
    X_dev, y_dev = dev_dataset
    X_test, y_test = test_dataset

    W, b = StochasticGradientDescent(X_train, y_train, X_dev, y_dev, X_test, y_test, learning_rate, epochs, m, early_stopping_patience)

    print(f'=> Final weights: {W.ravel()}')
    print(f'=> Final bias: {b}\n')

    pred_test_y = predict(X_test, W, b)
    test_mse = mean_squared_error(y_test, pred_test_y)
    print(f'=> Final TestSet MSE={test_mse:.4f}\n')

    # ============================================================================
    # 2. Scikit Sample Data
    # ============================================================================
    print('2. Scikit Sample Data')
    diabetes = datasets.load_diabetes()
    X = diabetes.data
    y = diabetes.target

    train_size = int(0.85 * len(y))
    dev_size = int(0.05 * len(y))
    test_size = int(0.1 * len(y))

    indices = np.arange(len(y))
    np.random.shuffle(indices)

    train_indices = indices[:train_size]
    dev_indices = indices[train_size:train_size + dev_size]
    test_indices = indices[train_size + dev_size:train_size + dev_size + test_size]

    X_train, y_train = (X[train_indices], y[train_indices])
    X_dev, y_dev = (X[dev_indices], y[dev_indices])
    X_test, y_test = (X[test_indices], y[test_indices])

    W, b = StochasticGradientDescent(X_train, y_train, X_dev, y_dev, X_test, y_test, learning_rate, epochs, m, early_stopping_patience)

    print(f'=> Final weights: {W.ravel()}')
    print(f'=> Final bias: {b}\n')

    pred_test_y = predict(X_test, W, b)
    test_mse = mean_squared_error(y_test, pred_test_y)
    print(f'=> Final TestSet MSE={test_mse:.4f}')


if __name__ == '__main__':
    main()
