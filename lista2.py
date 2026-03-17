#Exercícios sobre os comandos de condição em python
#'''
import random
from datetime import datetime
def exemploSe():
    idade = 18
    if idade == 18:  # Se idade for igual a 18
        print('Possui 18 anos')

def exemploSeSenao():
    idade = 60
    if idade >= 18 and idade < 60:   # Se idade for maior ou igual a 18 e menor que 60
        print('Maior de idade')
    elif idade >= 60: # Senão se a idade for maior ou igual a 60
        print('Melhor idade')
    else:             # Senão
        print('Menor de idade')

def exemploSeSenao():
    idade = 60
    if idade >=60:   # Se idade for maior ou igual a 60 
        print('Melhor idade')
    elif idade >= 18: # Senão se a idade for maior ou igual a 18
        print('Maior de idade')
    else:             # Senão
        print('Menor de idade')

def exemploCaso():      # serve apenas para valores conhecidos (poucos) e exatos.
    estado_civil = 's'
    match(estado_civil):
        case 's':
            print('Solteiro')
        case 'c':
            print('Casado')
        case _:
            print('Valor padrão ou desconhecido!')

#1. Faça um programa que leia dois valores numéricos inteiros e efetue
#   a adição, caso o resultado seja maior que 10, apresentá-lo.

def q1():
    try:
        num1 = int(input("Digite um número inteiro: "))
        num2 = int(input("Digite outro número inteiro: "))
        soma = num1 + num2

        if soma > 10:
            print(f"O resultado da soma é {soma}")

        else: 
            print("O resultado da soma é menor ou igual a 10.")
    
    except ValueError:
        print("Valor errado! Somente números inteiros são aceitos. Tente novamente.")
    

#2. Faça um programa que leia dois valores inteiros e efetue a adição.
#   Caso o valor somado seja maior que 20, este deverá ser apresentado
#   somando-se a ele mais 8, caso o valor somado seja menor ou igual a
#   20, este deverá ser apresentado subtraindo-se 5.

def q2():
    try:
        num1 = int(input("Digite um número inteiro para a adição: "))
        num2 = int(input("Digite um número inteiro para a adição: "))
        soma = num1 + num2

        if soma > 20:
            print(f'O resultado da adição de {num1} + {num2} é {soma}. {soma} + 8 é {soma + 8}')
        else:
            print(f'O resultado da adição de {num1} + {num2} é {soma}. {soma} - 5 é {soma - 5}')
    except ValueError:
        print("Valor errado! Somente números inteiros são aceitos. Tente novamente.")

#3. Faça um programa que leia um número e imprima uma das duas mensagens:
#   "É múltiplo de 3"ou "Não é múltiplo de 3".
def q3():
    try:
        num = int(input('Digite um número inteiro: '))

        if num % 3 == 0:
            print(f'O número {num} é múltiplo de 3.')
        else:
            print(f'O número {num} não é múltiplo de 3.')
    except ValueError:
        print("Valor errado! Somente números inteiros são aceitos. Tente novamente.")

#4. Faça um programa que leia um número e informe se ele é ou não divisível por 5.

def q4():
    try:
        num = int(input('Digite um número inteiro: '))
        
        if num % 5 == 0:
            print(f'O número {num} é divisível por 5.')
        else:
            print(f'O número {num} não é divisível por 5.')
    except ValueError:
        print("Valor errado! Somente números inteiros são aceitos. Tente novamente.")
        


#5. Faça um programa que leia um número e informe se ele é divisível por 3 e por 7.

def q5():
    try:
        num = int(input('Digite um número inteiro: '))

        if num % 3 == 0 and num % 7 == 0:
            print(f'O número {num} é divisível por 3 e por 7.')
        else:
            print(f'O número {num} não é divisível por 3 e por 7.')
    except ValueError:
        print("Valor errado! Somente números inteiros são aceitos. Tente novamente.")

#6. A prefeitura do Rio de Janeiro abriu uma linha de crédito para os funcionários
#   estatutários. O valor máximo da prestação não poderá ultrapassar 30% do salário
#   bruto. Faça um programa que permita entrar com o salário bruto
#   e o valor da prestação e informar se o empréstimo pode ou não ser concedido.

