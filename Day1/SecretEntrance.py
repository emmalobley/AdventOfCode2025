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

def wrap_position(previous_position, x):
    print(x)
    i = 0
    while x < 0:
        if previous_position != 0:
            i = i + 1
        x = x + 100
    while x > 99:
        if x != 100:
            i = i + 1
        x = x - 100

    print(x,i)
    return x, i

def count_zeros(filename, start_position):
    lines = txt_to_lst(filename)
    position = start_position
    zero_count = 0
    i_count = 0
    for line in lines:
        new_move = int(add_orientation(line))
        position, i = wrap_position(position, position + new_move)
        if position == 0:
            zero_count = zero_count + 1
        i_count = i_count + i
        # print(position)
    return zero_count, i_count


# print(txt_to_lst("testinput.txt"))

x, i = count_zeros("input.txt", 50)
print("Zeros landed on: " + str(x))
print("Zeros passed: " + str(i))
print(x+i)

# 969 Zeros landed on
# 5483 too low