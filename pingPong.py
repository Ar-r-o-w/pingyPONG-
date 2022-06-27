import pygame
pygame.init()
pygame.mixer.init()

import time



HEIGHT = 400
WDTH = 700
FPS = 30

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WDTH, HEIGHT))
pygame.display.set_caption('a tiled One')
clock = pygame.time.Clock()

font = pygame.font.SysFont("Ariel", 50)


def blit_text(msg, color, x, y):

    
    text = font.render(msg, True, color)
    screen.blit(text, (x,y))
def main():
    p1 = 0
    p2 = 0
    
    PADDLE_HEIGHT = 100
    PADDLE_WDTH = 10

    SPAWNY_P1 = HEIGHT/2-50
    SPAWNX_P1 = 10

    SPAWNY_P2 = HEIGHT/2-50
    SPAWNX_P2 = WDTH-PADDLE_WDTH-10

    running = True

    PONG_X = WDTH/2
    PONG_Y = HEIGHT/2

    PONG_S = 10

    v = 7
    x = 7
    y = 7
    while running:
        clock.tick(FPS)
    # PROCESS INPUT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_w]:
            SPAWNY_P1 += -v
        if keys[pygame.K_s]:
            SPAWNY_P1 += v

        if keys[pygame.K_UP]:
            SPAWNY_P2 += -v
        if keys[pygame.K_DOWN]:
            SPAWNY_P2 += v

        

        

    #UPDATE SECTION
        PONG_X += -x
        PONG_Y += -y

        if PONG_Y <= 0 or PONG_Y+PONG_S >= HEIGHT :
            y = y*-1

        if PONG_X <= 0:
            
            print("P2 WIN and P2 LOSE")
            time.sleep(2)
            
            p2+=1

            PONG_X = WDTH/2
            PONG_Y = HEIGHT/2
            
            
            
        if PONG_X + PONG_S >= WDTH:
            
            print("P1 WINS and P2 LOSE")
            time.sleep(2)
            
            p1+=1
            
            PONG_X = WDTH/2
            PONG_Y = HEIGHT/2
            
            
            
            
        if PONG_X <= SPAWNX_P1 + PADDLE_WDTH:
            if PONG_Y >= SPAWNY_P1 and PONG_Y <= SPAWNY_P1 + PADDLE_HEIGHT:
                x = x* -1

        if PONG_X +PONG_S >= SPAWNX_P2:
            if PONG_Y >= SPAWNY_P2 and PONG_Y <= SPAWNY_P2 + PADDLE_HEIGHT:
                x = x * -1
        
        #print(pygame.Surface.get_at((0,0),))
                
    # draw
        screen.fill(WHITE)
        

        
        #PADDLES
        pygame.draw.rect(screen, BLACK, (SPAWNX_P1, SPAWNY_P1, PADDLE_WDTH, PADDLE_HEIGHT))
        pygame.draw.rect(screen, BLACK, (SPAWNX_P2, SPAWNY_P2, PADDLE_WDTH, PADDLE_HEIGHT))
       
        #SCORE
        blit_text(str(p1), RED, 5,5)
        blit_text(str(p2), BLUE, WDTH-20,5)
        #PONG
        pygame.draw.rect(screen, BLACK, (PONG_X, PONG_Y, PONG_S, PONG_S))

        if p1 == 3:
            win = True
            while win:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                keys = pygame.key.get_pressed()
                if keys[pygame.K_q]:
                    pygame.quit()
                if keys[pygame.K_c]:
                    main()
           
                blit_text("P1 Wins It All", GREEN, WDTH/2-100, HEIGHT/2-150)
                
            
                pygame.display.update()
            
        if p2 ==3:
            win = True
            while win:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                if keys[pygame.K_q]:
                    yearlyFanatics.menu()
                if keys[pygame.K_c]:
                    main()
                    
                blit_text("P2 Wins It All", GREEN, WDTH/2-100, HEIGHT/2-150)
                pygame.quit()
                
                pygame.display.update()
            
            
            

        pygame.display.flip()


if __name__ == "__main__":
  main()
