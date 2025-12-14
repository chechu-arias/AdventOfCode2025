with open("01/complex.txt") as f:
    lines = [elem.strip() for elem in f.readlines()]

n_zeros = 0
actual_point = 50
exactly_zero = False

for idx, elem in enumerate(lines):
    # Count exactly at 0
    if not actual_point:
        exactly_zero = True
        n_zeros += 1

    movement = elem[0]
    number = int(elem[1:])
    n_clicks = number // 100
    number = number % 100

    # Count big rotations (10 for L1000 for example)
    n_zeros += n_clicks

    if movement == "L":
        actual_point -= number
        if actual_point < 0:
            # Dont count 0 that was already counted before
            if not exactly_zero:
                n_zeros += 1
            actual_point += 100
    else:
        actual_point += number
        if actual_point > 99:
            # Dont count 0 that was already counted before
            # or 100 that will be 0 in next iteration
            if not exactly_zero and actual_point > 100:
                n_zeros += 1
            actual_point -= 100

    exactly_zero = False

# Ensure n_zeros counts if actual ends at 0
if not actual_point:
    n_zeros += 1

print(f"[PART 2]: Solution is {n_zeros}")
