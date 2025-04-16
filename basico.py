import os
import sensor
from motor import angle_d, angle_e

import crono
from definicoes import giroscopio

import definicoes as defs
from definicoes import motor_a_esquerdo, motor_b_direito

branco = 74
preto = 35

ESQ = 1
DIR = 2

VERMELHO = 3
VERDE = 4

FRENTE = 5
TRAS = 6

def hold():
    motor_a_esquerdo.hold()
    motor_b_direito.hold()

def inclinacao():
    return giroscopio.read(0)[0]

def giro(): #angulo
    return giroscopio.read(0)[2]

def pararMotores():
    motor_a_esquerdo.stop()
    motor_b_direito.stop()
    motor_a_esquerdo.brake()
    motor_b_direito.brake()

def beep(frequencia: int = 100, duracao: int = 100):
    comando = "beep -f " + str(frequencia) + " -l " + str(duracao) + " &"
    os.system(comando)

def girargraus(graus, direcao):

    motor_a_esquerdo.reset_angle(0)
    motor_b_direito.reset_angle(0)

    grauss = graus * 0.93

    vb = 90

    if direcao == ESQ:

        atual = giro()

        while giro() <= (atual + grauss):
            # print(giro())

            motor_a_esquerdo.dc(vb)
            motor_b_direito.dc(-vb)

    elif direcao == DIR:

        atual = giro()

        while giro() >= (atual - grauss):
            # print(giro())

            motor_a_esquerdo.dc(-vb)
            motor_b_direito.dc(vb)

    beep()
    motor_a_esquerdo.brake()
    motor_b_direito.brake()

def reto(mm, dir = FRENTE, vb = 80): #em mm
    motor_a_esquerdo.reset_angle(0)
    motor_b_direito.reset_angle(0)

    dist = mm * 4 #4

    if dir == FRENTE:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() < ang_inicial_d + dist and angle_e() < ang_inicial_e + dist:
            
            crono.reset()
            motor_a_esquerdo.dc(vb)
            motor_b_direito.dc(vb)



    elif dir == TRAS:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() > ang_inicial_d - dist and angle_e() > ang_inicial_e - dist:

            crono.reset()
            motor_a_esquerdo.dc(-vb)
            motor_b_direito.dc(-vb)

    # if hold == True:
    #     motor_a_esquerdo.hold()
    #     motor_b_direito.hold()
    # else:
    motor_a_esquerdo.brake()
    motor_b_direito.brake()

        # beep(1000, 50)

def retoAtePreto(mm, dir = FRENTE, vb = 80):
    motor_a_esquerdo.reset_angle(0)
    motor_b_direito.reset_angle(0)

    dist = mm * 4 #4

    if dir == FRENTE:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() < ang_inicial_d + dist and angle_e() < ang_inicial_e + dist:
            if crono.PretoDir.tempo() < 80 or crono.PretoEs.tempo() < 80:
                print(sensor.todos_linha())
                # beep()
                break
            
            crono.reset()
            motor_a_esquerdo.dc(vb)
            motor_b_direito.dc(vb)

        # motor_a_esquerdo.hold() #hold para a inercia do robo
        # motor_b_direito.hold()
        motor_a_esquerdo.brake()
        motor_b_direito.brake()
        
        # beep()

    elif dir == TRAS:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() > ang_inicial_d - dist and angle_e() > ang_inicial_e - dist:
            if crono.PretoDir.tempo() < 80 or crono.PretoEs.tempo() < 80:
                print(sensor.todos_linha())
                # beep()
                break

            crono.reset()
            motor_a_esquerdo.dc(-vb)
            motor_b_direito.dc(-vb)

        # motor_a_esquerdo.hold()
        # motor_b_direito.hold()
        motor_a_esquerdo.brake()
        motor_b_direito.brake()

        # beep(1000, 50)


def girarAtePreto(direc, graus = None): #GIRA ATE VER PRETO
    # if sensor.tudobranco() == True:

    grauss = 0
    if graus != None:
        grauss = graus * 0.93

    crono.reset()
    if direc == ESQ:
       
        atual = giro()
        while True:
            
            if graus != None:
                if giro() >= (atual + grauss):
                    break

            if crono.PretoDir.tempo() < 80 or crono.PretoEs.tempo() < 80:
                print(sensor.todos_linha())
                # beep()
                break
            crono.reset()
            motor_a_esquerdo.dc(80)
            motor_b_direito.dc(-80)

        pararMotores()

        # beep()
        # basic.girargraus(30, ESQ)

    elif direc == DIR:
         
        atual = giro()
        while True:
            
            if graus != None:
                if giro() <= (atual - grauss):
                    break
            
            if crono.PretoDir.tempo() < 80 or crono.PretoEs.tempo() < 80:

                print(sensor.todos_linha())
                # beep()
                break
            crono.reset()
            motor_a_esquerdo.dc(-80)
            motor_b_direito.dc(80)

        pararMotores()
        
        # beep()
        # basic.girargraus(30, DIR)

    
def vendobranco():
    if crono.PretoEs.tempo() > 150 and crono.PretoDir.tempo() > 150 and crono.PretoDirEX.tempo() > 150 and crono.PretoEsEX.tempo() > 150:
        return True
    else:
        return False

    #no lugar do tudo branco, eu simplesmente checo se os sensores do meio estao vendo preto agr pelo cronometro

def jinglebell():
    defs.ev3.speaker.play_notes(["D4/4", "D4/4", "D4/2", "Db4/4", "Db4/4", "Db4/2", "B3/4", "Db4/4", "B3/2", "F#3/3"], 238)