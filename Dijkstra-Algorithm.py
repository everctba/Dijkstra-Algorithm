from tkinter import messagebox, Tk 
import pygame
import sys

WINDOW_WIDTH = 500
WINDOW_HEIGTH = 500

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGTH))
pygame.display.set_caption("Dijkstra Algorithm do Youtube tutorial: https://www.youtube.com/watch?v=QNpUN8gBeLY&ab_channel=MaxonTech")

def main():
   while True:
      for event in pygame.event.get():
         #Quit Window
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
      window.fill((0,0,0))
      
      pygame.display.flip()
      
main()
