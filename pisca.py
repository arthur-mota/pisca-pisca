import RPi.GPIO as GPIO
import random
import time
import math

# Broadcom
GPIO.setmode(GPIO.BCM)

class Pisca:
    pinos = []

    # Acende um LED específico
    def ligar_pino(self, pino):
        print("Ligando pino " + str(pino) + "...")
        GPIO.setup(pino, GPIO.OUT)
        GPIO.output(pino, GPIO.HIGH)

    # Desliga um LED específico
    def desligar_pino(self, pino):
        print("Desligando pino " + str(pino) + "...")
        GPIO.setup(pino, GPIO.OUT)
        GPIO.output(pino, GPIO.LOW)

    # Acende todos os LEDs
    def ligar_tudo(self):
        for pino in self.pinos:
            self.ligar_pino(pino)

    # Deliga todos os LEDs
    def desligar_tudo(self):
        for pino in self.pinos:
            self.desligar_pino(pino)

    # Liga e desliga tudo, com um pequeno delay
    def piscar_tudo(self):
        intervalo = 0.1
        self.desligar_tudo()
        time.sleep(intervalo)
        self.ligar_tudo()
        time.sleep(intervalo)

    # Acende pino por pino em ordem, com um pequeno delay entre cada um
    def liga_um_por_um(self):
        for pino in self.pinos:
            self.ligar_pino(pino)
            time.sleep(0.25)

    # um_por_um invertido (começa do final da lista)
    def liga_um_por_um_invertido(self):
        pinos_invertidos = reversed(self.pinos)
        for pino in pinos_invertidos:
            self.ligar_pino(pino)
            time.sleep(0.25)

    # Desliga pino por pino em ordem, com um pequeno delay entre cada um
    def desliga_um_por_um(self):
        for pino in self.pinos:
            self.desligar_pino(pino)
            time.sleep(0.25)

    def desliga_um_por_um_invertido(self):
        pinos_invertidos = reversed(self.pinos)
        for pino in pinos_invertidos:
            self.desligar_pino(pino)
            time.sleep(0.25)

    # Pisca luz aleatória (qnt = quantidade de luzes ligadas ao mesmo tempo)
    def piscar_aleatorio(self, qnt):
        intervalo = 0.075
        # Desliga tudo primeiro
        self.desligar_tudo()
        # Pinos escolhidos para piscar
        pinos_escolhidos = []
        # Duplica self.pinos
        pinos = list(self.pinos)

        # Escolhe x pinos (x = qnt)
        for i in range(qnt):
            # Seleciona pino aleatório para piscar
            pino = random.choice(pinos)
            # Adiciona esse pino a pinos_escolhidos
            pinos_escolhidos.append(pino)
            # Remove o pino selecionado da lista, para não duplicar
            pinos.remove(pino)

        # Pisca os pinos_escolhidos
        for pino in pinos_escolhidos:
            self.ligar_pino(pino)
        time.sleep(intervalo)
        for pino in pinos_escolhidos:
            self.desligar_pino(pino)
        time.sleep(intervalo)

    # Pisca luzes alternadamente (índices pares acesos, ímpares apagados, por exemplo)
    def piscar_alternado(self, tipo=[0,1]):
        # Tipo = [0, 1] ou [1, 0]

        intervalo = 0.115
        for indice, pino in enumerate(self.pinos):
            if indice == 0 or indice % 2 == 0:
                self.__liga_ou_desliga(tipo[0], pino)
            elif indice % 2 != 0:
                self.__liga_ou_desliga(tipo[1], pino)
        time.sleep(intervalo)

    # Acende da borda para o meio, com simetria
    def borda_para_meio(self):
        # indices_atuais = [primeiro índice de self.pinos, último índice de self.pinos]
        indices_atuais = [0, len(self.pinos)-1]
        # índice do meio da array (ou do primeiro elemento do [x, y], se len(array) for par)
        indice_meio = (math.ceil(len(self.pinos)/2))-1

        while not indice_meio in indices_atuais:
            # Liga o pino do primeiro índice e aumenta índice em 1
            self.ligar_pino(self.pinos[indices_atuais[0]])
            indices_atuais[0] += 1

            # Liga o pino do segundo índice e diminui índice em 1
            self.ligar_pino(self.pinos[indices_atuais[1]])
            indices_atuais[1] -= 1

            time.sleep(0.25)

        self.ligar_tudo()

    # Acende do meio para a borda, com simetria
    def meio_para_borda(self):
        intervalo = 0.25
        if len(self.pinos) % 2 == 0:
            # Se self.pinos for par (número par de LEDs)

            # Primeira metade de self.pinos
            # Vai começar a acender do último elemento
            pinos_1 = self.pinos[0:int(len(self.pinos)/2)]
            # Reverte array
            pinos_1 = pinos_1[::-1]

            # Segunda metade de self.pinos
            # Vai começar a acender do primeiro elemento
            pinos_2 = self.pinos[int(len(self.pinos)/2):len(self.pinos)]

            return self.__acende_meio_para_borda(pinos_1, pinos_2, intervalo)

        elif len(self.pinos) % 2 != 0:
            # Se self.pinos for ímpar (número ímpar de LEDs)

            # Primeira metade de self.pinos
            # Esta lista possui um elemento a mais (ímpar)
            # Esse elemento será aceso primeiro, depois removido
            # da lista. Em seguida, acende_meio_para_borda() será chamada.
            pinos_1 = self.pinos[0:math.ceil(len(self.pinos)/2)]

            # Segunda metade de self.pinos
            pinos_2 = self.pinos[math.ceil(len(self.pinos)/2):len(self.pinos)]

            # Acende o último elemento (elemento ímpar) de pinos_1
            self.ligar_pino(pinos_1[-1])
            time.sleep(intervalo)
            # Remove pinos_1[-1]
            pinos_1.remove(pinos_1[-1])
            # Inverte pinos_1
            pinos_1 = pinos_1[::-1]

            return self.__acende_meio_para_borda(pinos_1, pinos_2, intervalo)

    # private

    # Se num == 0, desliga pino, se num == 1, liga pino
    def __liga_ou_desliga(self, num, pino):
        if num == 0:
            return self.desligar_pino(pino)
        elif num == 1:
            return self.ligar_pino(pino)

    def __acende_meio_para_borda(self, pinos_1, pinos_2, intervalo):
        for indice_1, pino_1 in enumerate(pinos_1):
            # Acende o último pino da primeira metade
            self.ligar_pino(pino_1)
            # Acende o primeiro pino da segunda metade
            self.ligar_pino(pinos_2[indice_1])
            time.sleep(intervalo)
