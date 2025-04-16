#!/usr/bin/env pybricks-micropython
from definicoes import motor_a_esquerdo, motor_b_direito, wait
import crono
import basico as basic
import sensor
import funcs as func

branco = 74
preto = 35

ESQ = 1
DIR = 2

VERMELHO = 3
VERDE = 4

FRENTE = 5
TRAS = 6
PRATA = 7

kp = 1.27 # 1.27 
kd = 1 # 1
erro_anterior = 0
rampa = False

motor_a_esquerdo.reset_angle(0)
motor_b_direito.reset_angle(0)

# basic.reto(100, FRENTE, 80)
# basic.girarAtePreto(ESQ, 90)

# while True:
#     motor_a_esquerdo.run(1000) # -
#     motor_b_direito.run(1000) # +

def erro():
    erro = (sensor.CorEsquerdaEXvendra() + sensor.CorEsquerdaVendra()) - (sensor.CorDireitaVendra() + sensor.CorDireitaEXvendra())
    return erro

# error_anterior =0
vb = 85
def pid(vb = vb):
    global erro_anterior
    
    kp = 1.27 # 1.27 
    kd = 1 # 1

    erroo = erro()
    p = erroo * kp 
    d = erroo - erro_anterior * kd
    

    valor = p + d #variacao da potencia do motor

    motor_a_esquerdo.dc(vb - valor) # -
    motor_b_direito.dc(vb + valor) # +
    
    erro_anterior = erroo

wait(1000)
run = 1
while run == 1:
    # # crono.relogio.reseta()
    # crono.reset()
    
    # # func.obstaculo()
    # func.girar90()
    # func.verde()
    # func.gap()
    # # func.rampa()

    # pid()

    func.alinhar()

    # print(sensor.checarcor(sensor.sensordecorMeio()))

    # print(basic.inclinacao())

    # # print(sensor.todos_linha())

    while crono.relogio.tempo() < 25:
        continue