from Channel import *
from DecisionRule import *
from Detection import *
from Transmitter import *
import matplotlib.pyplot as plt


def main():
    t1 = time.time()
    # find probability of error
    mi_array = generate_mi(0.5, 500)
    E = np.linspace(0.1, 10, num=100, endpoint=True)
    prob_of_error_array = []
    for e in E:
        s = voltage_s(mi_array, e)
        r1 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
        r2 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
        r3 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
        mhat_array = detection(Pm0=0.5, E=e, r1=r1, r2=r2,
                               r3=r3, var1=9, var2=9, var3=9)
        prob_of_error_array.append(prob_of_error(mi_array, mhat_array))
    prob_of_error_array = np.array(prob_of_error_array)
    print(prob_of_error_array)
    print(E)

    # vitualize data
    figure, axis1 = plt.subplots(figsize=(8, 4))
    axis1.set_yscale('log')
    axis1.plot(E, prob_of_error_array)
    axis1.set_xlabel('Signal energy')
    axis1.set_ylabel('probability of Error')
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.tight_layout()
    # plt.savefig(f'./figure/{filename[10:][:-4]}-freq.png')
    plt.show()
    t2 = time.time() - t1
    print(f'Executed in {t2:0.2f} seconds.')


if __name__ == '__main__':
    main()
