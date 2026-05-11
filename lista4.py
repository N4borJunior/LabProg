from util import inputint, inputfloat, gerar_palavra
from rich.console import Console
import random
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''

console = Console()

#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1():
    try:
        Números = []

        print("Digite 15 números inteiros: 1")
        for i in range(15):
            num = int(input(f"{i+1}º número: "))
            Números.append(num)

        busca = int(input("Digite o número que deseja buscar na lista: "))
        if busca in Números:
            posição = Números.index(busca)
            print(f"O número {busca} está na posição {posição+1}")
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

#3.1 Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q31():
    numeros: list = [int(random.randint(1, 200)) for _ in range(15)]
    with open('resultado_q31.txt','a') as arquivo:
        arquivo.write('=====================================================')

    print("Listagem numerada:")
    for i, num in enumerate(numeros, start=1):
        if num % 2 == 0:
            arquivo.write(f"{i}: {num} é par")
        else:
            arquivo.write(f"{i}: {num} é impar")           
            
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
        n1: list = round(random.uniform(0.0, 10.0), 1)
        n2: list = round(random.uniform(0.0, 10.0), 1)

        nota1.append(n1)
        nota2.append(n2)

        media = round((n1 + n2) / 2, 1)
        medias.append(media)

        if media >= 7.0:
            sit.append("1-Aprovado")
        else:
            sit.append("2-Reprovado")

    print(f"{'Aluno':<10} | {'Prova 1':<5} | {'Prova 2':<5} | {'Média':<6} | {'Situação'}")

    for i in range(15):
        print(f"{i+1:<10} | {nota1[i]:<7.1f} | {nota2[i]:<7.1f} | {medias[i]:<6.1f} | {sit[i]}")

#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q6():
    pessoas = 20
    salarios: list = []
    Nsalarios: list = []
    porcentagem = 8
    Rsalarios: list = []

    for i in range(pessoas):
        salario = round(random.uniform(1600.00, 5000.00), 2) 
        salarios.append(salario)
        Rsalario = salario*(porcentagem/100)
        Rsalarios.append(Rsalario)
        nsalario = salario + Rsalario
        Nsalarios.append(nsalario)

    for i, num in enumerate(salarios, start=1):
        print(f'{i+1:<9} | {salarios[i]:<9.2f} | {Nsalarios[i]:<9.2f}')


#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q7():
    pcompra = []
    pvenda = []

    for i in range(100):
        compra = round(random.uniform(10.0, 500.0), 2)
        print(f"\nvalor de compra: {compra}")
        venda = round(compra * random.uniform(1.05, 1.25), 2)
        print(f"Valor de venda: {venda}")
    
        pcompra.append(compra)
        pvenda.append(venda)

    lbaixo = 0   
    lmedio = 0   
    lalto = 0     

    for i in range(100):
        compra = pcompra[i]
        venda = pvenda[i]
    
        margem = ((venda - compra) / compra) * 100
    
        if margem < 10:
            lbaixo += 1
        elif 10 <= margem <= 20:
            lmedio += 1
        else:
            lalto += 1

    print(f"Lucro < 10%: {lbaixo} mercadorias")
    print(f"10% <= Lucro <= 20%: {lmedio} mercadorias")
    print(f"Lucro > 20%: {lalto} mercadorias")

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q8():

    estoque = {}

    for i in range(30):
        codigo = str(random.randint(0, 999))
    
        while codigo in estoque:
            codigo = str(random.randint(0, 999))
        
        qtd = random.randint(1, 100)         
        vcompra = round(random.uniform(10.0, 500.0), 2)
        vvenda = round(vcompra * random.uniform(1.2, 1.8), 2)

        estoque[codigo] = {
            'quantidade': qtd,
            'compra': vcompra,
            'venda': vvenda
        }

    print(f"Sucesso: {len(estoque)} produtos cadastrados com dados aleatórios.")

    while True:
        print("\n--- Sistema de Estoque ---")
        print("1 - Listar todos os produtos")
        print("2 - Buscar produto por código")
        print("0 - Sair")
    
        opcao = input("Escolha uma opção: ")
    
        if opcao == '1':
            print(f"\n{'CÓDIGO':<10} | {'QTD':<5} | {'COMPRA (R$)':<12} | {'VENDA (R$)':<12}")
            for cod, dados in estoque.items():
                print(f"{cod:<10} | {dados['quantidade']:<5} | {dados['compra']:<12.2f} | {dados['venda']:<12.2f}")
    
        elif opcao == '2':
            cbusca = input("Digite o código para busca: ")
            if cbusca in estoque:
                p = estoque[cbusca]
                print(f"\n[ Detalhes do Produto {cbusca} ]")
                print(f"Estoque: {p['quantidade']} unidades")
                print(f"Preço de Custo: R$ {p['compra']:.2f}")
                print(f"Preço de Venda: R$ {p['venda']:.2f}")
                print(f"Lucro Unitário: R$ {(p['venda'] - p['compra']):.2f}")
            else:
                print("\nErro: Código não encontrado.")
            
        elif opcao == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
def q9():
    c1 = set(random.sample(range(1, 26), 10))
    c2 = set(random.sample(range(1, 26), 10))

    print(f"Conjunto 1: {sorted(list(c1))}")
    print(f"Conjunto 2: {sorted(list(c2))}")

    print(f"Números em ambos os conjuntos: {sorted(c1 & c2)}")

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
def q10():
    lista1 = list(random.randint(1, 16), 10)

    

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
        if opcao < 1 or opcao > 31:
            raise Exception("Questão inválida, valores devem estar entre 1 e 31")
        eval(f'q{opcao}()')
        erro = False
    except ValueError:
        print('O número da questão deve ser numérico (inteiro)!')
    except Exception as e:
        print(e)
