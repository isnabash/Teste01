# Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius
# A fórmula de conversão é: C = K-273.15, sendo C a temperatura em Celsius
# e K a temperatura em Kelvin

tempoK = float(input("Digite a temperatura em graus Kelvin: "))

tempoC = tempoK - 273.15

print(f"A temperatura em graus Celsius é: {tempoC:.0f}ºC")
