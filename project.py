import pygame
pygame.init()
screen=pygame.display.set_mode((640,480))
ss=pygame.display.set_caption("my first game screen")
pygame.draw.rect(screen, (125,125,125), pygame.Rect(200,200,120, 120))
text_font=pygame.font.Font(None, 36)
text_surface=text_font.render("Hello, Pygame!", True, (255, 255, 255))
screen.blit(text_surface, (200, 200))
pygame.display.flip()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()