import pygame



pygame.init()


#creates game screen and caption
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Scrolling Platformer")

gameover = False
clock = pygame.time.Clock()

player = [100, 550, 0, 0]# xpos ypos xVel yVel 
touchGround = False
offset = 0

platforms = [(500,400), (700, 300)] 

def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150,10,10), (platforms[i][0] + offset, platforms[i][1], 100, 30))

def move_player():
    global touchGround, offset
    keys = pygame.key.get_pressed()

 
    if not touchGround:
        player[3] += 1 
    else:
        player[3] = 0  

  
    if player[3] > 10:
        player[3] = 10


    if player[1] >= 450:
        player[1] = 450
        touchGround = True

 
    on_platform = False
    for i in range(len(platforms)):
        platform_x = platforms[i][0] + offset
        platform_y = platforms[i][1]
        if player[0] + 50 > platform_x and player[0] < platform_x + 100:
            if player[1] + 50 >= platform_y and player[1] + 50 <= platform_y + 30:
                on_platform = True
                player[1] = platform_y - 50
                player[3] = 0 

    touchGround = on_platform or player[1] >= 450


    if keys[pygame.K_a]:
        if player[0] > 0:
            player[0] -= 5
        elif offset < 0:
            offset += 5

    elif keys[pygame.K_d]:  # Move right
        if player[0] < 750:
            player[0] += 5
        elif offset > -1500:
            offset -= 5

    if touchGround and keys[pygame.K_w]:
        player[3] = -15
        touchGround = False


    player[1] += player[3]

 

     

def draw_clouds():
    for x in range(100, 800, 300):
        for i in range(3):
            pygame.draw.circle(screen, (255,255,255), (x + offset, 100), 40)
            pygame.draw.circle(screen, (255,255,255), (x - 50 + offset, 125), 40)
            pygame.draw.circle(screen, (255,255,255), (x + 50 + offset, 125), 40)
            pygame.draw.rect(screen, (255,255,255), (x - 50 + offset, 100, 100, 65)) 


def draw_trees():
    for x in range(100, 800, 300):
        for i in range(3): 
            pygame.draw.rect(screen, (150,75,0), (x - 15 + offset, 300, 30, 200)) 
            pygame.draw.circle(screen, (32,130,32), (x + offset, 300), 40)
            pygame.draw.circle(screen, (32,130,32), (x - 50 + offset, 325), 40)
            pygame.draw.circle(screen, (32,130,32), (x + 50 + offset, 325), 40)



#BEGIN GAME LOOP######################################################
while not gameover:
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True


   


    #keyboard input-----------------------------------

    move_player()
     
    #render section-----------------------------------vis
    screen.fill((135,206,235))

    draw_clouds()
    draw_trees()
    draw_platforms() 
    pygame.draw.rect(screen, (34,140,34), (0, 500, 800, 600)) 
    pygame.draw.rect(screen, (255,0,255), (player[0], player[1], 50, 50))



    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()