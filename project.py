import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
ss=pygame.display.set_caption("my first game screen")
done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True
    pygame.draw.rect(screen, (125,125,125), pygame.Rect(180,180,170,170))
    pygame.display.flip()