'''
  Tech01 simple Python game(controlled by AI) By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/simpleAIGame/
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
'''

import pygame
import sys
import random
import traceback

try:
    # Initialize Pygame
    pygame.init()
    print("Pygame initialized successfully")

    # Set window size
    WIDTH, HEIGHT = 800, 600
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Square AI Game")
    print("Window created successfully")

    # Background color
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Player position and size (black square)
    player_size = 50
    player_pos = [WIDTH // 2, HEIGHT // 2]

    # Enemy position and size (red square)
    enemy_size = 30
    enemy_pos = [300, 200]

    # Enemy and player speed
    enemy_speed = 2
    player_speed = 5

    # Font for displaying text
    font = pygame.font.SysFont(None, 30)
    print("Game variables initialized")

    def get_enemy_direction(player_pos, enemy_pos):
        # Simple AI logic: move towards the player
        dx = player_pos[0] - enemy_pos[0]
        dy = player_pos[1] - enemy_pos[1]
        
        # Add some randomness to make it more interesting
        if random.random() < 0.1:  # 10% chance to make a random move
            return random.choice(["left", "right", "up", "down"])
        
        # Determine the primary direction of movement
        if abs(dx) > abs(dy):
            return "right" if dx > 0 else "left"
        else:
            return "down" if dy > 0 else "up"

    # Main game loop
    clock = pygame.time.Clock()  # Add clock for frame rate control
    running = True
    print("Starting game loop")

    while running:
        # Event checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                print("Quit event received")

        # Get pressed keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= player_speed
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
            player_pos[0] += player_speed
        if keys[pygame.K_UP] and player_pos[1] > 0:
            player_pos[1] -= player_speed
        if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
            player_pos[1] += player_speed

        # Move the enemy according to logic if it is near the player
        enemy_direction = get_enemy_direction(player_pos, enemy_pos)
        if enemy_direction == "left" and enemy_pos[0] > 0:
            enemy_pos[0] -= enemy_speed
        elif enemy_direction == "right" and enemy_pos[0] < WIDTH - enemy_size:
            enemy_pos[0] += enemy_speed
        elif enemy_direction == "up" and enemy_pos[1] > 0:
            enemy_pos[1] -= enemy_speed
        elif enemy_direction == "down" and enemy_pos[1] < HEIGHT - enemy_size:
            enemy_pos[1] += enemy_speed

        # Update window
        win.fill(WHITE)
        pygame.draw.rect(win, BLACK, (player_pos[0], player_pos[1], player_size, player_size))
        pygame.draw.rect(win, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

        # Check for collision between player and enemy
        if (player_pos[0] < enemy_pos[0] + enemy_size and
                player_pos[0] + player_size > enemy_pos[0] and
                player_pos[1] < enemy_pos[1] + enemy_size and
                player_pos[1] + player_size > enemy_pos[1]):
            text = font.render("Game Over!", True, BLACK)
            win.blit(text, [WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2])
            pygame.display.update()
            pygame.time.delay(2000)  # Delay before exiting
            running = False
            print("Game Over!")

        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

    print("Game loop ended")
    pygame.quit()
    sys.exit()

except Exception as e:
    print("An error occurred:")
    print(traceback.format_exc())
    pygame.quit()
    sys.exit(1)
