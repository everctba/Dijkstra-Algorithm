from curses.ascii import controlnames
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
      self.y = j
      self.start = False
      self.wall = False
      self.target = False
      
   def draw(self, win, color):
      pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 1, box_height - 1))

# Create Grid
for i in range(columns):
   arr = []
   for j in range(rows):
      # print("j = ", j)
      arr.append(Box(i,j))
   grid.append(arr)


def main():
   begin_search = False
   target_box_set = False
   
   while True:
      for event in pygame.event.get():
         #Quit Window
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         # Mouse control
         elif event.type == pygame.MOUSEMOTION:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
         # DraWall
         if event.button[2]:
            i = x // box_width
            j = y // box_height
            target_box = grid[i][j]
            target_box.target = True
            target__box_set = True
            
         # Start Algorithm
         if event.type == pygame.KEYDOWN
            begin_search = True

            
      window.fill((0,0,0))
      
      for i in range(columns):
         for j in range(rows):
            box = grid[i][j]
            box.draw(window, (50, 50, 50))
      
      pygame.display.flip()
      
main()