def q6():
    try:
        SBruto = float(input('Informe o seu salário bruto: '))
        Percentual = float(input('Informe o valor da prestação: '))
        SMax = SBruto * 0.30

        if Percentual <= SMax:
            print(f'O empréstimo pode ser concedido. A prestação de {Percentual:.2f} está dentro do limite de 30% (R${SMax}) ')
        else:
            print(f'O empréstimo não pode ser concedido. A prestação de {Percentual:.2f} excede o limite de 30% (R${SMax}')
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos')
#7. Faça um programa que leia um número e indique se o número está compreendido
#   entre 20 e 50 ou não.

def q7():
    try:
        num = random.randrange(100)

        if num >= 20 and num <= 50:
            print(f'O número {num} está entre 20 e 50')
        else:
            print(f'O número {num} está fora do intervalo de 20 e 50')
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos')

#8. Faça um programa que leia um número e imprima uma das mensagens:
#   "Maior do que 20", "Igual a 20"ou "Menor do que 20".

def q8():
    try:
        num = int(input('Insira um número inteiro: '))

        if num > 20:
            print(f'O número {num} é maior do que 20')
        elif num < 20:
            print(f'O número {num} é menor do que 20')
        else:
            print(f'O número {num} é igual a 20')
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos')

#9. Faça um programa que permita entrar com o ano de nascimento da pessoa e com o
#   ano atual. O programa deve imprimir a idade da pessoa. Não se esqueça de
#   verificar se o ano de nascimento informado é válido.

def q9():
    try:
        ano = int(input("Informe o seu ano de nascimento: "))
        idade = (datetime.now().year - ano)

        if 1900 <= ano <= datetime.now().year:
            idade = datetime.now().year - ano
            print(f'Se você nasceu em {ano}, você tem {idade} anos.')
        else:
            print('Ano de nascimento inválido')
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos')

#10. Faça um programa que leia três números inteiros e imprima os três em ordem
#crescente.

def q10():
    try:

        num1 = int(input('Informe o 1° número inteiro: '))
        num2 = int(input('Informe o 2° número inteiro: '))
        num3 = int(input('Informe o 3° número inteiro: '))

        if num1 <= num2 and num1 <= num3:
            if num2 <= num3:
                print(num1, num2, num3)
            else:
                print(num1, num3, num2)
        elif num2 <= num1 and num2 <= num3:
            if num1 <= num3:
                print(num2, num1, num3)
            else:
                print(num2, num3, num1)
        else:
            if num1 <= num2:
                print(num3, num1, num2)
            else:
                print(num3, num2, num1)
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos')



#11. Faça um programa que leia 3 números e imprima o maior deles.

def q11():
    try:

        num1 = int(input('Informe 1° número inteiro: '))
        num2 = int(input('Informe 2° número inteiro: '))
        num3 = int(input('Informe 3° número inteiro: '))

        if num1 > num2 and num1 > num3:
            print(f"O maior número digitado é: {num1}")
        elif num2 > num1 and num2 > num3:
            print(f"O maior número digitado é: {num2}")
        else:
            print(f"O maior número digitado é: {num3}")
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos')

#12. Faça um programa que leia a idade de uma pessoa e informe:
#• Se é maior de idade
#• Se é menor de idade
#• Se é maior de 65 anos

def q12():
    try:
        idade = int(input('Informe sua idade: '))

        if idade >= 18 and idade <= 65:
            print('Maior de idade.') 
        elif idade < 18:
            print('Menor de idade.')
        else:
            print('Mais de 65 anos')
    except ValueError:
        print('Idade inválida! Somente aceitamos em números inteiros')

#13. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
#da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
#a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
#"Reprovado"ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
#reprovação e as demais em prova final).

