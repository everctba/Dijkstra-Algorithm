# from curses.ascii import controlnames
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
queue = []
path = []
class Box:
   def __init__(self, i, j):
      self.x = i
      self.y = j
      self.start  = False
      self.wall   = False
      self.target = False
      self.queued = False
      self.visited = False
      self.neighbours = []
      self.prior = None    
        
   def draw(self, win, color):
      pygame.draw.rect(win, color, (self.x * box_width, self.y * box_height, box_width - 1, box_height - 1))

   def set_neighbours(self):
      if self.x > 0:
         self.neighbours.append(grid[self.x -1 ] [self.y])
      if self.x < columns - 1:
         self.neighbours.append(grid[self.x +1][self.y])
      if self.y > 0:
         self.neighbours.append(grid[self.x][self.y - 1])
      if self.y < rows - 1:
         self.neighbours.append(grid[self.x][self.y + 1])
         
# Initialize Pygame's font module
pygame.font.init()
font = pygame.font.SysFont("Calibri", 24)            
# Create Grid
for i in range(columns):
   arr = []
   for j in range(rows):
      # print("j = ", j)
      arr.append(Box(i,j))
   grid.append(arr)

#Set Neighbours
for i in range(columns):
   for j in range(rows):
      grid[i][j].set_neighbours()

# start_box = grid[0][0]
# start_box.start = True
# start_box.visited = True
# queue.append(start_box)

def main():
   begin_search = False
   target_box_set = False
   searching = True
   taget_box = None
   start_box_set = False
   
   while True:
      for event in pygame.event.get():
         #Quit Window
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         # Mouse control
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # Left mouse button click
               x, y  = pygame.mouse.get_pos()
               i = x // box_width
               j = y // box_height
               if not start_box_set and not grid[i][j].wall:
                  start_box = grid[i][j]
                  start_box.start = True
                  start_box.visited = True
                  queue.append(start_box)
                  start_box_set = True
               
         elif event.type == pygame.MOUSEMOTION:
            x = pygame.mouse.get_pos()[0]
            y = pygame.mouse.get_pos()[1]
            # DraWall
            if event.buttons[0]:
               i = x // box_width
               j = y // box_height
               grid[i][j].wall = True
            # Set Target
            if event.buttons[2] and not target_box_set:
               i = x // box_width
               j = y // box_height
               target_box = grid[i][j]
               target_box.target = True
               target_box_set = True            
         # Start Algorithm
         if event.type == pygame.KEYDOWN and target_box_set:
            begin_search = True

      if begin_search:
         if len(queue) > 0 and searching:
            current_box = queue.pop(0)
            current_box.visited = True
            if current_box == target_box:
               searching = False
               while current_box.prior != start_box:
                  path.append(current_box.prior)
                  current_box = current_box.prior
            else:
               for neighbour in current_box.neighbours:
                  if not neighbour.queued and not neighbour.wall:
                     neighbour.queued = True
                     neighbour.prior = current_box
                     queue.append(neighbour)
         else:
            if searching:
               Tk().wm_withdraw()
               messagebox.showinfo("No Solution", "There is no solution!")
               searching = False            
            
      window.fill((0,0,0))
      
      for i in range(columns):
         for j in range(rows):
            box = grid[i][j]
            box.draw(window, (50, 50, 50))

            if box.queued:
               box.draw(window, (200, 0, 0))
               
            if box.visited:
               box.draw(window, (0, 200, 0))  
               
            if box in path:
               box.draw(window, (0, 0, 200))   
               
            if box.start:
               box.draw(window, (0,200,200))
            
            if box.wall:
               box.draw(window, (90, 90, 90))
            
            if box.target:
               box.draw(window, (200, 200, 0))
         
            # Render instructions text
         instructions = [
            "Instructions:",
            "1. Left click to set start",
            "2. Left click and hold to draw walls",
            "3. Right click to set target",
            "4. Press SPACE to run"
         ]
         for i, instruction in enumerate(instructions):
            text_surface = font.render(instruction, True, (255, 255, 255))
            window.blit(text_surface, (0, WINDOW_HEIGHT - (len(instructions) - i) * 20 - 10))   
      
      pygame.display.flip()
      
main()

