import pygame

class Hitbox:
    def __init__(self, position, size, position_offset=(0.0, 0.0)): #constructor
        self.position = position    #position   | (x, y)
        self.size = size    #size of hitbox | (width, height)
        self.position_offset = position_offset  #offset of position | (dx, dy)
        self.color = (255, 0 , 0)   #color, default red
        self.width = 2  #thickness of border, default 2
        
        
    def update_position(self, position):  #moving the hitbox
        self.position = position + self.position_offset
        
        
    def draw(self, screen): #drawing the rectangle around the hitbox
        rectangle = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1]) #hitbox rectangle
        pygame.draw.rect(screen, self.color, rectangle, self.width)
        
                
    def intersects(self, other):    #to do
        print("INTERSECTS")