from cronometro import Cronometro
import sensor
from sensor import checarcor
import basico as basic

relogio = Cronometro("tempo") ## MEDE O TEMPO DE EXECUCAO DO ROBO

## CRONOMETRO QUE MEDE O TEMPO DES DE A ULTIMA VEZ QUE VIU ALGO NO SENSOR ESPECIFICADO
VerdeDir = Cronometro() 
VerdeMeio = Cronometro()
VerdeEs = Cronometro()

PretoDirEX = Cronometro()
PretoDir = Cronometro()
PretoEs = Cronometro()
PretoEsEX = Cronometro()

FezVerde = Cronometro()

Fez90 = Cronometro()

#INICIA OS CRONOMETROS
relogio.carrega()

FezVerde.inicia()
Fez90.inicia()

VerdeDir.inicia()
VerdeMeio.inicia()
VerdeEs.inicia()
PretoDirEX.inicia()
PretoDir.inicia()
PretoEs.inicia()
PretoEsEX.inicia()

branco = 74
preto = 20

ESQ = 1
DIR = 2

VERMELHO = 3
VERDE = 4

FRENTE = 5
TRAS = 6

def reset():
    ##reset dos cronometros, pra mostrar quanto tempo faz des de o ultimo momento em que eles viram algo
    if checarcor(sensor.sensordecorDir()) == VERDE: 
        VerdeDir.reseta()
        basic.beep()

    if checarcor(sensor.sensordecorMeio()) == VERDE:
        VerdeMeio.reseta()
        basic.beep()

    if checarcor(sensor.sensordecorEs()) == VERDE:
        VerdeEs.reseta()
        basic.beep()

    if sensor.CorDireitaEXvendra() < preto:
        PretoDirEX.reseta()
    if sensor.CorDireitaVendra() < preto:
        PretoDir.reseta()
    if sensor.CorEsquerdaVendra() < preto:
        PretoEs.reseta()
    if sensor.CorEsquerdaEXvendra() < preto:
        PretoEsEX.reseta()