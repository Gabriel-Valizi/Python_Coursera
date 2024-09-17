def fatorial (n):

    resultado = 1
    contador = 1

    while contador <= n:

        resultado *= contador
        contador += 1

    return resultado

def binomial (n, k):
    
    return ((fatorial(n)) / (fatorial(k) * fatorial(n - k)))

############################ Função main ############################

n = int(input("Digite o valor de n: "))
k = int(input("Digite o valor de k: "))

if n < 0 or k < 0:

    print("O fatorial não está definido para números negativos.")

else:

    fat = fatorial(n)
    fat_2 = fatorial(k)
    bin = binomial(n, k)
    print("Os fatoriais de n e k são, respectivamente,", fat, "e", fat_2)
    print("O binomial n/k é", bin)
