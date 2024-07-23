from tkinter import messagebox, Tk 
import pygame
import sys

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dijkstra Algorithm do Youtube tutorial: https://www.youtube.com/watch?v=QNpUN8gBeLY&ab_channel=MaxonTech")

columns = 25
rows = 25

box_width = WINDOW_WIDTH // columns
box_height = WINDOW_HEIGHT // rows

grid = []

class Box:
   def __init__(self, i, j):
      self.x = i
      self.j = j
      
      def draw(self, win, color):
         pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 2, box_height - 2))

# Create Grid
for i in range(columns):
   arr = []
   for j in range(rows):
      # print("j = ", j)
      arr.append(Box(i,j))
   grid.append(arr)


def main():
   while True:
      for event in pygame.event.get():
         #Quit Window
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
      window.fill((0,0,0))
      
      for i in range(columns):
         for j in range(rows):
            box = grid[i][j]
            box.draw(window, (50, 50, 50))
      
      pygame.display.flip()
      
main()
