'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
    print('Nabor')



#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print(30*27)



#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    media = (5+8+12)/3
    print(f'5+8+12)/3 = {media:.2}')



#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    num = int(input('Digite um número: '))
    print(f'Você digitou o número: {num}')



#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    x = float(input('Digite um número real: '))
    y = float(input('Digite outro número real: '))

    print(f'Números digitados: {x} e {y}')



#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    num = int(input('Digite um número inteiro: '))
    print(f'Antecessor de {num} é {num - 1}')
    print(f'Sucessor de {num} é {num + 1}')



#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input('Digite seu nome: ').title().strip()
    endereço = input('Digite seu endereço: ')
    telefone = input('Digite seu telefone: ')

    print (f'\nNome: {nome}\nEndereço: {endereço}\nTelefone: {telefone}')
    


#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    num1 = int(input('Digite o 1º número: '))
    num2 = int(input('Digite o 2º número: '))

    print(f'A subtração de {num1} e {num2} é {num1 - num2}')



#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    num = float(input('Digite um número real: '))

    print (f'1/4 do número {num} é: {num/4}')



#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    num1 = int(input('Digite o 1º número:'))
    num2 = int(input('Digite o 1º número:'))
    num3 = int(input('Digite o 1º número:'))

    soma = num1 + num2 + num3
    media = soma/3
    print(f'\nA média aritmética dos numeros {num1}, {num2} e {num3} é: {media:.2}')



#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    num1 = float(input('Digite o 1º número real: '))
    num2 = float(input('Digite o 2º número real: '))

    print(f'\nAdição: {num1 + num2:.2}')
    print(f'\nSubtração: {num1 - num2:.2}')
    print(f'\nMultiplicação: {num1 * num2:.2}')
    print(f'\nDivisão: {num1 / num2:.2}')



#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():

    num = float(input('Digite um número real: '))

    print(f'O valor ao quadrado de {num} é: {num*num}')


#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input('Digite o saldo da conta poupança: '))
    NSaldo = saldo*1.02 

    print(f'\n O novo saldo com reajuste de 2% é: {NSaldo:.2f}')



#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    
def q14():
    base = float(input('Informe a base do retângulo: '))
    altura = float(input('Informe a altura do retângulo: '))
    perímetro = (base*2 + altura*2)
    área = (base * altura)

    print(f'O perímetro do retângulo é: {perímetro:.2f}m')
    print(f'A área do retângulo é: {área:.2f}m')



#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():

    produto = float(input('Digite o valor do produto: '))
    percentual = float(input('Digite o percentual de desconto desejado: '))

    desconto = produto * (percentual/100)
    valorFinal = produto - desconto

    print(f'O valor do desconto é R${desconto:.2f}')
    print(f'O valor final do produto é R${valorFinal:.2f}')



#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():

    SalarioAtual = float(input('Insira o salário atual: '))
    Percentual = float(input('Informe o percentual de reajuste: '))

    NovoSalario = SalarioAtual + (SalarioAtual * (Percentual/100))
    print(f'\nNovo Salário com reajuste: R${NovoSalario:.2f}')



#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17(): 

    centigrados = float(input('Informe a temperatura em graus centígrados: '))
    Fahrenheit = (9 * centigrados + 160) / 5

    print(f'A conversão de Graus centígrados para fahrenheit é: {Fahrenheit:.2f}°F')

 

#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    t = float(input('Informe o tempo percorrido na viagem: '))
    v = float(input('Informe a velocidade média do carro: '))

    d = t * v 
    l = d / 12

    print(f'Distância percorrida na viagem: {d}m')
    print(f'Quantidade de litros consumidos: {l:.2f}l')




#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():

    prestaçãoV = float(input('Informe o valor da prestação vencida: '))
    taxaPJuros = float(input('Informe a taxa periódica de juros: '))
    PDatraso = float(input('Informe o período de atraso: '))

    juros = prestaçãoV * (taxaPJuros/100) * PDatraso
    valorFinal = prestaçãoV + juros

    print (f'Valor da prestação atrasada: R${prestaçãoV:.2f}')
    print (f'Período de atraso: R${PDatraso}')
    print (f'Valor do juros: R${juros:.2f}')
    print (f'Valor total da prestação com juros acrescentado: R${valorFinal:.2f}')


#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():

    Dólar = float(input('Informe um valor em Dólar(US$): '))
    real = Dólar * 5.14

    print(f'O valor {Dólar}(US$) convertido em real(R$) é: {real:.2f} ')

questão = input('Digite a questão a ser executada: ')
eval(f'q{questão}()')
