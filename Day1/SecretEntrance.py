def txt_to_lst(file_path):
    # converts txt file to list or rotation instructions
    try:
        stopword = open(file_path,"r")
        lines = stopword.read().split('\n')

    except Exception as e:
        print(e)

    return lines

def add_orientation(x):
    # replaces L with a - or removed R
    match = x.startswith('L')
    if match:
        return "-" + x[1:]
    return x[1:]

def wrap_position(previous_position, new_position):
    # print(previous_position, new_position)
    i = 0
    
    while new_position < 0:
        i = i + 1
        new_position = new_position + 100
    while new_position > 99:
        i = i + 1
        new_position = new_position - 100

    if previous_position == 0 & i > 0:
            i = i - 1
    print("New position: " + str(new_position))
    print("Passed zero: "+ str(i))
    return new_position, i

def count_zeros(filename, start_position):
    lines = txt_to_lst(filename)
    position = start_position
    land_zero_count = 0
    pass_zero_count = 0
    for line in lines:
        new_move = int(add_orientation(line))
        print("New move: " + str(new_move))
        position, i = wrap_position(position, position + new_move)
        if position == 0:
            land_zero_count = land_zero_count + 1
        pass_zero_count = pass_zero_count + i
        # print(position)
    return land_zero_count, pass_zero_count


# print(txt_to_lst("testinput.txt"))

x, i = count_zeros("testinput.txt", 50)
print("Zeros landed on: " + str(x))
print("Zeros passed: " + str(i))
print(x+i)

# 969 Zeros landed on
# 5483 too low
# 5876 not right