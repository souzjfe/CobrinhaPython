#!/usr/local/bin/python
# coding: utf-8

import pygame
import random
from pygame.locals import*


def on_grid_random():
    x = random.randint(0, 880)
    y = random.randint(0, 880)
    return(x//40 * 40 + 10, y // 40 * 40 + 10)


def collision(obj1, obj2):
    return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
fontesys = pygame.font.SysFont('Manjari-Bold.tff', 70, bold=False, italic=False)
screen = pygame.display.set_mode((1020, 1020))
clock = pygame.time.Clock()
score = (0,0)
backgroud = pygame.image.load('backgroud.png')
pygame.display.set_caption('Snake')
# Loog game
Menu = True

while Menu:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    # snkae
    snake1 = [(810, 890), (850, 890), (890, 890)]
    snake2 = [(50, 50), (50, 50), (10, 50)]
    snake1_body = pygame.Surface((40, 40))
    snake1_body.fill((0, 255, 0))
    snake2_body = pygame.Surface((40, 40))
    snake2_body.fill((0, 255, 255))
    image_snake1_head = pygame.image.load('headsnake1-2.png')
    image_snake2_head = pygame.image.load('headsnake2-2.png')
    snake1_head = pygame.transform.rotate(image_snake1_head, 90)
    snake2_head = pygame.transform.rotate(image_snake2_head, -90)
    image_snake1_tail = pygame.image.load('tailsnake1.png')
    image_snake2_tail = pygame.image.load('tailsnake2.png')
    pygame.transform
    snake1_tail = pygame.transform.rotate(image_snake1_tail, 90)
    snake2_tail = pygame.transform.rotate(image_snake2_tail, -90)

    # apple
    apple = pygame.transform.scale(pygame.image.load('apple.png'), (40, 40))
    apple_pos = on_grid_random()
    
    # teleport
    Teleport_on = False
    teleport = [on_grid_random(), on_grid_random()]
    teleport_skin = pygame.image.load('teleport.png')

    # wall
    wall = pygame.Surface((60, 40))
    wall.fill((0, 110, 100))

    # troll
    Troll_on = False
    Moviment_on = True
    Moviment_apple_on = False

    # confgs
    Game_over = False
    Game_over_text = fontesys.render('Game over, Press [r] to Restart', True, (255, 255, 255))
    velocity = 7.5
    Restart = False
    Running = True
    my_direction = LEFT
    your_direction = RIGHT
    rotation1 = list()
    rotation2 = list()
    clock.tick(velocity)
    while Running:
        pygame.display.set_caption('Snake1   %d x %d ' %score)
        clock.tick(velocity)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        screen.fill((68,80,22))
        screen.blit(backgroud,(10,10))
        # pygame.draw.rect(screen, (200,0,200), (500,500), 1)
        # colisions
        if collision(snake1[0], apple_pos):
            apple_pos = on_grid_random()
            for pos in teleport:
                while apple_pos == pos:
                    apple_pos = on_grid_random()
            snake1.append((0, 0))
            if len(snake1) > 1:
                if Teleport_on == True:
                    teleport.append(on_grid_random())
                Teleport_on = True
            velocity += 0.1
        if collision(snake2[0], apple_pos):
            apple_pos = on_grid_random()
            for pos in teleport:
                while apple_pos == pos:
                    apple_pos = on_grid_random()
            snake2.append((0, 0))
            if len(snake2) > 5:
                if Teleport_on == True:
                    teleport.append(on_grid_random())
                Teleport_on = True
            velocity += 0.1
        if Teleport_on == True:
            for pos in teleport:
                screen.blit(teleport_skin, pos)
                if collision(snake1[0], pos):
                    snake1[0] = random.choice(list(filter(lambda x: x != pos, teleport)))
                    if my_direction == UP:
                        snake1[0] = (snake1[0][0], snake1[0][1]-40)
                    elif my_direction == DOWN:
                        snake1[0] = (snake1[0][0], snake1[0][1]+40)
                    elif my_direction == LEFT:
                        snake1[0] = (snake1[0][0]-40, snake1[0][1])
                    elif my_direction == RIGHT:
                        snake1[0] = (snake1[0][0]+40, snake1[0][1])
                if collision(snake2[0], pos):
                    snake2[0] = random.choice(list(filter(lambda x: x != pos, teleport)))
                    if your_direction == UP:
                        snake2[0] = (snake2[0][0], snake2[0][1]-40)
                    elif your_direction == DOWN:
                        snake2[0] = (snake2[0][0], snake2[0][1]+40)
                    elif your_direction == LEFT:
                        snake2[0] = (snake2[0][0]-40, snake2[0][1])
                    elif your_direction == RIGHT:
                        snake2[0] = (snake2[0][0]+40, snake2[0][1])
        if Troll_on:
            if collision(snake1[0], (apple_pos[0] - 40, apple_pos[1])) and not apple_pos[0] + 40 >= 900:
                apple_pos = (apple_pos[0]+40, apple_pos[1])
                Moviment_on = False
                Moviment_apple_on = True
                Troll_on = False
            elif collision(snake1[0], (apple_pos[0] + 40, apple_pos[1])) and not apple_pos[0] - 40 < 0:
                apple_pos = (apple_pos[0]-40, apple_pos[1])
                Moviment_on = False
                Moviment_apple_on = True
                Troll_on = False
            elif collision(snake1[0], (apple_pos[0], apple_pos[1] - 40)) and not apple_pos[1] + 40 >= 900:
                apple_pos = (apple_pos[0], apple_pos[1]+40)
                Moviment_on = False
                Moviment_apple_on = True
                Troll_on = False
            elif collision(snake1[0], (apple_pos[0], apple_pos[1] + 40)) and not apple_pos[1] - 40 < 0:
                apple_pos = (apple_pos[0], apple_pos[1]-40)
                Moviment_on = False
                Moviment_apple_on = True
                Troll_on = False

        if snake1[0][0] >= 1000 or snake1[0][0] <= -40 or snake1[0][1] >= 1000 or snake1[0][1] <= -40 or snake2[0][0] >= 1000 or snake2[0][0] <= -40 or snake2[0][1] >= 1000 or snake2[0][1] <= -40:
            Running = False
        for pos in snake1[2:]:
            if collision(snake1[0], pos):
                Running = False
                score = (score[0],score[1]+1)
            if collision(snake2[0],pos):
                score = (score[0]+1,score[1])
                Running = False
        for pos in snake2[2:]:
            if collision(snake2[0], pos):
                score = (score[0]+1,score[1])
                Running = False
            if collision(snake1[0],pos):
                score = (score[0],score[1]+1)
                Running = False
        # snake
        if event.type == KEYDOWN:
            if event.key == K_DOWN and my_direction != UP:
                my_direction = DOWN
                rotation1.append((snake1[0],my_direction))                 
                snake1_head = pygame.transform.rotate(image_snake1_head, 180)
            elif event.key == K_RIGHT and my_direction != LEFT:
                my_direction = RIGHT
                rotation1.append((snake1[0],my_direction))                 
                snake1_head = pygame.transform.rotate(image_snake1_head, 270)
            elif event.key == K_LEFT and my_direction != RIGHT:
                my_direction = LEFT
                rotation1.append((snake1[0],my_direction))                 
                snake1_head = pygame.transform.rotate(image_snake1_head, -270)
            elif event.key == K_UP and my_direction != DOWN:
                my_direction = UP
                rotation1.append((snake1[0],my_direction))         
                snake1_head = pygame.transform.rotate(image_snake1_head, 0)
            if event.key == K_s and your_direction != UP:
                your_direction = DOWN
                rotation2.append((snake2[0],your_direction))   
                snake2_head = pygame.transform.rotate(image_snake2_head, 180)
            elif event.key == K_d and your_direction != LEFT:
                your_direction = RIGHT
                rotation2.append((snake2[0],your_direction))   
                snake2_head = pygame.transform.rotate(image_snake2_head, 270)
            elif event.key == K_a and your_direction != RIGHT:
                your_direction = LEFT
                rotation2.append((snake2[0],your_direction))   
                snake2_head = pygame.transform.rotate(image_snake2_head, -270)
            elif event.key == K_w and your_direction != DOWN:
                your_direction = UP
                rotation2.append((snake2[0],your_direction))   
                snake2_head = pygame.transform.rotate(image_snake2_head, 0)
        if random.randint(0, 1) == 0:
            image_snake1_head = pygame.image.load('headsnake1-2.png')
            image_snake2_head = pygame.image.load('headsnake2-2.png')
        else:
            image_snake1_head = pygame.image.load('headsnake1-1.png')
            image_snake2_head = pygame.image.load('headsnake2-1.png')
            
        if len(rotation1) > 0 and collision(snake1[len(snake1)-2],rotation1[0][0]):
            if rotation1[0][1] == UP:
                snake1_tail = pygame.transform.rotate(image_snake1_tail, 0)
            elif rotation1[0][1] == LEFT:
                snake1_tail = pygame.transform.rotate(image_snake1_tail, -270)
            elif rotation1[0][1] == RIGHT:
                snake1_tail = pygame.transform.rotate(image_snake1_tail, 270)
            elif rotation1[0][1] == DOWN:
                snake1_tail = pygame.transform.rotate(image_snake1_tail, 180)
            rotation1.pop(0)

        if len(rotation2) > 0 and collision(snake2[len(snake2)-2],rotation2[0][0]):
            if rotation2[0][1] == UP:
                snake2_tail = pygame.transform.rotate(image_snake2_tail, 0)
            elif rotation2[0][1] == LEFT:
                snake2_tail = pygame.transform.rotate(image_snake2_tail, -270)
            elif rotation2[0][1] == RIGHT:
                snake2_tail = pygame.transform.rotate(image_snake2_tail, 270)
            elif rotation2[0][1] == DOWN:
                snake2_tail = pygame.transform.rotate(image_snake2_tail, 180)
            rotation2.pop(0)

        if Moviment_on:
            if my_direction == UP:
                snake1[0] = (snake1[0][0], snake1[0][1]-40)
            elif my_direction == DOWN:
                snake1[0] = (snake1[0][0], snake1[0][1]+40)
            elif my_direction == RIGHT:
                snake1[0] = (snake1[0][0]+40, snake1[0][1])
            elif my_direction == LEFT:
                snake1[0] = (snake1[0][0]-40, snake1[0][1])
            for i in range(len(snake1) - 1, 0, -1):
                snake1[i] = (snake1[i-1][0], snake1[i-1][1])
            if your_direction == UP:
                snake2[0] = (snake2[0][0], snake2[0][1]-40)
            elif your_direction == DOWN:
                snake2[0] = (snake2[0][0], snake2[0][1]+40)
            elif your_direction == RIGHT:
                snake2[0] = (snake2[0][0]+40, snake2[0][1])
            elif your_direction == LEFT:
                snake2[0] = (snake2[0][0]-40, snake2[0][1])
            for i in range(len(snake2) - 1, 0, -1):
                snake2[i] = (snake2[i-1][0], snake2[i-1][1])
        screen.blit(snake1_tail, snake1[len(snake1)-1])
        for pos in snake1[2:len(snake1)-1]:
            screen.blit(snake1_body, pos)
        screen.blit(snake1_head, (snake1[0][0]-10, snake1[0][1]-10))
        screen.blit(snake2_tail, snake2[len(snake2)-1])
        for pos in snake2[2:len(snake2)-1]:
            screen.blit(snake2_body, pos)
        screen.blit(snake2_head, (snake2[0][0]-10, snake2[0][1]-10))
        # apple
        screen.blit(apple, apple_pos)
        if Moviment_apple_on:
            if my_direction == UP:
                apple_pos = (apple_pos[0], apple_pos[1]-40)
            elif my_direction == DOWN:
                apple_pos = (apple_pos[0], apple_pos[1]+40)
            elif my_direction == RIGHT:
                apple_pos = (apple_pos[0]+40, apple_pos[1])
            elif my_direction == LEFT:
                apple_pos = (apple_pos[0]-40, apple_pos[1])

        

        pygame.display.update()

    while not Game_over:
        clock.tick(velocity)
        pygame.display.update()
        screen.blit(Game_over_text, (100, 100))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    Game_over = True
    pygame.display.update()



        
    