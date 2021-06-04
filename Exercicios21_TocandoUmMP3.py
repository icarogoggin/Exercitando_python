#Music: https://www.bensound.com
import pygame
pygame.init()
pygame.mixer.music.load('bensound-memories.mp3')
pygame.mixer.music.play()
pygame.event.wait()