def q13():
    try:

        nome = input("Informe seu nome: ")
        nota1 = float(input('Informe a nota da prova 1: '))
        nota2 = float(input('Informe a nota da prova 2: '))
        média = (nota1 + nota2)/2

        if nota1 < 0 and nota2 > 10 and nota2 < 0 and nota2 > 10:
            print('Notas inválidas')
        elif média >= 7:
            print(f'Aluno: {nome}\nNota da prova 1: {nota1}\nNota da prova 2: {nota2}\nMédia: {média}\nAprovado!!!')
        elif média < 3:
            print(f'Aluno: {nome}\nNota da prova 1: {nota1}\nNota da prova 2: {nota2}\nMédia: {média}\nReprovado!!!') 
        else:
            print(f'Aluno: {nome}\nNota da prova 1: {nota1}\nNota da prova 2: {nota2}\nMédia: {média}\nEm Prova Final!!!')           
    except ValueError:
        print('Nome inválido! Somente aceitamos nomes em texto')


#14. Faça um programa que permita entrar com o salário de uma pessoa e imprima o
#desconto do INSS segundo a tabela seguir:
#Salário Faixa de Desconto
#Menor ou igual à R$600,00 Isento
#Maior que R$600,00 e menor ou igual a R$1200,00 20%
#Maior que R$1200,00 e menor ou igual a R$2000,00 25%
#Maior que R$2000,00 30%

def q14():
    try:
        Salário = float(input("Informe o seu salário: "))
        Desconto = 0.0

        if Salário <= 600.00:
            Desconto = 0.0
            print('Faixa: isento')
        elif Salário > 600.00 and Salário <= 1200.00:
            Desconto = Salário * 0.20
            print("Faixa: 20%")
        elif Salário > 1200.00 and Salário <= 2000.00:
            Desconto = Salário * 0.25
            print('Faixa: 25%')
        else:
            Desconto = Salário * 0.30
            print('Faixa: 30%')
        print(f'Salário bruto: R${Salário:.2f}')
        print(f'Desconto INSS: R${Desconto:.2f}')
        print(f'Salário Líquido: R${Salário - Desconto:.2f}')
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos. Tente Novamente.')

#15. Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o
#valor da compra for menor que R$20,00, caso contrário, o lucro será de 30%.
#Faça um programa que leia o valor do produto e imprima o valor da venda.

def q15():
    try:
        produto = float(input("Informe o valor do produto: "))
        Lucro = 0.0

        if produto < 20.00:
            Lucro = produto * 0.45
            print(f'O valor de venda do produto com 45% de Lucro é:  R${produto + Lucro:.2f}')
        else:
            Lucro = produto * 0.30
            print(f'O valor de venda do produto com 30% de Lucro é: R${produto + Lucro:.2f}')
    except ValueError:
        print('Valor inválido! Somente números reais são aceitos. Tente Novamente.')

#16. A confederação brasileira de natação irá promover eliminatórias para o
#próximo mundial. Faça um programa que receba a idade de um nadador e imprima
#a sua categoria segundo a tabela a seguir:
#Categoria Idade
#Infantil A 5 - 7 anos
#Infantil B 8 - 10 anos
#Juvenil A 11 - 13 anos
#Juvenil B 14 - 17 anos
#Sênior maiores de 18 anos

def q16():
    try:
        idade = int(input('Informe a idade do nadador: '))

        if idade >= 5 and idade <= 7:
            print(f'A Categoria do nadador é Infantil A.')
        elif idade >= 8 and idade <= 10:
            print(f'A Categoria do nadador é Infantil B.')
        elif idade >= 11 and idade <= 13:
            print(f'A Categoria do nadador é Juvenil A.')
        elif idade >= 14 and idade <= 17:
            print(f'A Categoria do nadador é Juvenil B.')
        else:
            print(f'A Categoria do nadador é Sênior.')
    except ValueError:
        print('Valor Inválido! Somente números inteiros são aceitos. Tente Novamente')

#17. Depois da liberação do governo para as mensalidades dos planos de saúde,
#as pessoas começaram a fazer pesquisas para descobrir um bom plano, não
#muito caro. Um vendedor de um plano de saúde apresentou a tabela a seguir.
#Faça um programa que entre com o nome e a idade de uma pessoa e imprima o
#nome e o valor que ela deverá pagar.
#Idade Valor
#Até 10 anos R$30,00
#Acima de 10 até 29 anos R$60,00
#Acima de 29 até 45 anos R$120,00
#Acima de 45 até 59 anos R$150,00
#Acima de 59 até 65 anos R$250,00
#Maior que 65 anos R$400,00

