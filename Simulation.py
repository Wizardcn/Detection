from Channel import *
from DecisionRule import *
from Detection import *
from Transmitter import *
import matplotlib.pyplot as plt


def simulation(Pm0, var1, var2, var3, n):

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
        s = transmit.voltage_s(mi_array, e)
        n1 = generate_noise(var1, n)
        n2 = generate_noise(var2, n)
        n3 = generate_noise(var3, n)
        r1 = received_voltage(s, n1)
        r2 = received_voltage(s, n2)
        r3 = received_voltage(s, n3)
        mhat_array = detection(Pm0=Pm0, E=e, r1=r1, r2=r2,
                               r3=r3, var1=var1, var2=var2, var3=var3)
        prob_of_error_array.append(prob_of_error(mi_array, mhat_array))
    prob_of_error_array = np.array(prob_of_error_array)
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
    plt.savefig(f'./Figure/{input("Enter file name: ")}.png')
    # plt.show()


if __name__ == '__main__':

    Pm0, var1, var2, var3, message = input(
        "Please enter Pm0, variance1, variance2, variance3 and amount of random messages:\n(ex. 0.5 9 9 9 50)\n-> ").split(" ")
    Pm0 = float(Pm0)
    var1, var2, var3, message = [int(element)
                                 for element in [var1, var2, var3, message]]

    t1 = time.time()
    print("processing...")
    simulation(Pm0, var1, var2, var3, message)
    t2 = time.time() - t1
    print(f'Calculated in {t2:0.2f} sec or {t2/60:0.2f} min.')
