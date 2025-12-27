with open("02/complex.txt") as f:
    id_ranges = [elem.strip() for elem in f.readline().split(",")]


def is_repeated(number_str):
    numbers_dict = {}
    for digit in number_str:
        numbers_dict[digit] = numbers_dict.get(digit, 0) + 1

    if len(numbers_dict) == 1 and len(number_str) > 1:
        return True

    if (
        len(set(numbers_dict.values())) != 1
        and any(elem % 2 == 1 for elem in numbers_dict.values())
    ) or (
        len(set(numbers_dict.values())) == 1
        and len(numbers_dict) > 1
        and list(numbers_dict.values())[0] == 1
    ):
        return False

    for cut_length in range(2, (len(number_str) // 2) + 1):
        if len(number_str) % cut_length == 0 and (
            len(
                set(
                    [
                        number_str[i * cut_length : (i + 1) * cut_length]
                        for i in range(len(number_str) // cut_length)
                    ]
                )
            )
            == 1
        ):
            return True

    return False


result = 0
for r in id_ranges:
    start = r.split("-")[0]
    end = r.split("-")[1]

    for i in range(int(start), int(end) + 1):
        if is_repeated(str(i)):
            result += i

print(result)
