import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.position.x), int(self.position.y)), int(self.radius), 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, self.rotate(random_angle) * 1.2)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, self.rotate(-random_angle) * 1.2)
        asteroids.add(new_asteroid1, new_asteroid2)
        
                
    def rotate(self, angle):
        return self.velocity.rotate(angle)