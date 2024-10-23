import numpy as np


def numpy_quiz_1():
    """
    1.2.1	Consider a 16x16 array, how to get the block-sum (block size is 4x4)?
    """
    Z = np.ones((16, 16))
    k = 4
    S = np.add.reduceat(np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                        np.arange(0, Z.shape[1], k), axis=1)
    print(S)


def numpy_quiz_2():
    """
    1.2.2	Given an integer n and a 2D array X,
    select from X the rows which can be interpreted as draws from a multinomial distribution with n degrees,
    i.e., the rows which only contain integers and which sum to n.
    """
    X = np.asarray([[1.0, 0.0, 3.0, 8.0],
                    [2.0, 0.0, 1.0, 1.0],
                    [1.5, 2.5, 1.0, 0.0]])
    n = 4
    M = np.logical_and.reduce(np.mod(X, 1) == 0, axis=-1)
    M &= (X.sum(axis=-1) == n)

    print(X[M])


def numpy_quiz_3():
    """
    1.2.3   Considering 2 vectors A & B, write the einsum equivalent of inner, outer, sum, and mul function
    """
    a = [1, 2, 3]
    b = [4, 5, 6]

    ab_sum = np.einsum('i->', a)
    ab_mul = np.einsum('i,i->i', a, b)
    ab_inner = np.einsum('i,i', a, b)
    ab_outer = np.einsum('i,j->ij', a, b)

    print(f'sum => {ab_sum}\nmul => {ab_mul}\ninner => {ab_inner}\nouter => {ab_outer}')


def numpy_quiz_4():
    """
    1.2.4	Given a two dimensional array, how to extract unique rows?
    """
    Z = np.random.randint(0, 2, (3, 3))
    uZ = np.unique(Z, axis=0)

    print(uZ)


def numpy_quiz_5():
    """
    1.2.5	Given an arbitrary number of vectors, build the cartesian product (every combinations of every item)
    """

    def cartesian(arrays):
        arrays = [np.asarray(a) for a in arrays]
        shape = (len(x) for x in arrays)

        ix = np.indices(shape, dtype=int)
        ix = ix.reshape(len(arrays), -1).T

        for n, arr in enumerate(arrays):
            ix[:, n] = arrays[n][ix[:, n]]

        return ix

    print(cartesian(([1, 2, 3], [4, 5])))
