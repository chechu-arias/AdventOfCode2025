with open("01/complex.txt") as f:
    lines = [elem.strip() for elem in f.readlines()]

n_zeros = 0
actual_point = 50


for elem in lines:
    if not actual_point:
        n_zeros += 1

    movement = elem[0]
    number = int(elem[1:])
    number = number % 100

    if movement == "L":
        actual_point -= number
        if actual_point < 0:
            actual_point = 100 + actual_point
    else:
        actual_point += number
        if actual_point > 99:
            actual_point -= 100

if not actual_point:
    n_zeros += 1

print(f"[PART 1]: Solution is {n_zeros}")
