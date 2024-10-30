import pygame
import random
pygame.init()

W, H = 800, 600
display = pygame.display.set_mode((W, H))
pygame.display.set_caption('ТИР')
score = 0

def draw_score(score):

    font=pygame.font.Font(None, 50)
    text=font.render(f'Score:{score}',True,"yellow")
    text_rect=text.get_rect()
    display.blit(text,text_rect)

class Object:
    def __init__(self,img):
        self.image = pygame.image.load(img)
        self.rect=self.image.get_rect()

    def draw(self):
        display.blit(self.image, self.rect)

    def is_clicked(self, sprite):
        click = pygame.mouse.get_pressed(num_buttons=5)

        if click[0]:  # левой

            hit_x = self.rect.left < sprite.rect.centerx < self.rect.right
            hit_y = self.rect.top < sprite.rect.centery < self.rect.bottom
            return hit_x and hit_y



    def move(self):
        global score
        if self.is_clicked(scope):
            score += 1
            self.rect.x = random.randint(0, W - self.image.get_width())
            self.rect.y = random.randint(0, H - self.image.get_height())


target=Object("target_small.png")
scope=Object("crosshair_small.png")

#target = pygame.image.load('target_small.png')
#target_rect = target.get_rect()

#scope=pygame.image.load('crosshair_small.png')
#scope_rect = scope.get_rect()

def main ():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        scope.rect.center = pygame.mouse.get_pos()
        display.fill('blue')
        target.draw()
        scope.draw()
        target.move()
        draw_score(score)
#        display.blit(target, target_rect)
#       display.blit(scope, scope_rect)
        pygame.display.update()

main()


