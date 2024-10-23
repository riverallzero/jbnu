import numpy as np


def solver(A, b):
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)

    return x


def main():
    """
    Ax = b에서 선형방정식에서 해 x를 구하시오
    A: 정방행렬
    """
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    x = solver(A, b)

    print('x =', x)


if __name__ == '__main__':
    main()
