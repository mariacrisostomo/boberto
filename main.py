#!/usr/bin/env pybricks-micropython
import os
from pybricks.hubs import EV3Brick # type: ignore
from pybricks.iodevices import I2CDevice, LUMPDevice # type: ignore
from pybricks.parameters import Port # type: ignore
from pybricks.ev3devices import Motor # type: ignore
from pybricks.robotics import DriveBase # type: ignore
from pybricks.ev3devices import UltrasonicSensor, ColorSensor # type: ignore
from pybricks.parameters import Stop, Direction # type: ignore
from pybricks.tools import wait # type: ignore
from cronometro import Cronometro

import time

#DEFINICOES

ev3 = EV3Brick()

sensorLinha = LUMPDevice(Port.S2)
giroscopio = LUMPDevice(Port.S3) #S3

placa = LUMPDevice(Port.S4) #S4

motor_a_esquerdo = Motor(Port.A, Direction.CLOCKWISE) #antihorario
motor_b_direito = Motor(Port.B, Direction.COUNTERCLOCKWISE) #horario 

#AS PORTAS E ETC TAO ERRADAS PQ EU TO TESTANDO EM OUTRO ROBO

bobo = DriveBase(motor_a_esquerdo, motor_b_direito, 48, 116)
bobo.settings(300, 1000, 400, 1000)

branco = 74
preto = 35

ESQ = 1
DIR = 2

VERMELHO = 3
VERDE = 4

FRENTE = 5
TRAS = 6

#relacionado aos sensores
#region 

## VALORES HSV
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

#checa se está vendo vermelho
def checarcor(sensor):

    h = sensor[0]
    s = sensor[1]
    v = sensor[2]

    # verde
    if (57 >= h >= 20) and (s >= 32) and (v > 10):

        wait(25)

        if (57 >= h >= 20) and (s >= 32) and (v > 10):

        # wait(1)
        # if (55 >= h >= 25) and (s >= 40) and (v > 10):
            # beep(100,50)
        # print(VERDE)
            return VERDE
        
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

        wait(50)

        if CorEsquerdaVendra() > branco and CorEsquerdaEXvendra() > branco and CorDireitaVendra() > branco and CorDireitaEXvendra() > branco:
            return True
    else:
        return False

def viupreto():

    if CorEsquerdaVendra() < preto or CorEsquerdaEXvendra() < preto or CorDireitaVendra() < preto or CorDireitaEXvendra() < preto:

        wait(50)

        if CorEsquerdaVendra() < preto or CorEsquerdaEXvendra() < preto or CorDireitaVendra() < preto or CorDireitaEXvendra() < preto:
            return True 
    else:
        return False
#endregion

## FUNÇÕES BASICAS
#region

def pararMotores():
    bobo.stop()
    motor_a_esquerdo.brake()
    motor_b_direito.brake()
    motor_a_esquerdo.stop()
    motor_b_direito.stop()

def giro(): #angulo
    return giroscopio.read(0)[2]

def inclinacao():
    return giroscopio.read(0)[0]

def dist(): #sensor a laser, medida em milimetros
    return placa.read(0)[2]

def angle_d():
    return motor_b_direito.angle()

def angle_e():
    return motor_a_esquerdo.angle()

def erro():
    erro = (CorEsquerdaEXvendra() + CorEsquerdaVendra()) - (CorDireitaVendra() + CorDireitaEXvendra())
    return erro

def girargraus(graus, direcao):
    erro = 1

    motor_a_esquerdo.reset_angle(0)
    motor_b_direito.reset_angle(0)

    grauss = graus * 0.90

    vb = 90

    if direcao == ESQ:

        atual = giro()

        while giro() <= (atual + grauss):
            print(giro())

            motor_a_esquerdo.dc(vb)
            motor_b_direito.dc(-vb)

    elif direcao == DIR:

        atual = giro()

        while giro() >= (atual - grauss):
            print(giro())

            motor_a_esquerdo.dc(-vb)
            motor_b_direito.dc(vb)

    beep()
    motor_a_esquerdo.brake()
    motor_b_direito.brake()

def girargraus_errado(gr, direc):
    pararMotores()
    graus = gr * 3.2

    if direc == ESQ:
        bobo.turn(graus)
    elif direc == DIR:
        bobo.turn(-graus)
    pararMotores()

def reto_errado(mm):
    pararMotores()
    bobo.straight(mm * 2.05)
    pararMotores()

