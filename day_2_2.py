def read_file(file):
    with open(file, "r") as f:
        input_data = f.readlines()
    return input_data

def split_commands(data_list):
    cmd_list = []
    for command in data_list:
        direction, distance = command.split(" ")
        cmd_list.append((direction, int(distance)))
    return cmd_list

def find_position(movements):
    horizontal, depth, aim = 0, 0, 0
    for movement in movements:
        if movement[0] == 'forward':
            horizontal += movement[1]
            depth += aim * movement[1]
        elif movement[0] == 'back':
            horizontal -= movement[1]
        elif movement[0] == 'up':
            aim -= movement[1]
        elif movement[0] == 'down':
            aim += int(movement[1])
    return (horizontal, depth)

def multiply_postion(final_pos):
    multi_pos = final_pos[0] * final_pos[1]
    return multi_pos

my_list = read_file('test2.txt')
command_list = split_commands(my_list)
final_position = find_position(command_list)
answer = multiply_postion(final_position)
print(final_position)
print(answer)