import basico as basic
import sensor
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
PRATA = 7

def erro():
    erro = (sensor.CorEsquerdaEXvendra() + sensor.CorEsquerdaVendra()) - (sensor.CorDireitaVendra() + sensor.CorDireitaEXvendra())
    return erro

def girar90(): #ta funcionando bem, so tem q ajustar o kp e o kd melhor, e a condicao um pouquinho e tentar checar mais
    # print(crono.PretoEsEX.tempo(),crono.PretoDirEX.tempo())
    ##se ver 90 checar se tem linha dps, pq se tiver e pra ignorar
    # ESQ
    if crono.PretoEsEX.tempo() < 100 and crono.PretoDirEX.tempo() > 800:
        print("ESQ") 
        # print(sensor.todos_linha())
        # basic.beep(500, 50)
        if crono.Fez90.tempo() > 800: #checar se ele fez 90 a pouco tempo

            # basic.pararMotores()
            # input("esq")
            basic.reto(20)
            # basic.hold()
            if crono.PretoEs.tempo() > 60 and crono.PretoDir.tempo() > 60:
                print("ESQ valido") 
                basic.beep()
                # basic.pararMotores()

                # basic.girarate(ESQ)
                basic.girarAtePreto(ESQ)

                basic.reto(10, TRAS)
              
                crono.Fez90.reseta()

    # DIR
    
    if crono.PretoEsEX.tempo() > 800 and crono.PretoDirEX.tempo() < 100:
        print("DIR") 
        # print(sensor.todos_linha())
        # basic.beep()
        if crono.Fez90.tempo() > 800: #checar se ele fez 90 a pouco tempo

            # basic.pararMotores()
            # input("dir")
            basic.reto(20)
            # basic.hold()
            if crono.PretoEs.tempo() > 60 and crono.PretoDir.tempo() > 60:
                print("DIR valido") 
                # basic.beep()
                # basic.pararMotores()

                # basic.girarate(DIR)
                basic.girarAtePreto(DIR)

                
                basic.reto(10, TRAS)
               
                crono.Fez90.reseta()


    ## esses numeros que eu to subtraindo nas condicoes q nem o "CorEsquerdaVendra() < preto - 10"
    ## tao servindo pra calibrar o valor minimo q o sensor tem q estar vendo pra ele dar a condicao como verdade com mais precisao
    ## eu to preferindo ver cada sensor individualmente pq e mais preciso doq calcular a media, mas precisa calibrar bem esses valores

def verde(): 

    espera = 1000
    #CHEGOU TORTO
    if crono.VerdeMeio.tempo() < 100 and crono.FezVerde.tempo() > espera: ## CERTO
        basic.reto(40, TRAS)

    #180
    elif crono.VerdeEs.tempo() < 150 and crono.VerdeDir.tempo() < 150 and crono.FezVerde.tempo() > espera:
        # reto(70)
        crono.FezVerde.reseta()

        print(sensor.sensoresdecor2())
        basic.girargraus(180, DIR)
        basic.reto(20, TRAS)
        # basic.beep(100)

    #ESQ
    elif crono.VerdeEs.tempo() < 100 and crono.VerdeDir.tempo() > 500 and crono.FezVerde.tempo() > espera:
        print("esq")
        print(sensor.sensoresdecor2())
        print(crono.PretoDirEX.tempo(),crono.VerdeDir.tempo())
        print()

        basic.reto(10)
        if crono.PretoEsEX.tempo() < crono.VerdeEs.tempo():
            crono.FezVerde.reseta()
            if crono.VerdeDir.tempo() < 100 and crono.VerdeDir.tempo() < crono.PretoDirEx.tempo():
                print(sensor.sensoresdecor2())
                basic.girargraus(180, DIR)
                basic.reto(20, TRAS)
                # basic.beep(100)
            else:
                print(crono.PretoEsEX.tempo(),crono.VerdeEs.tempo())

                basic.reto(30)
                basic.girargraus(50, ESQ)
                basic.girarAtePreto(ESQ)
                basic.reto(20, TRAS)
                # basic.beep(300)

    #DIR
    elif crono.VerdeEs.tempo() > 500 and crono.VerdeDir.tempo() < 100 and crono.FezVerde.tempo() > espera:
        print("dir")
        print(sensor.sensoresdecor2())
        print(crono.PretoDirEX.tempo(),crono.VerdeDir.tempo())

        basic.reto(10)
        if crono.PretoDirEX.tempo() < crono.VerdeDir.tempo():
            crono.FezVerde.reseta()
            if crono.VerdeEs.tempo() < 100 and crono.VerdeEs.tempo() < crono.PretoEsEX.tempo():
                print(sensor.sensoresdecor2())
                basic.girargraus(180, DIR)
                basic.reto(20, TRAS)
                # basic.beep(100)
            else:
                print(crono.PretoDirEX.tempo(),crono.VerdeDir.tempo())
            
                basic.reto(30)
                basic.girargraus(50, DIR)
                basic.girarAtePreto(DIR)
                basic.reto(20, TRAS)
                # basic.beep(1000)

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
    
