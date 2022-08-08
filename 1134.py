alcool = gasolina = diesel = selecionado = 0
while selecionado != '4':
    selecionado = input()
    if selecionado == '1':
        alcool += 1
    if selecionado == '2':
        gasolina += 1
    if selecionado == '3':
        diesel += 1
print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}')
    