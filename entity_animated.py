from entity import Entity
from animation import Animation

class Entity_animated(Entity):
    def __init__(self, position, size, hitboxes, animations={}, speed=0.0):    #constructor
        super().__init__(None, position, size, hitboxes, speed)
        self.animations = animations    #dictionary of animations of entity
        self.current_animation = self.animations["idle"]   #current animation
        
    
    def update(self, delta_time):   #update
        if self.current_animation:
            self.current_animation.update(delta_time)
            
            
    def draw(self, screen, draw_hitboxes=False): #draw
        frame = self.current_animation.get_frame()  #get frame
        screen.blit(frame, self.position)   #draw
        
        if draw_hitboxes:   #draw hitboxes if true
            for hitbox in self.hitboxes:
                hitbox.draw(screen)
    

