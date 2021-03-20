
import pygame
import random
import time
import os

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 15)

window_size_x = 400
window_size_y = 300

# define RGB colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

snake_block = 10

fname = "score.txt"

display = pygame.display.set_mode((window_size_x, window_size_y))  # define display, set window size

def get_food_pos(window_size_x,window_size_y):

    x_pos_rand = random.randrange(0, window_size_x, 10)
    y_pos_rand = random.randrange(0, window_size_y, 10)

    return x_pos_rand, y_pos_rand

def message(msg,color):
    mesg = myfont.render(msg, True, color)
    display.blit(mesg, [window_size_x/4, window_size_y/2])

def display_score(score, highest_score):

    value = myfont.render("Your Score: " + str(score), True, blue)
    display.blit(value, [0, 0])
    value = myfont.render("Highest Score: " + str(highest_score), True, blue)
    display.blit(value, [0, 20])

def game_lost(score, highest_score):

    message("Game Over Press Q-Quit or C-Play Again", red)
    pygame.display.update()

    if score > highest_score:
        write_highest_score(score)

    play_again = True

    while play_again:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    play_again = False
                    pygame.quit()
                    quit()
                if event.key == pygame.K_c:
                    main()

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])

def write_highest_score(score):
    f = open(fname, "w")
    # f.seek(0)
    f.write(str(score))
    # f.truncate()
    f.close()

def read_highest_score():
    if os.path.isfile(fname): # if file exists, read highest score
        f = open(fname, "r")
        highest_score = int(f.read())
    else: # else highest score is 0
        highest_score = 0
    return highest_score

def main():

    pygame.init()

    pygame.display.set_caption('SNAKE')  # title on pygame window

    # start positions of snake
    snake_head_x = window_size_x / 2
    snake_head_y = window_size_y / 2

    snake_list = []
    snake_len = 1

    x_delta = 0
    y_delta = 0

    score = 0

    delta_pos = 10 # how much the position changes per frame

    frames_per_second = 10  # how many times display updates snake position per second ~ speed

    clock = pygame.time.Clock()  # create clock object

    exit_game = False  # boolean for pygame while loop

    food_x, food_y = get_food_pos(window_size_x, window_size_y)

    game_over = False

    highest_score = read_highest_score()

    while not game_over:

        for event in pygame.event.get():


            # print(event) # print out events

            if event.type == pygame.QUIT: # if close button is clicked
                exit_game = True

            if event.type == pygame.KEYDOWN: # if key is pressed
                if event.key == pygame.K_UP: # up arrow
                    x_delta = 0
                    y_delta = -snake_block
                if event.key == pygame.K_DOWN: # down arrow
                    x_delta = 0
                    y_delta = snake_block
                if event.key == pygame.K_LEFT: # left arrow
                    x_delta = -snake_block
                    y_delta = 0
                if event.key == pygame.K_RIGHT: # right arrow
                    x_delta = snake_block
                    y_delta = 0

        snake_head_x += x_delta
        snake_head_y += y_delta

        snake_head = []
        snake_head.append(snake_head_x)
        snake_head.append(snake_head_y)
        snake_list.append(snake_head)
        print(snake_list)

        if len(snake_list) > snake_len:
            del snake_list[0]



        # if snake reaches food position, generate new food position
        if (snake_head_x == food_x) and (snake_head_y == food_y):
            snake_len = snake_len + 1
            score = score + 10
            print(snake_len)
            food_x, food_y = get_food_pos(window_size_x, window_size_y)

        display.fill(white) # background color

        pygame.draw.rect(display, black, [snake_head_x, snake_head_y, snake_block, snake_block]) # snake
        pygame.draw.rect(display, red, [food_x, food_y, 10, 10]) # food

        our_snake(snake_block, snake_list)

        display_score(score, highest_score)

        pygame.display.update()

        clock.tick(frames_per_second) # update x frames/second

        print(snake_head_x, snake_head_y)

        # ??? if you bump into snake's tail
        for x in snake_list[:-1]:
            if x == snake_head:
                game_over = True
                game_lost(score, highest_score)

        # if you go off screen
        if (snake_head_x < 0) or (snake_head_x > window_size_x) or (snake_head_y < 0) or (snake_head_y > window_size_y):
            game_over = True
            game_lost(score, highest_score)

    pygame.display.update()

    time.sleep(60)

main()