import os
from pybricks.hubs import EV3Brick 
from pybricks.iodevices import I2CDevice, LUMPDevice 
from pybricks.parameters import Port
from pybricks.ev3devices import Motor 
from pybricks.robotics import DriveBase 
from pybricks.ev3devices import UltrasonicSensor, ColorSensor 
from pybricks.parameters import Stop, Direction 
from pybricks.tools import wait 

#DEFINICOES

ev3 = EV3Brick()

sensorLinha = LUMPDevice(Port.S2)
giroscopio = LUMPDevice(Port.S3) #S3

placa = LUMPDevice(Port.S4) #S4

motor_a_esquerdo = Motor(Port.A, Direction.CLOCKWISE) #antihorario
motor_b_direito = Motor(Port.B, Direction.COUNTERCLOCKWISE) #horario 

bobo = DriveBase(motor_a_esquerdo, motor_b_direito, 48, 116)
bobo.settings(300, 1000, 400, 1000)