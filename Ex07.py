# Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius
# A fórmula de conversão é: C = 5 * (F-32) /9, sendo C a temperatura em Celsius
# e F a temperatura em Fahrenheit!

tempoF = float(input('Digite a temperatura em Fahrenheit: '))

tempoC = 5.0 * (tempoF - 32.0) / 9.0

print(f'A temperatura em Celsius é: {tempoC:.0f}ºC')
