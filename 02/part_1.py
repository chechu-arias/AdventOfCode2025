with open("02/complex.txt") as f:
    id_ranges = [elem.strip() for elem in f.readline().split(",")]


def is_repeated(number_str):
    if len(number_str) % 2 == 1:
        return False

    str_len = len(number_str) // 2
    return number_str[:str_len] == number_str[str_len:]


result = 0
for r in id_ranges:
    start = r.split("-")[0]
    end = r.split("-")[1]

    for i in range(int(start), int(end) + 1):
        if is_repeated(str(i)):
            result += i

print(result)
