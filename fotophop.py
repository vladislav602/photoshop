import pygame

class Hero:
    def init(self, x,y, texture, width, height, speed):
        self.image = pygame.image.load(texture)
        self.image = pygame.transform.scale(self.image, [width, height])
        self.hitbox = self.image.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed


    def draw(self, window):
        window.blit(self.image, [self.hitbox.x, self.hitbox.y])

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
pygame.init()

window = pygame.display.set_mode([700, 500])
fps = pygame.time.Clock()

background = pygame.transform.scale(pygame.image.load("background.png"), [700, 500])

player1 = Hero(250, 250, "sprite1.png", 50, 50, 10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    player1.move()


    window.fill([0, 250, 0])
    window.blit(background, [0, 0])
    player1.draw(window)
    pygame.display.flip()

    fps.tick(60)