def reto(mm, dir = FRENTE, vb = 90): #em mm
    motor_a_esquerdo.reset_angle(0)
    motor_b_direito.reset_angle(0)
    dist = mm * 6.6

    if dir == FRENTE:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() < ang_inicial_d + dist and angle_e() < ang_inicial_e + dist:
            
            cronoreset()
            motor_a_esquerdo.dc(vb)
            motor_b_direito.dc(vb)

        motor_a_esquerdo.hold() #hold para a inercia do robo
        motor_b_direito.hold()
        
        # beep()

    elif dir == TRAS:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() > ang_inicial_d - dist and angle_e() > ang_inicial_e - dist:

            cronoreset()
            motor_a_esquerdo.dc(-vb)
            motor_b_direito.dc(-vb)

        motor_a_esquerdo.hold()
        motor_b_direito.hold()

        # beep(1000, 50)

def girarate(direc): #GIRA ATE VER PRETO
    if tudobranco() == True:
        if direc == ESQ:
            while tudobranco() == True:
                cronoreset()
                motor_a_esquerdo.dc(80)
                motor_b_direito.dc(-80)
            girargraus(30, ESQ)

        elif direc == DIR:
            while tudobranco() == True:
                cronoreset()
                motor_a_esquerdo.dc(-80)
                motor_b_direito.dc(80)
            girargraus(30, DIR)

def cronoreset():
    ##reset dos cronometros, pra mostrar quanto tempo faz des de o ultimo momento em que eles viram algo
    if checarcor(sensordecorDir()) == VERDE: 
        tempoVerdeDir.reseta()
        beep()

    if checarcor(sensordecorMeio()) == VERDE:
        tempoVerdeMeio.reseta()
        beep()

    if checarcor(sensordecorEs()) == VERDE:
        tempoVerdeEs.reseta()
        beep()

    if CorDireitaEXvendra() < preto:
        tempoPretoEsEX.reseta()
    if CorDireitaVendra() < preto:
        tempoPretoEs.reseta()
    if CorEsquerdaVendra() < preto:
        tempoPretoDir.reseta()
    if CorEsquerdaEXvendra() < preto:
        tempoPretoDirEX.reseta()

def jinglebell():
    ev3.speaker.play_notes(["D4/4", "D4/4", "D4/2", "Db4/4", "Db4/4", "Db4/2", "B3/4", "Db4/4", "B3/2", "F#3/3"], 238)

def beep(frequencia: int = 100, duracao: int = 100):
      comando = "beep -f " + str(frequencia) + " -l " + str(duracao) + " &"
      os.system(comando)

#endregion

#FUNCOES PRINCIPAIS
#region

def noventasemverde(): #ta funcionando bem, so tem q ajustar o kp e o kd melhor, e a condicao um pouquinho e tentar checar mais
    
    ##se ver 90 checar se tem linha dps, pq se tiver e pra ignorar

    # if CorEsquerdaVendra() < preto and CorEsquerdaEXvendra() < preto and CorDireitaVendra() > branco - 20 and CorDireitaEXvendra() > branco - 20:
    #     wait(25)
    if CorEsquerdaVendra() < preto - 5 and CorEsquerdaEXvendra() < preto - 5 and CorDireitaVendra() > branco - 30 and CorDireitaEXvendra() > branco - 20:
        reto(15)
        if tudobranco() == True:
            print("ESQ") 
            print(todos_linha())
            beep()
            pararMotores()
            reto(15)
            # if tudobranco == True:
                
            while tudobranco() == True:
                girarate(ESQ)

            girargraus(30,ESQ)
            reto(-30)

    # if CorDireitaVendra() < preto and CorDireitaEXvendra() < preto and CorEsquerdaVendra() > branco - 20 and CorEsquerdaEXvendra() > branco - 20:
    #     wait(25)
    if CorDireitaVendra() < preto - 5 and CorDireitaEXvendra() < preto - 5 and CorEsquerdaVendra() > branco - 30 and CorEsquerdaEXvendra() > branco - 20:
        reto(15)
        if tudobranco() == True:
            print("DIR") 
            print(todos_linha())
            beep()
            pararMotores()
            reto(15)
            # if tudobranco == True:
            
            while tudobranco() == True:
                girarate(DIR)
            girargraus(30,DIR)
            reto(-30)


    ## esses numeros que eu to subtraindo nas condicoes q nem o "CorEsquerdaVendra() < preto - 10"
    ## tao servindo pra calibrar o valor minimo q o sensor tem q estar vendo pra ele dar a condicao como verdade com mais precisao
    ## eu to preferindo ver cada sensor individualmente pq e mais preciso doq calcular a media, mas precisa calibrar bem esses valores

