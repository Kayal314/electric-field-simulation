import pygame
from charge import Charge
import math

charges = []
n = int(input("Enter the number of charges "))
for i in range(0, n):
    mag = int(input("Enter the magnitude of charge with sign "))
    y = int(input("Enter y coordinate of charge "))
    charges.append(Charge(magnitude=mag, position=(750, y)))
pygame.init()

screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption('Electric Field Visualization')
arrow_len = 8
negative = pygame.image.load('sprites/negative.png')
negative = pygame.transform.scale(negative, (20, 20))
positive = pygame.image.load('sprites/positive.png')
positive = pygame.transform.scale(positive, (20, 20))


def grid():
    for row in range(0, 1000, 25):
        pygame.draw.line(screen, (36, 36, 38), (0, row), (1500, row), 1)
    for col in range(0, 1500, 25):
        pygame.draw.line(screen, (36, 36, 38), (col, 0), (col, 1000))


def display_field():
    for j in range(0, 1500, 30):
        for k in range(0, 1000, 30):
            x_net = 0
            y_net = 0
            success = True
            for charge in charges:
                if j != charge.position[0] or k != charge.position[1]:
                    field = 10e9 * charge.magnitude / (charge.get_sq_distance_from((j, k)))
                    cos, sin = charge.get_component_factors((j, k))
                    x_net += (cos * field)
                    y_net += (sin * field)
                else:
                    success = False
            if success:
                if x_net != 0:
                    angle = math.atan(y_net / x_net)
                    if angle == math.pi / 2:
                        print(y_net, x_net)
                else:
                    angle = math.pi / 2
                del_x = arrow_len * math.cos(angle)
                del_y = arrow_len * math.sin(angle)
                pygame.draw.line(screen, (219, 52, 235), (j, k), (j + del_x, k + del_y), 1)


def display_charges():
    for each_charge in charges:
        if each_charge.magnitude < 0:
            screen.blit(negative, each_charge.get_shifted_position())
        else:
            screen.blit(positive, each_charge.get_shifted_position())


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        grid()
        display_field()
        display_charges()
        pygame.display.update()
