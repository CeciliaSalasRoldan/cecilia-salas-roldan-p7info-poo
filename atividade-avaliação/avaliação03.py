numero_input = int(input('Insira um número positivo: '))
soma_num = 0
contagem = 0
num = 2

while contagem < numero_input:
    num_primo = True
    for i in range(2, num):
        if num % i == 0:
           num_primo = False
           break
    if num_primo:
        print(num)
        soma_num += num
        contagem += 1
    num += 1
print('A soma dos números primos é: ',soma_num)