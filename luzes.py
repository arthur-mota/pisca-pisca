import RPi.GPIO as GPIO
import time
import pisca

# Broadcom
GPIO.setmode(GPIO.BCM)

pisca = pisca.Pisca()
pisca.pinos = [26, 19, 13, 6, 5, 9, 22, 27, 17, 4]

try:
    while True:
        pisca.desligar_tudo()
        pisca.meio_para_borda()
        pisca.desligar_tudo()

        pisca.borda_para_meio()
        time.sleep(0.4)

        for i in range(10):
            pisca.piscar_tudo()

        for i in range(20):
            pisca.piscar_alternado([0,1])
            pisca.piscar_alternado([1,0])
        pisca.desligar_tudo()

        pisca.liga_um_por_um_invertido()
        pisca.desliga_um_por_um()

        for i in range(10):
            pisca.piscar_tudo()

        for i in range(25):
            pisca.piscar_aleatorio(3)

        for i in range(5):
            pisca.piscar_tudo()

        pisca.desligar_tudo()
        pisca.liga_um_por_um()
        pisca.desliga_um_por_um()

        for i in range(3):
            pisca.piscar_tudo()

        pisca.desligar_tudo()

        pisca.liga_um_por_um_invertido()
        pisca.desliga_um_por_um_invertido()
        pisca.ligar_tudo()
        time.sleep(3)

except KeyboardInterrupt:
    pass

time.sleep(5)

GPIO.cleanup()
