def optimumDecisionRule(r1, r2, r3):
    if r1 + r2 + r3 < 0:
        mhat = 0
    elif r1 + r2 + r3 > 0:
        mhat = 1
    return mhat


if __name__ == "__main__":
    print(optimumDecisionRule(3, 3, 2))
    print(optimumDecisionRule(3, -3, -2))
