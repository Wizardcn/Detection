import numpy as np
import matplotlib.pyplot as plt
import Transmitter as transmit


def received_voltage(s_array, n_array):
    return s_array + n_array


def show_noise_pdf(noise_array):
    # noise = np.random.normal(mu, sigma, n)
    mu = np.mean(noise_array)
    sigma = np.var(noise_array)/10
    print("mu: ", mu)
    print("sigma: ", sigma)
    count, bins, ignored = plt.hist(noise_array, 30, density=True)

    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu)**2 / (2 * sigma**2)),
             linewidth=2, color='r')
    # plt.plot(np.sort(noise), 1/(sigma * np.sqrt(2 * np.pi)) *
    #          np.exp(- (np.sort(noise) - mu)**2 / (2 * sigma**2)),
    #          linewidth=2, color='r')
    plt.show()


if __name__ == "__main__":
    # noise = np.random.normal(0, 9, 100)
    # show_noise_pdf(noise)
    s = transmit.voltage_s(transmit.generate_mi(0.5, 500000), 0.1, 10, 0.1)
    n = np.random.normal(0, 9, s.shape[0])
    print(s)
    print(n)
    print(received_voltage(s, n))
    r1 = received_voltage(s, n)
    r2 = received_voltage(s, n)
    r3 = received_voltage(s, n)
    print("r1 = ", r1)
    print("r2 = ", r2)
    print("r3 = ", r3)
