def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = file_data.split("\n")
    return data_list

def count_value_changes(my_list):
    getting_bigger = 0
    the_same = 0
    getting_smaller = 0
    for index in range(len(my_list)):
        if int(my_list[index]) > int(my_list[index - 1]):
            getting_bigger += 1
        elif int(my_list[index]) == int(my_list[index - 1]):
            the_same += 1
        elif int(my_list[index]) < int(my_list[index - 1]):
            getting_smaller += 1
    return getting_bigger, the_same, getting_smaller

my_list = get_data('day_1.txt')
print(len(my_list))
print(count_value_changes(my_list))