def verde(): 
    #CHEGOU TORTO
    if checarcor(sensordecorMeio()) == VERDE: 
        if tempoPretoDir.tempo() < tempoVerdeMeio.tempo() and tempoPretoEs.tempo() < tempoVerdeMeio.tempo():
            reto(60, TRAS)

    #180
    elif checarcor(sensordecorEs()) == VERDE and checarcor(sensordecorDir()) == VERDE:
        # reto(70)

        girargraus(180, DIR)
        reto(30, TRAS)
        print(sensoresdecor2())
        beep(100)

    #ESQ
    elif (checarcor(sensordecorEs()) == VERDE and checarcor(sensordecorDir()) != VERDE):
        reto(7)
        if tempoPretoEsEX.tempo() < tempoVerdeEs.tempo():

            reto(30)
            girargraus(70, ESQ)
            girarate(ESQ)
            reto(10, TRAS)
            print(sensoresdecor2())
            beep(300)

    #DIR
    elif checarcor(sensordecorEs()) != VERDE and checarcor(sensordecorDir()) == VERDE:
        reto(7)
        if tempoPretoDirEX.tempo() < tempoVerdeDir.tempo():
        
            reto(30)
            girargraus(70, DIR)
            girarate(DIR)
            print(sensoresdecor2())
            reto(10, TRAS)
            beep(1000)

def obstaculo(): #FUNCIONANDO
    if dist() < 100:
        print(dist())
        beep(100, 100)
        # reto(30)
        girargraus(90, ESQ)
        while tudobranco() == True:
            motor_a_esquerdo.run(300)
            motor_b_direito.run(1100)


        reto(50)
        girargraus(60, ESQ)
    
def gap():
    if tudobranco() == True:
        reto(147)

        if tudobranco() == True:
            girargraus(70, ESQ)

            if tudobranco() == True:
                girargraus(140, DIR)

                if tudobranco() == True:
                    girargraus(70, ESQ)
                    reto(30)

                    if tudobranco() == True:
                        while tudobranco() == True:
                            motor_a_esquerdo.dc(-60)
                            motor_b_direito.dc(-60)

    #substituir esse final pra aql ngc q salva a posicao atual no inicio do gap e guarda a quantidade de milimetros que ele andou
    #e usar esse numero pra voltar
    #dai eu unitilizaria o reto
#endregion

##DEFINICOES

## RELOGIOS
#region
relogio = Cronometro("tempo") ## MEDE O TEMPO DE EXECUCAO DO ROBO

## CRONOMETRO QUE MEDE O TEMPO DES DE A ULTIMA VEZ QUE VIU ALGO NO SENSOR ESPECIFICADO
tempoVerdeDir = Cronometro() 
tempoVerdeMeio = Cronometro()
tempoVerdeEs = Cronometro()

tempoPretoDirEX = Cronometro()
tempoPretoDir = Cronometro()
tempoPretoEs = Cronometro()
tempoPretoEsEX = Cronometro()

#CARREGA E INICIA OS CRONOMETROS
relogio.carrega()

tempoVerdeDir.carrega()
tempoVerdeDir.inicia()
tempoVerdeMeio.carrega()
tempoVerdeMeio.inicia()
tempoVerdeEs.carrega()
tempoVerdeEs.inicia()

tempoPretoDirEX.carrega()
tempoPretoDirEX.inicia()
tempoPretoDir.carrega()
tempoPretoDir.inicia()
tempoPretoEs.carrega()
tempoPretoEs.inicia()
tempoPretoEsEX.carrega()
tempoPretoEsEX.inicia()
# endregion

kp = 1.27 #1.27
kd = 1.1 # 1
erro_anterior = 0
rampa = False

motor_a_esquerdo.reset_angle(0)
motor_b_direito.reset_angle(0)

# girargraus_errado(90, ESQ)
# girargraus_errado(90, ESQ)

run = 1
while run == 1:
    relogio.reseta()

    # noventasemverde()
    verde()
    # obstaculo()
    # gap()

    cronoreset()

    erroo = erro()
    p = erroo * kp 
    d = erroo - erro_anterior * kd

    vb = 100

    #region RAMPA (TA DANDO CERTO)
    # # checa se o robo ta na rampa
    # if inclinacao() < -17:
    #     # beep()
    #     rampa = True

    # #checa se o robo acabou de sair da rampa
    # if rampa == True and not(inclinacao() < -17):
    #     beep()
    #     rampa = False
    #     reto(-40)
    #endregion
    
    valor = p + d #variacao da potencia do motor

    motor_a_esquerdo.dc(vb - valor) # -
    motor_b_direito.dc(vb + valor) # +

    erro_anterior = erroo

    # print(dist())
    # print(todos_linha())
    # print(sensoresdecor2())
    # print(inclinacao())


    while relogio.tempo() < 25:
        continue

#COMENTA ESSA MERDA, tudo oque você faz tem que ser entendivel

#antes de mecher com as funcoes tem q ajustar BEM o kp e kd

#dps disso calibrar BEM as condicoes q ativam as funcoes, pra n ficar ativando em momentos errados
#fica pedindo so pra beepar, e n fazer mais nada
#dai dps comeca a trabalhar nas funcoes em si


#LEMBRAR DE CALIBRAR DIREITO NO ROBO E CRIAR FUNCAO Q CALIBRA SOZINHO TBM