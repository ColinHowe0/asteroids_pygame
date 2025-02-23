import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    score_text = pygame.font.Font(size=SCORE_FONT_SIZE)


    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, drawable, shots)

    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    score = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000

        updateable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                quit()
            for shot in shots:
                if asteroid.collides(shot):
                    score += 1
                    asteroid.split()
                    shot.kill()

        pygame.Surface.fill(screen, (0,0,0))
        pygame.Surface.blit(screen, score_text.render(f"SCORE: {score}", True, (0, 255, 0)), (0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