def varrer():
    basic.girarAtePreto(ESQ, 90)

    if basic.vendobranco() == True:
        basic.girarAtePreto(DIR, 180)
        
        if basic.vendobranco() == True:
            basic.girarAtePreto(ESQ, 90)



def gap():
    if basic.vendobranco() == True:
        print("gap")

        varrer()
        if basic.vendobranco() == True:
            basic.retoAtePreto(100, TRAS)

            

            basic.retoAtePreto(150)
            if basic.vendobranco() == True:
                varrer()

                basic.reto(200, TRAS)





def rampa(): # TA MUITO ERRADO
    # checa se o robo ta na rampa SUBINDO
    if basic.inclinacao() > 18:
        print("RAMPA SUBIU")
        basic.beep(1000,600)
        # erro_anterior = 0

        erro_anterior = 0
        while basic.inclinacao() > 18:
        # beep()
            vb = 90
            # global erro_anterior
            
            kp = 1.27 # 1.27 
            kd = 1.5 # 1

            erroo = erro()
            p = erroo * kp 
            d = erroo - erro_anterior * kd
            

            valor = p + d #variacao da potencia do motor

            motor_a_esquerdo.run((vb - valor) * 10) # -
            motor_b_direito.run((vb + valor) * 10) # +
            
            erro_anterior = erroo

            #checa se o robo acabou de sair da rampa
            print(basic.inclinacao())
            print("tempo", crono.RampaSubiu.tempo())

            if basic.inclinacao() > 18:
                crono.RampaSubiu.reseta()

            if not(basic.inclinacao() > 18) and crono.RampaSubiu.tempo() > 2000:
                basic.beep(700,100)
                print("RAMPA SUBIU (saiu)")
                break
            
        basic.reto(-40)


    # checa se o robo ta na rampa DESCENDO
    if basic.inclinacao() < -18:
        print("RAMPA DESCEU")
        basic.beep(500,100)
        # erro_anterior = 0

        crono.RampaDesceu.reseta()
        erro_anterior = 0
        while basic.inclinacao() < -18:        
        # beep()
            vb = 50
            # global erro_anterior
            
            kp = 1.27 # 1.27 
            kd = 1 # 1

            erroo = erro()
            p = erroo * kp 
            d = erroo - erro_anterior * kd
            

            valor = p + d #variacao da potencia do motor

            motor_a_esquerdo.dc(vb - valor) # -
            motor_b_direito.dc(vb + valor) # +
            
            erro_anterior = erroo

            print(basic.inclinacao())
            print("tempo", crono.RampaDesceu.tempo())

            #checa se o robo acabou de sair da rampa
            if basic.inclinacao() < -18:
                crono.RampaDesceu.reseta()

            if not(basic.inclinacao() < -18) and crono.RampaDesceu.tempo() > 2000:
                basic.beep(300,100)
                print("RAMPA DESCEU (saiu)")
                break

            
            