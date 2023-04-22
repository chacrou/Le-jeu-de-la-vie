import pygame
import keyboard
import time

running = True
debut = True
#Images size = 16x16
dead_png = 'assets\dead.png'
alive_png = 'assets\\alive.png'
alive = pygame.image.load(alive_png)
dead = pygame.image.load(dead_png)
icone = pygame.image.load('assets\icone.jpg')

pygame.init()
screen = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)
pygame.display.set_caption("Le jeu de la vie")
pygame.display.set_icon(icone)
x_max, y_max = screen.get_size()
x_max = x_max // 16
y_max = y_max // 16


class Cell:
    global cells
    global screen
    global alive
    global dead
    next_gen = 'dead'
    
    def __init__(self, x, y, statut = 'dead'):
        self.x = x
        self.y = y
        self.statut = statut
    
        
    def launch(self):
        if self.statut == 'alive':
            screen.blit(alive, (self.x * 16, self.y * 16))
        if self.statut == 'dead':
            screen.blit(dead, (self.x * 16, self.y * 16))
        pygame.display.flip()
    

    def generation(self, test = ''):
        alive_cells_around = 0
        try:
            if cells[self.x - 1, self.y - 1].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:    
            if cells[self.x, self.y - 1].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:
            if cells[self.x + 1, self.y - 1].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:
            if cells[self.x - 1, self.y].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:
            if cells[self.x + 1, self.y].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:
            if cells[self.x - 1, self.y + 1].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:
            if cells[self.x, self.y + 1].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        try:
            if cells[self.x + 1, self.y + 1].statut == 'alive':
                alive_cells_around += 1
        except:
            abc = 0
            abc += 1
        if alive_cells_around == 3:
            self.next_gen = 'alive'
        elif self.statut == 'alive':
            if alive_cells_around == 2 or alive_cells_around == 3:
                self.next_gen = 'alive'
            else:
                self.next_gen = 'dead'
        else:
            self.next_gen = 'dead'
        return alive_cells_around
            
            
    def refresh(self):
        self.statut = self.next_gen
        if self.statut == 'dead':
            screen.blit(dead, (self.x * 16, self.y * 16))
        if self.statut == 'alive':
            screen.blit(alive, (self.x * 16, self.y * 16))


def creation(x_max, y_max):
    x = 0
    y = 0
    cells = {}
    
    #Repete le nombre de fois qu'il faut pour creer le bon nombre de cellules
    for a in range(x_max * y_max):
        cells[x, y] = Cell(x, y, 'dead')
        cells[x, y].launch()
        x += 1
        if x == x_max:
            x = 0
            y += 1
    
    return cells

cells = creation(x_max, y_max)
while running:
    while debut:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                c_x, c_y = event.pos #coordonnées du clique
                c_x = c_x // 16
                c_y = c_y // 16
                button = event.button
                button = int(button)
                if button == 1:
                    cells[c_x, c_y].statut = 'alive'
                    cells[c_x, c_y].launch()
                if button == 3:
                    cells[c_x, c_y].statut = 'dead'
                    cells[c_x, c_y].launch()
                pygame.display.flip()
            if event.type == pygame.QUIT:
                print('Fermeture du programme...')
                running = False
                debut = False
            if keyboard.is_pressed("a"):
                debut = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Fermeture du programme...')
            running = False
    x = 0
    y = 0
    for a in range(len(cells)):
        cells[x, y].generation()
        x += 1
        if x == x_max:
            x = 0
            y += 1
    x = 0
    y = 0
    for a in range(len(cells)):
        cells[x, y].refresh()
        x += 1
        if x == x_max:
            x = 0
            y += 1
    time.sleep(1)
    pygame.display.flip()
    if keyboard.is_pressed("e"):
        debut = True
pygame.quit()