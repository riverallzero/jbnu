import numpy as np
import pickle


def generate_random_dataset(d, N=1000, seed=42, filename='myrandomdataset'):
    if seed is not None:
        np.random.seed(seed)

    R = 10
    sigma = 0.1 * R
    w = np.random.uniform(-R, R, d)
    b = np.random.uniform(-R, R)

    x = np.random.uniform(-R, R, (N, d))
    y = np.random.normal(np.dot(x, w) + b, sigma, N)

    train_size = int(0.85 * N)
    dev_size = int(0.05 * N)
    test_size = int(0.1 * N)

    indices = np.arange(N)
    np.random.shuffle(indices)

    train_indices = indices[:train_size]
    dev_indices = indices[train_size:train_size + dev_size]
    test_indices = indices[train_size + dev_size:train_size + dev_size+test_size]

    train_data = (x[train_indices], y[train_indices])
    dev_data = (x[dev_indices], y[dev_indices])
    test_data = (x[test_indices], y[test_indices])

    dataset = {
        'train': train_data,
        'dev': dev_data,
        'test': test_data,
    }

    with open(f'{filename}.pkl', 'wb') as f:
        pickle.dump(dataset, f)


def main():
    generate_random_dataset(d=1, N=1000, seed=42)
    generate_random_dataset(d=1, N=10000, seed=42, filename='myrandomdataset-10000')
    generate_random_dataset(d=1, N=100000, seed=42, filename='myrandomdataset-100000')


if __name__ == '__main__':
    main()
