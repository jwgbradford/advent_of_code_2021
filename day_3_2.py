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

def find_bit_count(my_data, position):
    count_1, count_0 = 0, 0
    for word in my_data:
        if word[position] == '1':
            count_1 += 1
        else:
            count_0 += 1
    return count_1, count_0

def find_oxygen(my_data):
    word_length = len(my_data[0])
    filtered_data = my_data
    for pos in range(word_length):
        unfiltered_data = filtered_data
        filtered_data = []
        bit_count = find_bit_count(unfiltered_data, pos)
        if bit_count[0] > bit_count[1] or bit_count[0] == bit_count[1]:
            bit = '1'
        else:
            bit = '0'
        for word in unfiltered_data:
            if word[pos] == bit:
                filtered_data.append(word)
        if len(filtered_data) == 1:
            break
    return filtered_data[0]

def find_co2(my_data):
    word_length = len(my_data[0])
    filtered_data = my_data
    for pos in range(word_length):
        unfiltered_data = filtered_data
        filtered_data = []
        bit_count = find_bit_count(unfiltered_data, pos)
        if bit_count[0] < bit_count[1]:
            bit = '1'
        else:
            bit = '0'
        for word in unfiltered_data:
            if word[pos] == bit:
                filtered_data.append(word)
        if len(filtered_data) == 1:
            break
    return filtered_data[0]

my_data = read_file('day_3.txt')
epsilon_bin = find_epsilon(my_data)
gamma_bin = flip_bin(epsilon_bin)
oxygen = find_oxygen(my_data)
co2 = find_co2(my_data)
print(int(oxygen, 2) * int(co2, 2))