with open("03/complex.txt") as f:
    banks = [elem.strip() for elem in f.readlines()]


result = 0
for bank in banks:
    best_candidate = None
    for i in range(9):
        number = 9 - i
        index = bank.find(str(number))
        if index >= 0:
            for j in range(9):
                number2 = 9 - j
                index2 = bank[index + 1 :].find(str(number2))
                if index2 >= 0:
                    current = number * 10 + number2
                    if not best_candidate or current > best_candidate:
                        best_candidate = current

    result += best_candidate

print(result)
