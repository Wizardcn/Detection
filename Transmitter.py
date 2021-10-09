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


def voltage_s(mi, E):
    """ pass array of mi to this function to transmit voltage s """
    # E = np.linspace(Ei, Ef, num=int(Ef / inc), endpoint=True)
    return np.power(-1, mi) * np.sqrt(E)


if __name__ == "__main__":
    print(voltage_s(generate_mi(0.5, 500000), 0.5).shape[0])
