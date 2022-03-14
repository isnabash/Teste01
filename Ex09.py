# Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin
# A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius
# e K a temperatura em Kelvin

tempoC = float(input('Digite a temperatura em graus Celsius: '))

tempoK = tempoC + 273.15

print(f"A temperatura em graus Kelvin é: {tempoK:.0f}ºK")
