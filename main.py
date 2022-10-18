import pygame
from pygame.locals import QUIT, KEYDOWN
import random
import time

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

size = width, height = (800, 800)
hbox, vbox = 200, 200
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
right_lane = width / 2 + road_w / 4
left_lane = width / 2 - road_w / 4
speed = 1

pygame.init()
running = True
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Dont Crash!")
screen.fill((60, 220, 0))

pygame.display.update()

car1 = pygame.image.load("car1.png")
car1_loc = car1.get_rect()
car1_loc.center = right_lane, height * 0.8

car2 = pygame.image.load("car2.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

picture = pygame.image.load("grass.png")
bg = pygame.transform.scale(picture, (800, 800))

GO = pygame.image.load("GO.png")


counter = 0
carsPassed = 0

screen.blit(bg, (0,0))
while running:
    counter += 1
    text = my_font.render("Score = "+str(carsPassed), 1, (200,200,0))

    if counter == 3000:
        speed += 0.25
        counter = 0
        print(f"speed increased {speed}")

    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
            carsPassed = carsPassed + 1
        else:
            car2_loc.center = left_lane, -200
            carsPassed = carsPassed + 1

    if car1_loc[0] == car2_loc[0] and car2_loc[1] > car1_loc[1] - 250:
        print("GAME OVER")
        screen.blit(GO, (0,0))
        pygame.display.update()
        time.sleep(2)
        break

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:

            if event.key in [pygame.K_a, pygame.K_LEFT]:
                car1_loc = car1_loc.move([-int(road_w / 2), 0])
                if car1_loc.x < 150:
                    car1_loc = car1_loc.move([int(road_w / 2), 0])

            if event.key in [pygame.K_d, pygame.K_RIGHT]:
                car1_loc = car1_loc.move([int(road_w / 2), 0])
                if car1_loc.x > 400:
                    car1_loc = car1_loc.move([-int(road_w / 2), 0])


    pygame.draw.rect(screen, (50, 50, 50),
                     (width / 2 - road_w / 2, 0, road_w, height))

    pygame.draw.rect(screen, (255, 240, 60),
                     (width / 2 - roadmark_w / 2, 0, roadmark_w, height))

    pygame.draw.rect(
        screen, (255, 255, 255),
        (width / 2 - road_w / 2 + roadmark_w * 3, 0, roadmark_w, height))

    pygame.draw.rect(
        screen, (255, 255, 255),
        (width / 2 + road_w / 2 - roadmark_w * 2, 0, roadmark_w, height))

    screen.blit(car1, car1_loc)
    screen.blit(car2, car2_loc)
    screen.blit(text, (230,0))
    pygame.display.update()

pygame.quit()