def q17():
    try:
        nome = input('Informe o seu nome: ')
        idade = int(input('Informe a sua idade: '))
        valor = 0

        if idade <= 10:
            valor = 30
            print(f'Nome: {nome}\nIdade: {idade}\nValor a pagar: R${valor},00')
        elif idade > 10 and idade <= 29:
            valor = 60
            print(f'Nome: {nome}\nIdade: {idade}\nValor a pagar: R${valor},00')
        elif idade > 29 and idade <= 45:
            valor = 120
            print(f'Nome: {nome}\nIdade: {idade}\nValor a pagar: R${valor},00')
        elif idade > 45 and idade <= 59:
            valor = 150
            print(f'Nome: {nome}\nIdade: {idade}\nValor a pagar: R${valor},00')
        elif idade > 59 and idade <= 65:
            valor = 250
            print(f'Nome: {nome}\nIdade: {idade}\nValor a pagar: R${valor},00')
        else:
            valor = 400
            print(f'Nome: {nome}\nIdade: {idade}\nValor a pagar: R${valor},00')
    except ValueError:
        print("Idade ou nomes inválidos! Nomes só são aceitos em texto, e idade somente em inteiros.")
        

#18. Faça um programa que leia um número inteiro entre 1 e 12 e escreva o mês
#correspondente. Caso o usuário digite um número fora desse intervalo, deverá
#aparecer uma mensagem informando que não existe mês com este número.

def q18():
    try:
        mes = int(input("Informe o número do mês desejado: "))

        if mes == 1:
            print("O mês digitado é Janeiro.")
        elif mes == 2:
            print("O mês digitado é Fevereiro.")
        elif mes == 3:
            print("O mês digitado é Março.")
        elif mes == 4:
            print("O mês digitado é Abril.")
        elif mes == 5:
            print("O mês digitado é Maio.")
        elif mes == 6:
            print("O mês digitado é Junho.")
        elif mes == 7:
            print("O mês digitado é Julho.")
        elif mes == 8:
            print("O mês digitado é Agosto.")
        elif mes == 9:
            print("O mês digitado é Setembro.")
        elif mes == 10:
            print("O mês digitado é Outubro.")
        elif mes == 11:
            print("O mês digitado é Novembro.")
        elif mes == 12:
            print("O mês digitado é Dezembro.")
        else:
            print("Não há um mês com esse número")
    except ValueError:
        print("Valor inválido! Meses só são aceitos em números inteiros.")

#19. Em um campeonato nacional de arco-e-flecha, tem-se equipes de três jogadores
#para cada estado. Sabendo-se que os arqueiros de uma equipe não obtiveram o
#mesmo número de pontos, criar um programa que informe se uma equipe foi
#classificada, de acordo com a seguinte especificação:
#• Ler os pontos obtidos por cada jogador da equipe;
#• Mostrar esses em ordem decrescente;
#• Se a soma dos pontos for maior do que 100, imprimir a média aritmética entre eles,
#  caso contrário, imprimir a mensagem "Equipe desclassificada".

