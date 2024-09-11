numero = int(input ("Digite um número inteiro: "))

# Remove o dígito das unidades
numero_dezenas = numero // 10

# Pega o último dígito, que é o das dezenas
digito_das_dezenas = numero_dezenas % 10

print("O dígito das dezenas é", digito_das_dezenas)