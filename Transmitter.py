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
    return mi


if __name__ == "__main__":
    print(generate_mi(0.5, 10))
