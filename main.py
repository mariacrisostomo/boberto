#!/usr/bin/env pybricks-micropython
from definicoes import motor_a_esquerdo, motor_b_direito
import crono
import basico as basic
import funcs as func
import definicoes as defs
import sensor

kp = 1.27 #1.27 
kd = 1.1 # 1
erro_anterior = 0
rampa = False

motor_a_esquerdo.reset_angle(0)
motor_b_direito.reset_angle(0)

def erro():
    erro = (sensor.CorEsquerdaEXvendra() + sensor.CorEsquerdaVendra()) - (sensor.CorDireitaVendra() + sensor.CorDireitaEXvendra())
    return erro

run = 1
while run == 1:
    crono.relogio.reseta()
    crono.reset()

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
    
    # func.obstaculo()
    # func.girar90()
    func.verde()
    # func.gap()

    

    erroo = erro()
    p = erroo * kp 
    d = erroo - erro_anterior * kd
    vb = 75

    
    valor = p + d #variacao da potencia do motor

    motor_a_esquerdo.dc(vb - valor) # -
    motor_b_direito.dc(vb + valor) # +

    erro_anterior = erroo

    while crono.relogio.tempo() < 25:
        continue