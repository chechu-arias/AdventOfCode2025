with open("03/complex.txt") as f:
    banks = [elem.strip() for elem in f.readlines()]


def get_solution_int(bank, current_solution):
    result = ""
    for index in current_solution:
        result += bank[index]

    return int(result)


def get_result(bank, current_solution, current_index, first: bool = False):

    if len(current_solution) == 12:
        return current_solution

    if len(bank) - current_index < 12 - len(current_solution):
        current_solution.pop()
        return current_solution

    for i in range(9):
        number = 9 - i
        search_index = current_index if first else current_index + 1
        index = bank[search_index:].find(str(number))
        global_str_index = index + search_index
        if index >= 0 and (
            not current_solution or global_str_index > current_solution[-1]
        ):
            current_solution.append(global_str_index)
            current_solution = get_result(
                bank,
                current_solution=current_solution,
                current_index=global_str_index,
            )
            if len(current_solution) == 12:
                return current_solution

    current_solution.pop()
    return current_solution


result = 0
for bank in banks:
    bank_voltage_indexes = get_result(bank, [], 0, first=True)
    bank_voltage = get_solution_int(bank, bank_voltage_indexes)
    result += bank_voltage

print(result)
