def create_pipe():
    height = random.randint(100, 400)
    return {
        "x": WIDTH,
        "top": height,
        "bottom": height + pipe_gap,
        "scored": False   # ✅ important
    }

import pygame
import pygame
import random


import pygame
import random

# Init
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()


BlACK = (255, 255, 255)
CYAN = (0, 200, 0)


bird_x = 50
bird_y = 300
bird_velocity = 0
gravity = 0.5
jump_strength = -8


pipe_width = 60
pipe_gap = 150
pipe_velocity = 3
pipes = []

def create_pipe():
    height = random.randint(100, 400)
    return {
        "x": WIDTH,
        "top": height,
        "bottom": height + pipe_gap
    }


running = True
frame_count = 0
score = 0

while running:
    clock.tick(60)
    screen.fill(BlACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = jump_strength

    # Bird physics
    bird_velocity += gravity
    bird_y += bird_velocity

    # Create pipes
    frame_count += 1
    if frame_count % 90 == 0:
        pipes.append(create_pipe())

    # Move pipes
    for pipe in pipes:
        pipe["x"] -= pipe_velocity

    # Draw pipes
    for pipe in pipes:
        pygame.draw.rect(screen, CYAN, (pipe["x"], 0, pipe_width, pipe["top"]))
        pygame.draw.rect(screen, CYAN, (pipe["x"], pipe["bottom"], pipe_width, HEIGHT))

    # Draw bird
    bird_rect = pygame.Rect(bird_x, bird_y, 30, 30)
    pygame.draw.rect(screen, (255, 0, 0), bird_rect)

    # Collision
    for pipe in pipes:
        top_rect = pygame.Rect(pipe["x"], 0, pipe_width, pipe["top"])
        bottom_rect = pygame.Rect(pipe["x"], pipe["bottom"], pipe_width, HEIGHT)

        if bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect):
            running = False

    # Ground / ceiling collision
    if bird_y <= 0 or bird_y >= HEIGHT:
        running = False

    # Score
    for pipe in pipes:
        if pipe["x"] == bird_x:
            score += 1

    # Display
    pygame.display.flip()

pygame.quit()
print("Score:", score)

pipe_velocity += 10

with open("highscore.txt", "r") as f:
    highscore = int(f.read())

for pipe in pipes:
    if pipe.get("scored") and pipe["x"] + pipe_width < bird_x:
        score += 1
        pipe["scored"] = True

try:
    with open("highscore.txt", "r") as f:
        highscore = int(f.read())
except:
    highscore = 0



if score > highscore:
    with open("highscore.txt", "w") as f:
        f.write(str(score))

highscore_text = f.render(f"High: {highscore}", True, (0, 0, 0))
screen.blit(highscore_text, (10, 40))