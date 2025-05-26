'''
  Tech01 simple Python game(controlled by AI) By Serhii Trush with MIT License.
  https://github.com/techn0man1ac/simpleAIGame/
  Thank's ChatGPT for help.
  By Tech01 labs 2024.
'''

import pygame
import sys
import ollama

# Initialize Pygame
pygame.init()

# Set window size
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square AI Game")

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
enemy_speed = 5
player_speed = 15

# Font for displaying text
font = pygame.font.SysFont(None, 30)

def get_enemy_direction(player_pos, enemy_pos):
    # Determine enemy position relative to the player
    if abs(enemy_pos[0] - player_pos[0]) > abs(enemy_pos[1] - player_pos[1]):
        if enemy_pos[0] < player_pos[0]:
            enemy_position = "right"
        else:
            enemy_position = "left"
    else:
        if enemy_pos[1] < player_pos[1]:
            enemy_position = "down"
        else:
            enemy_position = "up"

    # Create a query to Ollama
    question = f"Enemy on the {enemy_position} position!"
    print(question)
    response = ollama.chat(
        model='llama3',
        messages=[{'role': 'user', 'content': question + " You are running away from the enemy, in which direction will you run? Answers need to be one word and from this list - Left, Right, Down, Up"}],
        stream=False,
    )

    # Get the response
    answer = response['message']['content'].strip().lower()
    print(answer)
    return answer

# Main game loop
while True:
    # Event checking
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
        pygame.quit()
        sys.exit()

    pygame.display.update()
