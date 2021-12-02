def read_file(file):
    input_file = open(file, 'r')
    input_data = input_file.read()
    input_file.closed
    return input_data

def get_data(file):
    file_data = read_file(file)
    data_list = file_data.split("\n")
    return data_list

def split_commands(data_list):
    cmd_list = []
    for command in data_list:
        direction, distance = command.split(" ")
        cmd_list.append((direction, distance))
    return cmd_list

def find_position(movements):
    horizontal, depth, aim = 0, 0, 0
    for movement in movements:
        if movement[0] == 'forward':
            horizontal += int(movement[1])
            depth += aim * int(movement[1])
        elif movement[0] == 'back':
            horizontal -= int(movement[1])
        elif movement[0] == 'up':
            aim -= int(movement[1])
        elif movement[0] == 'down':
            aim += int(movement[1])
    return (horizontal, depth)

def multiply_postion(final_pos):
    multi_pos = final_pos[0] * final_pos[1]
    return multi_pos

my_list = get_data('day_2.txt')
command_list = split_commands(my_list)
final_position = find_position(command_list)
answer = multiply_postion(final_position)
print(final_position)
print(answer)