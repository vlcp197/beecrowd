total = 0

for i in range(2):
    cod, qtd, valor = input().split()
    total += int(qtd) * float(valor)

print(f"VALOR A PAGAR: R$ {total:.2f}")