def q19():
    try:
        ponto1 = int(input("Informe quantos pontos o Arqueiro número 1° fez: "))
        ponto2 = int(input("Informe quantos pontos o Arqueiro número 1° fez: "))
        ponto3 = int(input("Informe quantos pontos o Arqueiro número 1° fez: "))
        total = ponto1 + ponto2 + ponto3
        media = total/3

        if ponto1 >= ponto2 and ponto1 >= ponto3:
            if ponto2 >= ponto3:
                print(f"Pontos da equipe em ordem decrescente:\n{ponto1}, {ponto2} ,{ponto3}")
            else:
                print(f"Pontos da equipe em ordem decrescente:\n{ponto1}, {ponto3} ,{ponto2}")
        elif ponto2 >= ponto1 and ponto2 >= ponto3:
            if ponto1 >= ponto3:
                print(f"Pontos da equipe em ordem decrescente:\n{ponto2}, {ponto1} ,{ponto3}")
            else:
                print(f"Pontos da equipe em ordem decrescente:\n{pontos}, {ponto3} ,{ponto1}")
        else:
            if ponto1 >= ponto2:
                print(f"Pontos da equipe em ordem decrescente:\n{pontos3}, {ponto1} ,{ponto2}")
            else:
                print(f"Pontos da equipe em ordem decrescente:\n{pontos3}, {ponto2} ,{ponto1}\nPontuação total da equipe:\n{total}")

        if total > 100:
            print(f"A média da equipe é {media}.")
        else:
            print("Equipe desclassificada.")

    except ValueError: 
        print("Valor inválido!Somente números inteiros são aceitos")

#20. O banco XXX concederá um crédito especial com juros de 2% aos seus clientes de
#acordo com o saldo médio no último ano. Faça um programa que leia o saldo médio
#de um cliente e calcule o valor do crédito de acordo com a tabela a seguir.
#O programa deve imprimir uma mensagem informando o saldo médio e o valor de
#crédito.
#Saldo Médio Percentual
#de 0 a 500 nenhum crédito
#de 501 a 1000 30% do valor do saldo médio
#de 1001 a 3000 40% do valor do saldo médio
#acima de 3001 50% do valor do saldo médio

def q20():
    try:
        Smedio = float(input("Informe o salário médio: R$"))
        credito = 0

        if Smedio >= 0 and Smedio <= 500:
            credito = 0
        elif Smedio > 500 and Smedio <= 1000:
            credito = Smedio*0.30
        elif Smedio > 1000 and Smedio <= 3000:
            credito = Smedio*0.40
        elif Smedio > 3000:
            credito = Smedio*0.50 
        else:
            print("Não é possiver o saldo médio ser menor que 0.") 

        print(f"\nSaldo Médio: R$ {Smedio}")
        print(f"Valor do crédito: R${credito} ")
    except ValueError:
        print("Valor inválido!Somente são aceitos números reais.")

#21. A biblioteca de uma Universidade deseja fazer um programa que leia o nome do
#livro que será emprestado, o tipo de usuário (professor ou aluno) e possa
#imprimir um recibo conforme mostrado a seguir. Considerar que o professor
#tem dez dias para devolver o livro e o aluno só três dias.
#• Nome do livro:
#• Tipo de usuário:
#• Total de dias:

def q21():
    try:
        livro = input("Informe o nome do livro que vai emprestar: ")
        print("Tipo de Usuário: Professor [1], Aluno [2]")
        usuario = input('Digite o tipo de usuário [1] ou [2]: ')

        if usuario == "2":
            dias = 3
            usuario_str = 'Aluno'
        elif usuario == "1":
            dias = 3
            usuario_str = 'Professor'
            print(f'Livro Emprestado: {livro}\nTipo de Usuário: {usuario}\nTotal de dias para devolver: 10 dias.')
        else:
            print("Usúario inválido! Informe se é aluno ou professor.")

        if dias > 0 and dias < 3:
            print('\nRecibo do Empréstimo')
            print(f'Nome do livro: {livro}\nTipo de Usuário: {usuario_str}\nTotal de dias para devolver: {dias} dias.')
        else:
            print("Tipo de usuário inválido! Preencha com 1 ou 2.")
    except ValueError:
        print("Valor inválido!Somente são aceitos nomes em formato de texto")
     

#22. Construa um programa que leia o percurso em quilômetros, o tipo do carro e
#informe o consumo estimado de combustível, sabendo-se que um carro tipo A faz
#12 km com um litro de gasolina, um tipo B faz 9 km e o tipo C 8 km por litro.

