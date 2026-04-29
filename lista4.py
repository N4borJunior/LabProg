from util import inputint, inputfloat, gerar_palavra
import random
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1():
    try:
        Números = []

        print("Digite 15 números inteiros:")
        for i in range(15):
            num = int(input(f"{i+1}º número: "))
            Números.append(num)

        busca = int(input("Digite o número que deseja buscar na lista: "))
        if busca in Números:
            posição = Números.index(busca)
            print(f"O número {busca} está na posição {posição}")
        else:
            print(f"Número {busca} não foi encontrado dentro da lista")
    except ValueError:
        print("Valor Inválido! Somente são aceitos números inteiros.")

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)
def q2():
    letras: list = [chr(random.randint(65, 90)) for _ in range(10)]

    print("Listagem númerada:")
    for i, letra in enumerate(letras, start=1):
        print(f"{i}: {letra}")


#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21():
    try:
        tamanho = int(input("Informe a quantidade de caracteres para a sua senha: "))

        if tamanho <= 0:
            print("Informe um número maior que 0.")
            return
        
        senha = ""

        for i in range(tamanho):
            caractere = chr(random.randint(40,126))
            senha += caractere

        print("Senha aleatória gerada:")
        print(senha)
    except ValueError:
        print("Valor inválido! São aceitos somente números inteiros.")

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3():
    numeros: list = [int(random.randint(1, 200)) for _ in range(15)]

    print("Listagem numerada:")
    for i, num in enumerate(numeros, start=1):
        if num % 2 == 0:
            print(f"{i}: {num} é par")
        else:
            print(f"{i}: {num} é impar")
            
#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4():
    numeros: list = [int(random.randint(1, 200)) for _ in range(8)]

    print(f"Números gerados: {numeros}.")

    multiplos6: int = sum(1 for n in numeros if n % 6 == 0)

    print(f"Quantidade de números que são múltiplos de 6: {multiplos6}.")


#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5():
    nota1: list = []
    nota2: list = []
    medias = []
    sit = []
    alunos = 15

    for i in range(alunos):
        n1: list = [round(random.uniform(0.0, 10.0), 2) for _ in range(15)]
        n2: list = [round(random.uniform(0.0, 10.0), 2) for _ in range(15)]

        nota1.append(n1)
        nota2.append(n2)

        media = round((n1 + n2) / 2, 1)
        medias.append(media)

    print(nota1)

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#uma lista e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

erro = True
while (erro == True):
    try:
        opcao = int(input('Digite o número da questão: '))
        if opcao < 1 or opcao > 21:
            raise Exception("Questão inválida, valores devem estar entre 1 e 21")
        eval(f'q{opcao}()')
        erro = False
    except ValueError:
        print('O número da questão deve ser numérico (inteiro)!')
    except Exception as e:
        print(e)
