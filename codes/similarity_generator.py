import numpy as np

np.set_printoptions(suppress=True, linewidth=150, precision=3)


def pre_process(x, nfc):

    """
    :param x: numpy array, entity-to-feature matrix
    :param nfc:  Dict, the keys show column of categorical variable in X,
        while values demonstrates the number of subcategories in that categorical variable
    :return: numpy array, y, Pre-processed entity-to-feature matrix.
    """

    cv = np.mean(x, axis=0)
    rv = np.ptp(x, axis=0)
    y = np.divide(np.subtract(x, cv), rv)

    if nfc is not None:
        for k, v in nfc.items():
            y[:, int(k)] = np.divide(y[:, int(k)], np.sqrt(v))

    return y


def inner_product(y):

    """
    :param y: numpy array, pre-processed entity-to-feature matrix
    :return: inner-product similarity
    """
    n, v = y.shape
    sim = np.zeros([n, n])

    for i in range(n):
        for j in range(n):
            if i != j:
                sim[i, j] = np.dot(y[i, :], y[j, :])
    return sim


def kernel_trick(y, m):

    """
    :param y: numpy array, pre-processed entity-to-feature matrix
    :param m: Number of features
    :return: affinity data derived by kernel trick
    """

    n, v = y.shape
    aff = np.zeros([n, n])

    for i in range(n):
        for j in range(n):
            if i != j:
                aff[i, j] = np.exp((np.sum(np.power(np.subtract(y[i, :], y[j, :]), 2))) / (m/18))

    return aff


def generate_similarities(y,):

    n, v = y.shape
    y_inn = inner_product(y=y)  # inner product
    y_aff = kernel_trick(y=y, m=v)  # Kernel trick

    return y_inn, y_aff
