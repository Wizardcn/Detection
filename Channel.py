import numpy as np
import matplotlib.pyplot as plt
import Transmitter as transmit


def generate_noise(variance, n):
    return np.random.normal(0, np.sqrt(variance), n)


def received_voltage(s_array, variance):
    r_array = []
    for s in s_array:
        r = s + np.random.normal(0, np.sqrt(variance))
        r_array.append(r)
    return np.array(r_array)


def show_pdf(rv):
    # noise = np.random.normal(mu, sigma, n)
    mu = np.mean(rv)
    sigma = np.sqrt(np.var(rv))
    # print("mu: ", mu)
    # print("sigma: ", sigma)
    count, bins, ignored = plt.hist(rv, 30, density=True)

    # plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
    #          np.exp(- (bins - mu)**2 / (2 * sigma**2)),
    #          linewidth=2, color='r')
    # plt.plot(np.sort(noise), 1/(sigma * np.sqrt(2 * np.pi)) *
    #          np.exp(- (np.sort(noise) - mu)**2 / (2 * sigma**2)),
    #          linewidth=2, color='r')
    plt.show()


if __name__ == "__main__":
    # s = transmit.voltage_s(transmit.generate_mi(0.5, 50), 0.1)
    # n = np.random.normal(0, 9, s.shape[0])
    # print(s)
    # print(n)
    # print(received_voltage(s, n))
    # r1 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    # r2 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    # r3 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    # print("r1 = ", r1)
    # print("r2 = ", r2)
    # print("r3 = ", r3)
    # print(r1.shape[0])
    # print(r2.shape[0])
    # print(r3.shape[0])
    mi_array = transmit.generate_mi(0.5, 5000)
    E = 9
    Pm0 = 0.5
    var1 = 1
    var2 = 1
    var3 = 1
    s = transmit.voltage_s(mi_array, E)

    r1 = received_voltage(s, var1)

    show_pdf(r1)
