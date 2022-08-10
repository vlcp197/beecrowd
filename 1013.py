a,b,c = map(int, input().split())

def abs(a,b): return a-b if a > b else -1 * (a-b)
    
abs = abs(a,b)

maiorAB = int((a+b+abs)/2)
maior = c if c > maiorAB else maiorAB

print(f'{maior} eh o maior')