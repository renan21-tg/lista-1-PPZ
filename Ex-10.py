c = int(input('Quantos cigarros você fuma por dia?'))
a = int(input('Há quantos anos você fuma?'))

tc = c * 365  * a 
d = tc / 144

print(f'Você perdeu {d: .2f} dias de vida')

