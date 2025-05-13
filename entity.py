from hitbox import Hitbox
import pygame

class Entity:
    def __init__(self, sprite, position, size, hitboxes, speed=0.0):    #constructor
        self.position = position    #position   | (x, y)
        self.size = size
        self.hitboxes = hitboxes    #hiboxes array
        self.speed = speed  #speed of moving entity, default 0
        if sprite:
            self.sprite = pygame.image.load(sprite)    #sprite path
            self.sprite = pygame.transform.scale(self.sprite, (self.size[0], self.size[1]))

    def move(self, direction):  #move the entity based of direction |   (x, y)
        self.position = (   self.position[0] + direction[0] * self.speed,   #move entity
                            self.position[1] + direction[1] * self.speed)
        for hitbox in self.hitboxes:    #move hitboxes
            hitbox.update_position(self.position)
        
    def draw(self, screen, draw_hitboxes=False):   #drawing function
        screen.blit(self.sprite, self.position) #draw sprite
        
        if draw_hitboxes:   #draw hitboxes if true
            for hitbox in self.hitboxes:
                hitbox.draw(screen)
    