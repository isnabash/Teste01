# Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit
# A fórmula de conversão é: F = C * (9/5) + 32, sendo F a temperatura em Fahrenheit
# e C a temperatura em Celsius

tempoC = float(input('Digite a temperatura em Celsius:'))

tempoF = (tempoC * (9.0 / 5.0) + 32.0)

print(f"A temperatura em Fahrenheit é: {tempoF:.0f}ºF")
