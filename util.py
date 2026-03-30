import random
def inputint(msg, min=None,max=None):
    erro = True
    while (erro == True):
        try:
            valor = int(input(msg))
            if min!=None and valor < min:
                raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
            if max!=None and valor > max:
                raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
            erro = False
            return valor
        except ValueError:
            print ('ERRO: Valor informado não é inteiro!')
        except Exception as erro:
            print(erro)

def inputfloat(msg, min=None,max=None):
    erro = True
    while (erro == True):
        try:
            valor = float(input(msg))
            if min!=None and valor < min:
                raise Exception(f'ERRO: valor é menor do que o mínimo permitido de {min}')
            if max!=None and valor > max:
                raise Exception(f'ERRO: valor é maior do que o máximo permitido de {max}')
            erro = False
            return valor
        except ValueError:
            print ('ERRO: Valor informado não é um número real!')
        except Exception as erro:
            print(erro)

def gerarP(min=4,max=10):
    qtdP = random.randrange(min,max+1)
    palavra = ''
    for _ in range(qtdP):
        palavra += chr(random.randrange(65,91))
    return palavra