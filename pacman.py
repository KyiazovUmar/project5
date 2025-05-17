import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константтар
CELL = 24  # бир клетканын пикселде өлчөмү
level = [
    "11111111111111111111",
    "10000000001100000001",
    "10111111101101111101",
    "10200000100010000021",
    "10101110111110110101",
    "10001000000000010001",
    "11101110101110101111",
    "00001000100010001000",
    "11101111101111101111",
    "10000000000000000001",
    "10111110111110111101",
    "10000010000010000001",
    "11111111111111111111",
]
ROWS = len(level)
COLS = len(level[0])

WIDTH  = COLS * CELL
HEIGHT = ROWS * CELL

# Түстөр
BLACK  = (0, 0, 0)
NAVY   = (0, 0, 128)
YELLOW = (255, 255, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
PINK   = (255, 105, 180)
CYAN   = (0, 255, 255)
ORANGE = (255, 165, 0)

# Экран жана таймер
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Pac-Man классы
class Pacman:
    def __init__(self):
        self.x = 1
        self.y = 1
        self.dir = (0, 0)
        self.next_dir = (0, 0)
        self.radius = CELL // 2 - 2

    def update(self):
        # Эгер кийинки багытка өтүү мүмкүн болсо, аны кабыл алабыз
        if self.can_move(self.next_dir):
            self.dir = self.next_dir

        # Учурдагы багытта жыл
        if self.can_move(self.dir):
            self.x += self.dir[0]
            self.y += self.dir[1]

        # Пеллет жегени текшерүү
        if level[self.y][self.x] == '2':
            # Символду '0'ге өзгөртүү үчүн сапты кайра курабыз
            row = list(level[self.y])
            row[self.x] = '0'
            level[self.y] = "".join(row)

    def can_move(self, d):
        dx, dy = d
        nx, ny = self.x + dx, self.y + dy
        return 0 <= nx < COLS and 0 <= ny < ROWS and level[ny][nx] != '1'

    def draw(self):
        px = self.x * CELL + CELL // 2
        py = self.y * CELL + CELL // 2
        pygame.draw.circle(screen, YELLOW, (px, py), self.radius)


class Ghost:
    colors = [RED, PINK, CYAN, ORANGE]
    def __init__(self, idx):
        self.x = COLS - 2
        self.y = ROWS - 2
        self.color = Ghost.colors[idx % len(Ghost.colors)]
        self.dir = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        self.size = CELL - 4

    def update(self):
        # Эгер дубалга тийсе же 20% кээде багытты алмаштырабыз
        if not self.can_move(self.dir) or random.random() < 0.2:
            self.dir = random.choice([(1,0),(-1,0),(0,1),(0,-1)])
        self.x += self.dir[0]
        self.y += self.dir[1]

    def can_move(self, d):
        dx, dy = d
        nx, ny = self.x + dx, self.y + dy
        return 0 <= nx < COLS and 0 <= ny < ROWS and level[ny][nx] != '1'

    def draw(self):
        px = self.x * CELL + 2
        py = self.y * CELL + 2
        pygame.draw.rect(screen, self.color, (px, py, self.size, self.size))

# Оюндун башталышы
pacman = Pacman()
ghosts = [Ghost(i) for i in range(4)]

# Башкы цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman.next_dir = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                pacman.next_dir = (1, 0)
            elif event.key == pygame.K_UP:
                pacman.next_dir = (0, -1)
            elif event.key == pygame.K_DOWN:
                pacman.next_dir = (0, 1)

    pacman.update()
    for g in ghosts:
        g.update()
        if g.x == pacman.x and g.y == pacman.y:
           
            pygame.quit()
            sys.exit()

   
    screen.fill(BLACK)

 
    for row_idx, row in enumerate(level):
        for col_idx, cell in enumerate(row):
            rect = pygame.Rect(col_idx*CELL, row_idx*CELL, CELL, CELL)
            if cell == '1':
                pygame.draw.rect(screen, NAVY, rect)
            elif cell == '2':
                center = rect.center
                pygame.draw.circle(screen, WHITE, center, CELL//6)

  
    pacman.draw()
    for g in ghosts:
        g.draw()

    pygame.display.flip()
    clock.tick(10)
