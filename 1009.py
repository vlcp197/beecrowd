nome, salario, valor_vendas = input(), float(input()), float(input())
sal_final = salario + valor_vendas*0.15
print(f'TOTAL = R$ {sal_final:.2f}')