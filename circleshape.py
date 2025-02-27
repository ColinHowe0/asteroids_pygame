import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # sub classes must override
    def draw(self, screen):
        pass

    # sub classes must override
    def update(self, dt):
        pass

    def collides(self, other: 'CircleShape'):
        if self.position.distance_to(other.position) <= self.radius + other.radius:
            return True
        return False