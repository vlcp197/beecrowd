(x1,y1),(x2,y2) = map(float,input().split()),map(float,input().split())

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

print(f'{distancia:.4f}')