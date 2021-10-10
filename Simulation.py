from Channel import *
from DecisionRule import *
from Detection import *
from Transmitter import *
import matplotlib.pyplot as plt


def simulation(Pm0, var1, var2, var3, n):

    t1 = time.time()
    # find probability of error
    # -------------- can modify ----------------------
    # Pm0 = 0.5
    # var1 = 9
    # var2 = 9
    # var3 = 9
    # mi_array = generate_mi(Pm0, 50)
    # -------------------------------------------------
    mi_array = generate_mi(Pm0, n)
    E = np.linspace(0.1, 10, num=100, endpoint=True)
    prob_of_error_array = []
    for e in E:
        s = voltage_s(mi_array, e)
        r1 = received_voltage(s, var1)
        r2 = received_voltage(s, var2)
        r3 = received_voltage(s, var3)
        mhat_array = detection(Pm0=Pm0, E=e, r1=r1, r2=r2,
                               r3=r3, var1=var1, var2=var2, var3=var3)
        prob_of_error_array.append(prob_of_error(mi_array, mhat_array))
    prob_of_error_array = np.array(prob_of_error_array)
    t2 = time.time() - t1
    # print(prob_of_error_array)
    # print(E)

    # vitualize data
    figure, axis1 = plt.subplots(figsize=(8, 6))
    axis1.set_title("Simulation transmittion using\n"
                    r"$P(m_{0})$" + f" = {Pm0} " + r"$P(m_{1})$" + f" = {1-Pm0} " + "\n" + r"$\sigma_{1}^2$" + f" = {var1} " + r"$\sigma_{2}^2$" + f" = {var2} " + r"$\sigma_{3}^2$" + f" = {var3} ")
    axis1.set_yscale('log')
    axis1.plot(E, prob_of_error_array)
    axis1.set_xlabel('Signal energy')
    axis1.set_ylabel('Probability of Error')
    plt.autoscale(enable=True, axis='x', tight=True)
    plt.tight_layout()
    # plt.savefig(f'./figure/{filename[10:][:-4]}-freq.png')
    print(f'Calculated in {t2:0.2f} sec or {t2/60:0.2f} min.')
    plt.show()


if __name__ == '__main__':
    simulation(0.5, 9, 9, 9, 500000)
