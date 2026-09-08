def get_ids(file_path):
    # converts txt file to list or rotation instructions
    try:
        stopword = open(file_path,"r")
        lines = stopword.read().split('-')

    except Exception as e:
        print(e)

    return lines

print(get_ids("testinput.txt"))