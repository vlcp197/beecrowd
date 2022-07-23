a, b, c = map(int,input().split())
print('S') if (a == b or a == c or b == c) or (a == b + c or b == a + c or c == a + b) else print('N')