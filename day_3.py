def read_file(file):
    with open(file, "r") as f:
        input_data = [str(data)[:-1] for data in f.readlines()]
    return input_data

def find_counts(my_data):
    count_1 = [0 for _ in range(len(my_data[0]))]
    count_0 = [0 for _ in range(len(my_data[0]))]
    for word in my_data:
        for index, value in enumerate(word):
            if value == '1':
                count_1[index] += 1
            else:
                count_0[index] += 1
    return count_1, count_0

def find_epsilon(my_data):
    count1, count0 = find_counts(my_data)
    epsilon = ''
    for index in range(len(count1)):
        if count1[index] > count0[index]:
            epsilon = epsilon + '1'
        else:
            epsilon = epsilon + '0'
    return epsilon

def flip_bin(bin_data):
    flipped_bin = ''
    for value in bin_data:
        if value == '1':
            flipped_bin = flipped_bin + '0'
        else:
            flipped_bin = flipped_bin + '1'
    return flipped_bin

my_data = read_file('day_3.txt')
epsilon_bin = find_epsilon(my_data)
gamma_bin = flip_bin(epsilon_bin)
print(epsilon_bin, gamma_bin)
print((int(epsilon_bin, 2)), (int(gamma_bin, 2)))
power_drain = (int(epsilon_bin, 2)) * (int(gamma_bin, 2))
print(power_drain)