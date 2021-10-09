from math import sqrt
import numpy as np
import random


def generate_mi(Pm0, n):
    """ input message generator function """
    mi = []
    m0 = 0  # m0 counter
    m1 = 0  # m1 counter
    for i in range(n):
        if random.uniform(0, 1) < Pm0:
            mi.append(0)
            m0 += 1
        else:
            mi.append(1)
            m1 += 1
    return np.array(mi)


def voltage_s(mi, Ei, Ef, inc):
    """ pass array of mi to this function to transmit voltage s """
    E = np.linspace(Ei, Ef, num=int(Ef / inc), endpoint=True)
    length = min(E.shape[0], mi.shape[0])
    return np.power(-1, mi)[:length] * np.sqrt(E)[:length]


if __name__ == "__main__":
    print(voltage_s(generate_mi(0.5, 500000), 0.1, 10, 0.1))
