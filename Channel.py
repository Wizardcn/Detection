import numpy as np
import matplotlib.pyplot as plt


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
