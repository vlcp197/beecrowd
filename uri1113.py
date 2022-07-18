while True:
    x,y = map(int,input().split())
    if x != y:
        print("Crescente") if x < y else print("Decrescente")
    else:
         break