import pygame
import time

# Initialize pygame and create a window
pygame.init()
width = 500
height = 500
screen = pygame.display.set_mode((width, height))

# Create a snake and a food object
snake = [(200, 200), (210, 200), (220, 200)]
food = (250, 250)

# Set the initial direction of the snake
direction = "right"

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_RIGHT:
                direction = "right"
            elif event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_DOWN:
                direction = "down"

    # Check if the snake has collided with the food
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        food = (random.randint(0, width // 10 - 1) * 10, random.randint(0, height // 10 - 1) * 10)
    else:
        snake.pop()

    # Draw the snake and the food on the screen
    screen.fill((0, 0, 0))
    for pos in snake:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food[0], food[1], 10, 10))
    pygame.display.update()

    # Wait for a short time before moving the snake again
    time.sleep(0.1)