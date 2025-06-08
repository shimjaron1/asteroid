from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    # Override draw() method from circleshape and use position, radius, and width of 2
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self, dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20,50)

        asteroid_1_vector = self.velocity.rotate(random_angle)
        asteroid_2_vector = self.velocity.rotate(-random_angle)

        asteroid_1_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_2_radius = self.radius - ASTEROID_MIN_RADIUS
        
        asteroid_1 = Asteroid(self.position.x, self.position.y, asteroid_1_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, asteroid_2_radius)

        asteroid_1.velocity = asteroid_1_vector * ASTEROID_SPLIT_SPEED_INC
        asteroid_2.velocity = asteroid_2_vector * ASTEROID_SPLIT_SPEED_INC

