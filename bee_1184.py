op = input().upper()

matrix = []
total = []

for line in range(12):
    matrix.append([])
    for column in range(12):
        float_ = (float(input()))
        matrix[line].append(float_)
        if column < line:
            total.append(float_)

if op == "S":
    print(sum(total))
elif op == "M":
    print(f"{(sum(total)/66):.1f}")