print(5>3)

print(type(False))

x=15
print(type(x>0))

print(x>0 and x**2>100) # AND
print(x>0 and x**2>300)

print(x>0 or x**2>300) # OR
print(x<0 and x**2>100)

print(not(x>0)) # NOT

# NIVEL 1 (BAIXO) - logico - OR
# NIVEL 2         - logico - AND
# NIVEL 3         - logico - NOT
# NIVEL 4         - relacional - ==, !=, <=, >=, >, <
# NIVEL 5         - adição - +, -
# NIVEL 6         - multiplicação - *, /, //, %
# NIVEL 7 (ALTO)  - exponenciação - **

a = 1000
b = 50
a > 0 and not b ==  50 or a + b == 150

# 1º soma --- soma a e b e compara com 150 --- a + b = 1050 > 150 - FALSE
# 2º not --- b == 50 - TRUE - inverte : FALSE
# 3º a > 0 (TRUE) and not b == 50 (FALSE) ----- FALSE
# 4º or --- resultado: FALSE

# fruta = laranja # erro: NameError

x = 10
y = 15
z = 25
print(x == z - y and z != y - x or not y != z - x)