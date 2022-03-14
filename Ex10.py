# Leia uma velocidade em km/h (quilômetros por hora), e apresente-a convertida em m/s
# (metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
# km/s e M em m/s!

velocidade_KM = float(input('Digite a velocidade em KM: '))

metros_S = velocidade_KM / 3.6

print(f'A velocidade por metros por segundo é: {metros_S:.0f}')
