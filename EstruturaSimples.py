A = input("informe um valor para a variável A: ")
B = input('informe um valor para a variável B: ')

if (A>B):
    aux = A
    A = B
    B = aux

print('o valor da variável A agora é : ', A)
print('o valor da variável B agora é : ', B)