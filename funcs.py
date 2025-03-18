import basico as basic
import definicoes
import sensor
from sensor import checarcor
from motor import motor_a_esquerdo, motor_b_direito
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
    # ESQ
    if crono.PretoEsEX.tempo() < crono.PretoDirEX.tempo() and crono.PretoEsEX.tempo() < 100 and crono.PretoDirEX.tempo() > 1000:
        print(sensor.todos_linha())
        basic.beep(500, 50)
        if crono.Fez90.tempo() > 800:

            # basic.pararMotores()
            # input("esq")
            basic.reto(30)
             
            if sensor.tudobranco() == True:
                print("ESQ") 
                basic.beep()
                # basic.pararMotores()
                # basic.girarate(ESQ)
                basic.girargraus(90,ESQ)
                basic.reto(10, TRAS)

                crono.Fez90.reseta()

    # DIR
    if crono.PretoEsEX.tempo() > crono.PretoDirEX.tempo() and crono.PretoEsEX.tempo() > 1000 and crono.PretoDirEX.tempo() < 100:
        print(sensor.todos_linha())
        basic.beep()
        if crono.Fez90.tempo() > 800:

            # basic.pararMotores()
            # input("dir")
            basic.reto(30)
            if sensor.tudobranco() == True:
                print("DIR") 
                basic.beep()
                # basic.pararMotores()

                # basic.girarate(DIR)
                basic.girargraus(90,DIR)
                basic.reto(10, TRAS)

                crono.Fez90.reseta()


    ## esses numeros que eu to subtraindo nas condicoes q nem o "CorEsquerdaVendra() < preto - 10"
    ## tao servindo pra calibrar o valor minimo q o sensor tem q estar vendo pra ele dar a condicao como verdade com mais precisao
    ## eu to preferindo ver cada sensor individualmente pq e mais preciso doq calcular a media, mas precisa calibrar bem esses valores

def verde(): 

    espera = 1600
    #CHEGOU TORTO
    if crono.VerdeMeio.tempo() < 100 and crono.FezVerde.tempo() > espera: ## CERTO
        basic.reto(60, TRAS)

    #180
    elif crono.VerdeEs.tempo() < 150 and crono.VerdeDir.tempo() < 150 and crono.FezVerde.tempo() > espera:
        # reto(70)
        crono.FezVerde.reseta()

        print(sensor.sensoresdecor2())
        basic.girargraus(180, DIR)
        basic.reto(20, TRAS)
        basic.beep(100)

    #ESQ
    elif crono.VerdeEs.tempo() < 100 and crono.VerdeDir.tempo() > 500 and crono.FezVerde.tempo() > espera:
        print("esq")
        print(sensor.sensoresdecor2())
        print(crono.PretoDirEX.tempo(),crono.VerdeDir.tempo())
        print()

        basic.reto(18)
        if crono.PretoEsEX.tempo() < crono.VerdeEs.tempo():
            crono.FezVerde.reseta()
            if crono.VerdeDir.tempo() < 100:
                print(sensor.sensoresdecor2())
                basic.girargraus(180, DIR)
                basic.reto(20, TRAS)
                basic.beep(100)
            else:
                print(crono.PretoEsEX.tempo(),crono.VerdeEs.tempo())

                basic.reto(30)
                basic.girargraus(70, ESQ)
                basic.girarate(ESQ)
                basic.reto(20, TRAS)
                basic.beep(300)

    #DIR
    elif crono.VerdeEs.tempo() > 500 and crono.VerdeDir.tempo() < 100 and crono.FezVerde.tempo() > espera:
        print("dir")
        print(sensor.sensoresdecor2())
        print(crono.PretoDirEX.tempo(),crono.VerdeDir.tempo())

        basic.reto(18)
        if crono.PretoDirEX.tempo() < crono.VerdeDir.tempo():
            crono.FezVerde.reseta()
            if crono.VerdeEs.tempo() < 120:
                print(sensor.sensoresdecor2())
                basic.girargraus(180, DIR)
                basic.reto(20, TRAS)
                basic.beep(100)
            else:
                print(crono.PretoDirEX.tempo(),crono.VerdeDir.tempo())
            
                basic.reto(30)
                basic.girargraus(70, DIR)
                basic.girarate(DIR)
                basic.reto(20, TRAS)
                basic.beep(1000)

def obstaculo(): #FUNCIONANDO
    if sensor.dist() < 100:
        print(sensor.dist())
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