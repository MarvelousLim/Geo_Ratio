input = open('frozen_ratio.txt', 'r')
output = open('frozen_ratio_table.txt', 'w')
data = input.read().split()
for i in range(len(data) // 3):
    t, r1, r2 = data[3 * i], data[3 * i + 1], data[3 * i + 2]
    output.write(str(t) + ' ' + str(r1) + ' ' + str(r2) + '\n')

input.close()
output.close()
