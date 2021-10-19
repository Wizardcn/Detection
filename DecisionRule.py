from math import *
import numpy as np

# m1 = 1 -> s < 0 -> mhat = 1
# m0 = 0 -> s > 0 -> mhat = 0

# Optimal Decision Rule


def ODR(Pm0, E, r1, r2, r3, var1, var2, var3):
    """ optimum decision rule for jointly statistically independent """
    TH = (1 / (2 * sqrt(E))) * log((1-Pm0)/Pm0)

    l = sum([r/variance
             for r, variance in zip([r1, r2, r3], [var1, var2, var3])])
    if l >= TH:
        mhat = 0
    elif l < TH:
        mhat = 1
    return mhat


def ABR(r1, r2, r3):
    l = r1+r2+r3
    if l >= 0:
        mhat = 0
    else:
        mhat = 1
    return mhat


def ODR_NOT(Pm0, E, r1, r2, r3, cov_matrix):
    TH = 2 * log((1-Pm0)/Pm0)
    inv_cov_matrix = np.linalg.inv(cov_matrix)
    vector_r = np.array([[r1], [r2], [r3]])
    vector_r_bar_m1 = [[- sqrt(E)], [- sqrt(E)], [- sqrt(E)]]
    vector_r_bar_m0 = [[sqrt(E)], [sqrt(E)], [sqrt(E)]]
    l = np.matmul(np.matmul((vector_r - vector_r_bar_m1).T, inv_cov_matrix), (vector_r - vector_r_bar_m1)) - \
        np.matmul(np.matmul((vector_r - vector_r_bar_m0).T,
                  inv_cov_matrix), (vector_r - vector_r_bar_m0))
    if l >= TH:
        mhat = 0
    elif l < TH:
        mhat = 1
    return mhat


if __name__ == "__main__":
    # test
    cov_matrix = np.array([[11.94950449, 5.70834037,  15.57133404],
                           [5.70834037, 17.93141068, 15.29760843],
                           [15.57133404, 15.29760843, 55.07355794]])

    print(ODR_NOT(0.5, 0.1, 50, 10, -30, cov_matrix))
