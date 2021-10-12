from math import *

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


def ODR_NOT():
    pass


if __name__ == "__main__":
    # test
    ODR(0.5, 0.1, 5, 10, -3, 9, 9, 9)
