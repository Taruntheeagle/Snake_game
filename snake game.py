import pygame
import random

x = pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# screen parameters
width = 900
height = 600
gamewindow = pygame.display.set_mode((width, height))

# display of the game
pygame.display.set_caption("Snake Game By Tarun")

# game handling variables
exit_game = False
game_over = False
snake_x = 45
snake_y = 55
fps = 20
velx = 0
vely = 0
score = 0
snake_size = 10
food_x = random.randint(20, width / 2)
food_y = random.randint(20, height / 2)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

neha_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]  # Colors for each letter of NEHA

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, blue)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gamewindow, snk_list, snk_size):
    for i, (x, y) in enumerate(snk_list):
        if i % 5 == 0:  # For every 5th element, draw NEHA
            text = "NEHA"[i // 5]
            color = neha_colors[i // 5]
            screen_text = font.render(text, True, color)
            gamewindow.blit(screen_text, [x, y])
        else:
            pygame.draw.rect(gamewindow, black, [x, y, snk_size, snk_size])

snk_list = []
snk_length = 1

pygame.display.update()

# game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velx = 7
                vely = 0
            if event.key == pygame.K_LEFT:
                velx = -7
                vely = 0
            if event.key == pygame.K_UP:
                vely = -7
                velx = 0
            if event.key == pygame.K_DOWN:
                vely = 7
                velx = 0
    if abs(snake_x - food_x) < 7 and abs(snake_y - food_y) < 7:
        score += 1
        print("Score: ", score * 10)
        food_x = random.randint(20, width / 2)
        food_y = random.randint(20, height / 2)
        snk_length += 5

    gamewindow.fill(white)
    text_screen("score: " + str(score * 10), red, 5, 5)
    pygame.draw.rect(gamewindow, black, [snake_x, snake_y, snake_size, snake_size])  # 10 , 10 is the snake size
    pygame.draw.rect(gamewindow, red, [food_x, food_y, snake_size, snake_size])  # here 10 , 10 is food size
    snake_x += velx
    snake_y += vely

    head = []
    head.append(snake_x)
    head.append(snake_y)
    snk_list.append(head)

    if len(snk_list) > snk_length:
        del snk_list[0]

    for i in snk_list:
        if snk_list.count(i) >= 2:
            game_over = True
            break
        if snake_x < 0 or snake_x >= width or snake_y < 0 or snake_y >= height:
            game_over = True

    if game_over:
        font = pygame.font.Font(None, 64)
        game_over_text = font.render("Game Over", True, (0, 0, 0))
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (width // 2, height // 2)
        gamewindow.blit(game_over_text, game_over_rect)
        pygame.display.update()
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting the game
        exit_game = True

    plot_snake(gamewindow, snk_list, snake_size)
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()
