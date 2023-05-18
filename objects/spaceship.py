import math

import pygame

from objects.object import GameObject


class Spaceship(GameObject):
    def __init__(self, position, velocity, img):
        print("Debug: Creating new Spaceship object")
        GameObject.__init__(self, position, velocity, pygame.transform.scale_by(img, 0.2))
        self.keyUp = pygame.K_UP
        self.keyDown = pygame.K_DOWN
        self.keyLeft = pygame.K_LEFT
        self.keyRight = pygame.K_RIGHT

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rectangle, width=5)
        screen.blit(self.surface, self.rectangle)

    def turn(self, angle):
        self.angle += angle
        self.surface = pygame.transform.rotate(self.img, self.angle)
        self.rectangle = self.surface.get_rect(center=self.position)

    def move(self, keys):
        self.handleTeleportation()

        if keys[self.keyLeft]:
            self.turn(0.5)
        if keys[self.keyRight]:
            self.turn(-0.5)

        if keys[self.keyUp]:
            dx = self.velocity[0] * math.cos(math.radians(self.angle + 90))
            dy = -self.velocity[1] * math.sin(math.radians(self.angle + 90))
            self.rectangle.move_ip(dx, dy)
            self.position = self.rectangle.center
            # print(self.rectangle.center)

    # def attack(self):