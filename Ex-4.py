s = float(input('Quanto você recebe?'))
a = float(input('Qual foi a porcentagem do seu aumento?'))
sa = s * (a / 100)

print(f'Você está recebendo R${sa: .2f} a mais')
print(f'Seu novo salário é R${s + sa: .2f}')
