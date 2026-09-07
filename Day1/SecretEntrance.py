
def get_orientation():

    return True


def get_turns(filename):
    with open("testinput.txt") as file_in:
        lines = []
        for line in file_in:
            lines.append(line)  

    print(lines)
    return lines

print(get_turns("testinput.txt"))
print("hello")