def q22():
    try:
        distancia = int(input("Informe a distância percorrida (Km): "))
        carro = input("Informe o tipo do carro [A], [B] ou [C]: ")

        if carro == 'A':
            consumo = distancia/12
            print(f"O consumo estimado para o carro tipo A é de {consumo:.2f} Litros")
        elif carro == 'B':
            consumo = distancia/9
            print(f"O consumo estimado para o carro tipo B é de {consumo:.2f} Litros")
        elif carro == 'C':
            consumo = distancia/8
            print(f"O consumo estimado para o carro tipo C é de {consumo:.2f} Litros")
        else:
            print("Tipo de carro inválido! Escolha entre A, B ou C.")
    except ValueError:
        print("Valor inválido! Informe a distancia em números inteiros")

#23. Crie um programa que informe a quantidade total de calorias de uma refeição
#a partir da escolha do usuário que deverá informar o prato, a sobremesa, e
#bebida conforme a tabela a seguir.
#Prato  Sobremesa   Bebida
#Vegetariano    180cal Abacaxi          75cal  Chá               20cal
#Peixe          230cal Sorvete diet     110cal Suco de laranja   70cal
#Frango         250cal Mousse diet      170cal Suco de melão     100cal
#Carne          350cal Mousse chocolate 200cal Refrigerante diet 65cal

def q23():
    try:
        print("\nCardápio\nPrato     Sobremesa     Bebida\nVegetariano[1]     Abacaxi[1]     Chá[1]\nPeixe[2]     Sorvete Diet[2]     Suco de Laranja[2]\nFrango[3]     Mousse diet[3]     Suco de melâo[3]\nCarne[4]     Mousse de Chocolate[4]     Refrigerante Diet[4]")
        prato = input("\nEscolha seu prato de 1-4: ")
        sobremesa = input("\nEscolha sua sobremesa de 1-4: ")
        bebida = input("\nEscolha sua bebida de 1-4: ")

        if prato == '1':
            opçao_prato = 180
        elif prato == '2':
            opçao_prato = 230
        elif prato == '3':
            opçao_prato = 250
        elif prato == '4':
            opçao_prato = 350
        else:
            print("Opção inválida! preencha entre 1 e 4")

        if sobremesa == '1':
            opçao_sobremesa = 75
        elif sobremesa == '2':
            opçao_sobremesa = 110
        elif sobremesa == '3':
            opçao_sobremesa = 170
        elif sobremesa == '4':
            opçao_sobremesa = 200
        else:
            print("Opção inválida! preencha entre 1 e 4")

        if bebida == '1':
            opçao_bebida = 20
        elif bebida == '1':
            opçao_bebida = 70
        elif bebida == '1':
            opçao_bebida = 100
        elif bebida == '1':
            opçao_bebida = 65
        else:
            print("Opção inválida! preencha entre 1 e 4")

        calorias = (opçao_prato + opçao_sobremesa + opçao_bebida)

        print(f"\nA quantidade total de calorias das opções escolhidas é de {calorias} cal")
    except ValueError:
        print("Valor inválido!Somente são aceitos opções em formato de texto")

#24. A polícia rodoviária resolveu fazer cumprir a lei e vistoriar veículos para
#cobrar dos motoristas o DUT. Sabendo-se que o mês em que o emplacamento do
#carro deve ser renovado é determinado pelo último número da placa do mesmo,
#faça um programa que, a partir da leitura da placa do carro, informe o mês
#em que o emplacamento deve ser renovado.

#25. A prefeitura contratou uma firma especializada para manter os níveis de
#poluição considerados ideais para um país do 1º mundo. As indústrias,
#maiores responsáveis pela poluição, foram classificadas em três grupos.
#Sabendo-se que a escala utilizada varia de 0,05 e que o índice de poluição
#aceitável é até 0,25, fazer um programa que possa imprimir intimações de
#acordo com o índice e a tabela a seguir:
#Índice Indústrias que receberão intimação
#0,3 1º grupo
#0,4 1º e 2º grupos
#0,5 1º, 2º e 3º grupos

try:
    opcao = int(input('Digite o número da questão: '))
    if opcao < 1 or opcao > 25:
        raise Exception('Questão inválida, valores devem estar entre 1 e 25')
    eval(f'q{opcao}()')
except ValueError:
    print('O número da questão deve ser numérico (inteiro)!')
except Exception as e:
    print(e)
