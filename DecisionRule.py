from math import *

# m1 = 0
# m0 = 1


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


def ODR(Pm0, E, r1, r2, r3, var1, var2, var3):
    TH = (1 / (2 * sqrt(E))) * log((1-Pm0)/Pm0)
    l = r1+r2+r3

    if l >= TH:
        mhat = 0
    elif l < TH:
        mhat = 1
    return mhat


if __name__ == "__main__":
    ODR(0.5, 0.1, 5, 10, -3, 9, 9, 9)
