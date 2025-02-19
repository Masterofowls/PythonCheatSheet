
"""
COMPREHENSIVE PYTHON PYGAME GUIDE
===============================
This guide covers PyGame concepts and game development.
Each section demonstrates different aspects of PyGame.
"""

import pygame
import sys
import random
from typing import Tuple, List

# ===========================
# SECTION 1: BASIC SETUP
# ===========================
"""
Basic PyGame initialization and game loop.
"""
pygame.init()
WINDOW_SIZE = (800, 600)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("PyGame Guide")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ===========================
# SECTION 2: GAME OBJECTS
# ===========================
"""
Basic game objects and their properties.
"""
class Player:
    def __init__(self, x: int, y: int):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.color = BLUE
        self.speed = 5
        self.velocity = [0, 0]

    def move(self):
        self.rect.x += self.velocity[0] * self.speed
        self.rect.y += self.velocity[1] * self.speed
        
        # Keep player in bounds
        self.rect.clamp_ip(screen.get_rect())

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(400, 300, 20, 20)
        self.color = RED
        self.speed = [4, 4]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        
        # Bounce off walls
        if self.rect.left < 0 or self.rect.right > WINDOW_SIZE[0]:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > WINDOW_SIZE[1]:
            self.speed[1] = -self.speed[1]

    def draw(self):
        pygame.draw.ellipse(screen, self.color, self.rect)

# Game objects
player = Player(375, 550)
ball = Ball()

# ===========================
# SECTION 3: GAME LOOP
# ===========================
"""
Main game loop with event handling.
"""
def handle_input():
    keys = pygame.key.get_pressed()
    player.velocity = [
        keys[pygame.K_RIGHT] - keys[pygame.K_LEFT],
        keys[pygame.K_DOWN] - keys[pygame.K_UP]
    ]

def update():
    player.move()
    ball.move()

def draw():
    screen.fill(BLACK)
    player.draw()
    ball.draw()
    pygame.display.flip()

def main():
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        handle_input()
        update()
        draw()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
