import numpy as np
from Channel import received_voltage
import Transmitter as transmit
import DecisionRule


def detection(Pm0, E, r1, r2, r3, var1, var2, var3):
    mhat = []
    for i in range(r1.shape[0]):
        decision_result = DecisionRule.ODR_not(
            Pm0=Pm0, E=E, r1=r1[i], r2=r2[i], r3=r3[i], var1=var1, var2=var2, var3=var3)
        mhat.append(decision_result)
    mhat_array = np.array(mhat)
    return mhat_array


def prob_of_error(mi, mhat):
    error = 0
    for mi_element, mhat_element in zip(mi, mhat):
        if mi_element == mhat_element:
            error += 1
        else:
            continue
    return error / mi.shape[0]


if __name__ == "__main__":
    mi_array = transmit.generate_mi(0.5, 50)
    E = 5
    s = transmit.voltage_s(mi_array, E)
    r1 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    r2 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))
    r3 = received_voltage(s, np.random.normal(0, 9, s.shape[0]))

    result = detection(0.5, E, r1, r2, r3, 9, 9, 9)
    print(result)
    print(result.shape[0])
    print(prob_of_error(mi=mi_array, mhat=result))
    # E = np.linspace(Ei, Ef, num=int(Ef / inc_E), endpoint=True)
