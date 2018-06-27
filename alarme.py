from datetime import datetime
import pygame
import time

pygame.mixer.init()


hora = datetime.now().strftime('%H:%M')
despertar = input("Qual hora quer que desperte?\n")

while True:
    if despertar == hora:
        pygame.mixer.music.load('alerta.wav')
        pygame.mixer.music.play(0)
        time.sleep(30)
