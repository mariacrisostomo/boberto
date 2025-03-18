import os
import sensor
import basico as basic
from sensor import giro

from motor import angle_d, angle_e

import crono

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

def pararMotores():
    motor_a_esquerdo.stop()
    motor_b_direito.stop()
    motor_a_esquerdo.brake()
    motor_b_direito.brake()


def beep(frequencia: int = 100, duracao: int = 100):
    comando = "beep -f " + str(frequencia) + " -l " + str(duracao) + " &"
    os.system(comando)

def girargraus(graus, direcao):
    erro = 1

    motor_a_esquerdo.reset_angle(0)
    motor_b_direito.reset_angle(0)

    grauss = graus * 0.90

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
    dist = mm * 6.6

    if dir == FRENTE:
        ang_inicial_d = angle_d()
        ang_inicial_e = angle_e()

        while angle_d() < ang_inicial_d + dist and angle_e() < ang_inicial_e + dist:
            
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

            crono.reset()
            motor_a_esquerdo.dc(-vb)
            motor_b_direito.dc(-vb)

        # motor_a_esquerdo.hold()
        # motor_b_direito.hold()
        motor_a_esquerdo.brake()
        motor_b_direito.brake()

        # beep(1000, 50)

def girarate(direc): #GIRA ATE VER PRETO
    # if sensor.tudobranco() == True:
    if direc == ESQ:
        while True:
            if sensor.tudobranco() == False:
                print(sensor.todos_linha())
                beep()
                break
            crono.reset()
            motor_a_esquerdo.dc(80)
            motor_b_direito.dc(-80)

            pararMotores()

        basic.beep()
        # basic.girargraus(30, ESQ)

    elif direc == DIR:
        while True:
            if sensor.tudobranco() == False:
                print(sensor.todos_linha())
                beep()
                break
            crono.reset()
            motor_a_esquerdo.dc(-80)
            motor_b_direito.dc(80)

            pararMotores()
        
        basic.beep()
        # basic.girargraus(30, DIR)

def jinglebell():
    defs.ev3.speaker.play_notes(["D4/4", "D4/4", "D4/2", "Db4/4", "Db4/4", "Db4/2", "B3/4", "Db4/4", "B3/2", "F#3/3"], 238)