def get_id_ranges(file_path):
    # converts txt file to list or rotation instructions
    try:
        file = open(file_path,"r")
        id_ranges = file.read().split(',')

    except Exception as e:
        print(e)

    return id_ranges

def get_all_even_digit_ids(id_ranges):
    even_digit_ids = []
    for r in id_ranges:
        start, end = r.split('-')
        if len(start)%2 == 0 or len(end)%2 == 0:
            # one or both start/end ids in range is divisible by 2
            new_ids = list(range(int(start),int(end)+1))
            for id in new_ids:
                if len(str(id))%2 == 0:
                    even_digit_ids.append(str(id))

    # print(even_digit_ids)
    return even_digit_ids


def get_sum_fake_ids(even_ids):
    sum = 0
    for s in even_ids:
        first_half  = s[:len(s)//2]
        second_half = s[len(s)//2:]
        if first_half == second_half:
            sum = sum + int(s)
    return sum


id_ranges = get_id_ranges("input.txt")
print(get_sum_fake_ids(get_all_even_digit_ids(id_ranges)))
