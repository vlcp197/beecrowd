
class Geometria:
    
    PI = 3.14159

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def area_triangulo(self,base,altura):
        return (base*altura)/2

    def area_circulo(self,raio):
        return Geometria.PI * raio**2

    def area_trapezio(self,b_maior,b_menor,altura):
        return ((b_maior+b_menor)*altura)/2

    def area_quadrado(self,lado):
        return lado**2

    def area_retangulo(self,comprimento,largura):
        return comprimento*largura

a,b,c = map(float,input().split())
geo = Geometria(a,b,c)        

print(f'TRIANGULO: {geo.area_triangulo(a,c):.3f}\nCIRCULO: {geo.area_circulo(c):.3f}\nTRAPEZIO: {geo.area_trapezio(a,b,c):.3f}\nQUADRADO: {geo.area_quadrado(b):.3f}\nRETANGULO: {geo.area_retangulo(a,b):.3f}')
