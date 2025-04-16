from definicoes import sensorLinha, placa 
import basico as basic

def sensoresdecor():
    return sensorLinha.read(2)[20], sensorLinha.read(2)[21], sensorLinha.read(2)[22], \
    sensorLinha.read(2)[23], sensorLinha.read(2)[24], sensorLinha.read(2)[25], \
    sensorLinha.read(2)[26], sensorLinha.read(2)[27], sensorLinha.read(2)[28]

def sensordecorDir():
    return sensorLinha.read(2)[20], sensorLinha.read(2)[21], sensorLinha.read(2)[22]
    
def sensordecorMeio():
    return sensorLinha.read(2)[23], sensorLinha.read(2)[24], sensorLinha.read(2)[25]

def sensordecorEs():
    return sensorLinha.read(2)[26], sensorLinha.read(2)[27], sensorLinha.read(2)[28]

def sensoresdecor2():
    return sensordecorEs(), sensordecorMeio(), sensordecorDir()

# SENSORES DE SEGUIR LINHA
branco = 85
preto = 35

ESQ = 1
DIR = 2

VERMELHO = 3
VERDE = 4

FRENTE = 5
TRAS = 6
PRATA = 7

#checa se está vendo vermelho
def checarcor(sensor):
    

    h = sensor[0]
    s = sensor[1]
    v = sensor[2]

    # print(h,s,v)

    # verde
    if (53 >= h >= 24) and (s >= 35) and (v > 10):

        # wait(25)

        # if (57 >= h >= 20) and (s >= 32) and (v > 10):

        # wait(1)
        # if (55 >= h >= 25) and (s >= 40) and (v > 10):
            # beep(100,50)
        # print(VERDE)
        return VERDE
    
    #prata   
    if (3 >= h) and (3 >= s) and (v > 110):

        # basic.beep()
        return PRATA

        
    # elif ((15 >= h >= 0) or (125 >= h >= 103)) and (s >= 35) and (v > 9): #VERMELHO

    #     wait(50)

    #     if ((15 >= h >= 0) or (125 >= h >= 103)) and (s >= 35) and (v > 9): 

    #     # wait(1)
    #     # if ((10 >= h >= 0) or (120 >= h >= 110))and (s >= 40) and (v > 10):
    #         beep(300,100)
    #         print("vermelho")
    #         return VERMELHO
    
    else:
        return "erro"

# cor do sensor da esquerda do meio
def CorEsquerdaVendra():
    return sensorLinha.read(2)[2]

# cor do sensor da esquerda extrema
def CorEsquerdaEXvendra():
    return sensorLinha.read(2)[3]

# cor do sensor da direita do meio
def CorDireitaVendra():
    return sensorLinha.read(2)[1]

# cor do sensor da direita extrema
def CorDireitaEXvendra():
    return sensorLinha.read(2)[0]

def todos_linha():
    return (CorEsquerdaEXvendra(), CorEsquerdaVendra(), CorDireitaVendra(), CorDireitaEXvendra())

## direita e da esquerda juntos

def sensoresDir():
    return (CorDireitaVendra() + CorDireitaEXvendra()) / 2

def sensoresEs():
    return (CorEsquerdaEXvendra() + CorEsquerdaVendra()) / 2

# o index 0 é o da direita

def tudobranco():
    if CorEsquerdaVendra() > branco and CorEsquerdaEXvendra() > branco and CorDireitaVendra() > branco and CorDireitaEXvendra() > branco:
        basic.beep()
        return True
    else:
        return False

def viupreto():

    if CorEsquerdaVendra() < preto or CorEsquerdaEXvendra() < preto or CorDireitaVendra() < preto or CorDireitaEXvendra() < preto:
        return True 
    else:
        return False

def dist(): #sensor a laser, medida em milimetros
    return placa.read(0)[2]