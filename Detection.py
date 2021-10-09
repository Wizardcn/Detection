import numpy as np
from Channel import received_voltage
import Transmitter as transmit
import DecisionRule


def detection(Pm0, Ei, Ef, inc_E, r1, r2, r3, var1, var2, var3):
    E = np.linspace(Ei, Ef, num=int(Ef / inc_E), endpoint=True)
    mhat = []
    for i in range(E.shape[0]):
        decision_result = DecisionRule.ODR_not(
            Pm0=Pm0, E=E[i], r1=r1[i], r2=r2[i], r3=r3[i], var1=var1, var2=var2, var3=var3)
        mhat.append(decision_result)
    mhat_array = np.array(mhat)
    return mhat_array


def prob_of_error():
    pass


if __name__ == "__main__":
    mi_array = transmit.generate_mi(0.5, 500000)
    s = transmit.voltage_s(mi_array, 0.1, 10, 0.1)
    r1 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    r2 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    r3 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    print(mi_array)
    print(detection(0.5, 0.1, 10, 0.1, r1, r2, r3, 9, 9, 9))
