import matplotlib.pyplot as plt

level_list = []
exp_list = []

for loop in range(2, 101):
    # exp = ((2 * loop) ** 3) * ((loop ** 2) - (3 * loop) + 38)
    # exp2 = ((2 * (loop - 1)) ** 3) * (((loop - 1) ** 2) - (3 * (loop - 1)) + 38)
    exp = (((loop - 1) ** 2) * ((1.5 * (loop ** 2)) - (21 * loop) + 92))
    exp2 = ((((loop - 1) - 1) ** 2) * ((1.5 * ((loop - 1) ** 2)) - (21 * (loop - 1)) + 92))
    level_list.append(loop)
    exp_list.append(exp)

    # 10000 * (10201 - 1515 + 62)
    # print(format(int(exp), ','))
    print(format(int((exp - exp2)), ','))
    # print(f"{loop-1} -> {loop} : 총 경험치 > {exp} | 경험치 차 > {exp - exp2}")
    # print(f"{loop - 1} → {loop}")

plt.plot(level_list, exp_list)
plt.show()