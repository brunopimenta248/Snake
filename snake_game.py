import pygame
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake initial state
snake = [(100, 100)]
direction = (GRID_SIZE, 0)

def get_random_food_position(snake):
    """Generate a new food position not overlapping the snake."""
    while True:
        pos = (
            random.randint(0, WIDTH // GRID_SIZE - 1) * GRID_SIZE,
            random.randint(0, HEIGHT // GRID_SIZE - 1) * GRID_SIZE
        )
        if pos not in snake:
            return pos

# Place the first food
food = get_random_food_position(snake)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Change direction, prevent reversing
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Move snake
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    # Check for collisions
    if (new_head in snake or
        not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT)):
        running = False  # Game over
    else:
        snake.insert(0, new_head)
        if new_head == food:
            food = get_random_food_position(snake)
        else:
            snake.pop()

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(10)  # Control the speed of the game

pygame.quit()

