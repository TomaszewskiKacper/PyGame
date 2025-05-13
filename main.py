import pygame, sys
from hitbox import Hitbox
from entity import Entity
from animation import Animation
from entity_animated import Entity_animated

#testing entity
h = Hitbox((200,200), (100, 70))    #hitbox of rock
rock = Entity("Textures/rock.png", (200, 200), (100, 70), [h])  #rock entity

#testing animated antity
idle = Animation("Textures\stick_idle.png", 0.4, 2)    #animation for idle
a = {"idle": idle}  #dict of animations
h2 = Hitbox((400,300), (50, 100))   #hitbox
animated = Entity_animated((400,300), (50,100), [h2], a)  #animated entity


class Player():
    def __init__(self):
        self.pos = [500,300]    #position
        self.radius = 20
        self.speed = 5

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()
        self.player = Player()

    def update(self):
        keys = pygame.key.get_pressed()

        #update position
        if keys[pygame.K_w]:
            self.player.pos[1] -= self.player.speed
        if keys[pygame.K_s]:
            self.player.pos[1] += self.player.speed
        if keys[pygame.K_a]:
            self.player.pos[0] -= self.player.speed
        if keys[pygame.K_d]:
            self.player.pos[0] += self.player.speed


    def run(self):
        while True:
            #events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            #update
            self.update()
            animated.update(0.05)
            
            
            #drawing
            self.screen.fill('black')
            pygame.draw.circle(self.screen, (100,255,255), self.player.pos, self.player.radius) #a moving circle    | Player
            rock.draw(self.screen, True)    #rock   | Entity
            animated.draw(self.screen, True)    #stickman   | Animated Entity
            
            pygame.display.update()
            self.clock.tick(60)




if __name__=="__main__":
    game = Game()
    game.run()