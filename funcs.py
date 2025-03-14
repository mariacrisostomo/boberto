import basico as basic
import definicoes
import sensor
from sensor import checarcor
import motor
import crono

branco = 74
preto = 35

ESQ = 1
DIR = 2

VERMELHO = 3
VERDE = 4

FRENTE = 5
TRAS = 6

def girar90(): #ta funcionando bem, so tem q ajustar o kp e o kd melhor, e a condicao um pouquinho e tentar checar mais
    
    ##se ver 90 checar se tem linha dps, pq se tiver e pra ignorar
    if sensor.CorEsquerdaVendra() < preto - 5 and sensor.CorEsquerdaEXvendra() < preto - 20 and\
        sensor.CorDireitaVendra() > branco - 10 and sensor.CorDireitaEXvendra() > branco + 20:
        print(sensor.todos_linha())

        basic.reto(30)
        if sensor.tudobranco() == True:
            print("ESQ") 
            basic.beep()
            basic.pararMotores()
                
            basic.girarate(ESQ)
            basic.girargraus(30,ESQ)
            basic.reto(30, ATRAS)

    if sensor.CorDireitaVendra() < preto - 5 and sensor.CorDireitaEXvendra() < preto - 5 and\
        sensor.CorEsquerdaVendra() > branco - 30 and sensor.CorEsquerdaEXvendra() > branco - 20:
        print(sensor.todos_linha())
        basic.reto(15)

        if sensor.tudobranco() == True:
            print("DIR") 
            basic.beep()
            basic.pararMotores()

            basic.girarate(DIR)
            basic.girargraus(30,DIR)
            basic.reto(30, ATRAS)


    ## esses numeros que eu to subtraindo nas condicoes q nem o "CorEsquerdaVendra() < preto - 10"
    ## tao servindo pra calibrar o valor minimo q o sensor tem q estar vendo pra ele dar a condicao como verdade com mais precisao
    ## eu to preferindo ver cada sensor individualmente pq e mais preciso doq calcular a media, mas precisa calibrar bem esses valores

def verde(): 
    #CHEGOU TORTO
    if checarcor(sensor.sensordecorMeio()) == VERDE: 
        if crono.PretoDir.tempo() < crono.VerdeMeio.tempo() and crono.PretoEs.tempo() < crono.VerdeMeio.tempo():
            basic.reto(60, TRAS)

    #180
    elif checarcor(sensor.sensordecorEs()) == VERDE and checarcor(sensor.sensordecorDir()) == VERDE:
        # reto(70)

        basic.girargraus(180, DIR)
        basic.reto(30, TRAS)
        print(sensor.sensoresdecor2())
        basic.beep(100)

    #ESQ
    elif (checarcor(sensor.sensordecorEs()) == VERDE and checarcor(sensor.sensordecorDir()) != VERDE):
        basic.reto(7)
        if crono.PretoEsEX.tempo() < crono.VerdeEs.tempo():

            basic.reto(30)
            basic.girargraus(70, ESQ)
            basic.girarate(ESQ)
            basic.reto(10, TRAS)
            print(sensor.sensoresdecor2())
            basic.beep(300)

    #DIR
    elif checarcor(sensor.sensordecorEs()) != VERDE and checarcor(sensor.sensordecorDir()) == VERDE:
        basic.reto(7)
        if crono.PretoDirEX.tempo() < crono.VerdeDir.tempo():
        
            basic.reto(30)
            girargraus(70, DIR)
            girarate(DIR)
            print(sensor.sensoresdecor2())
            reto(10, TRAS)
            beep(1000)

def obstaculo(): #FUNCIONANDO
    if dist() < 100:
        print(dist())
        basic.beep(100, 100)
        # reto(30)
        basic.girargraus(90, ESQ)
        while sensor.tudobranco() == True:
            motor_a_esquerdo.run(300)
            motor_b_direito.run(1100)

        basic.reto(50)
        basic.girargraus(60, ESQ)
    
def gap():
    if sensor.tudobranco() == True:
        basic.reto(147)

        if sensor.tudobranco() == True:
            basic.girargraus(70, ESQ)

            if sensor.tudobranco() == True:
                basic.girargraus(140, DIR)

                if sensor.tudobranco() == True:
                    basic.girargraus(70, ESQ)
                    basic.reto(30)

                    if sensor.tudobranco() == True:
                        while sensor.tudobranco() == True:
                            motor_a_esquerdo.dc(-60)
                            motor_b_direito.dc(-60)