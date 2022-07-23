x = []
[x.append(input()) for i in range (0,6)]
x = [float(i) for i in x if float(i) > 0] 
print(f'{len(x)} valores positivos')