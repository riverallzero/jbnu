import numpy as np


def solver(A, b):
    A_pinv = np.linalg.pinv(A)
    x = np.dot(A_pinv, b)

    return x


def main():
    """
    Ax = b에서 Pseudo inverse를 이용하여 선형방정식의 근사해 (least squares solution) x를 구하시오
    A: 정방행렬이 아닌 일반행렬
    """
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([1, 0, 1])
    x = solver(A, b)

    print('x =', x)


if __name__ == '__main__':
    main()
