import pygame
from random import randint


pygame.init() #Khởi tạo pygame
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
WHITE  = (255,255,255)
x_bird = 50
y_bird = 350
tube1_x =400
tube2_x = 600
tube3_x = 800
tube_width = 50
d_2tube= 150
bird_drop_velocity = 0
gravity = 0.5
tube_velocity = 2
score = 0
font= pygame.font.SysFont("san",20)
font1= pygame.font.SysFont("san",50)
tube1_height = randint(100,400)
tube2_height = randint(100,400)
tube3_height = randint(100,400)
background_img = pygame.image.load("./Python_basic_Tutorial/Flappybird/flappy bird/images/background.png")
background_img = pygame.transform.scale(background_img,(400,600))
bird_img = pygame.image.load("./Python_basic_Tutorial/Flappybird/flappy bird/images/bird.png")
bird_img = pygame.transform.scale(bird_img,(35,35))
tube_img = pygame.image.load("./Python_basic_Tutorial/Flappybird/flappy bird/images/tube.png")
tube_op_img = pygame.image.load("./Python_basic_Tutorial/Flappybird/flappy bird/images/tube_op.png")
sand_img = pygame.image.load("./Python_basic_Tutorial/Flappybird/flappy bird/images/sand.png")
sand_img = pygame.transform.scale(sand_img,(400,30))
sound = pygame.mixer.Sound("./Python_basic_Tutorial/Flappybird/flappy bird/no6.wav")

tube1_pass = False
tube2_pass =False
tube3_pass = False
pausing = False
running = True

while running:
    pygame.mixer.Sound.play(sound)
    clock.tick(60) #Nháy màn hình 60 lần 1 giây
    screen.fill(WHITE)
    screen.blit(background_img, (0,0))
    #ép ống và vẽ ống
    tube1_img = pygame.transform.scale(tube_img,(tube_width,tube1_height))
    tube1 = screen.blit(tube1_img,(tube1_x,0))
    tube2_img = pygame.transform.scale(tube_img, (tube_width, tube2_height))
    tube2 = screen.blit(tube2_img, (tube2_x, 0))
    tube3_img = pygame.transform.scale(tube_img, (tube_width, tube3_height))
    tube3 = screen.blit(tube3_img, (tube3_x, 0))
    #ép và sẽ ống đối diện
    tube1_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-(tube1_height+d_2tube)))
    tube1_op = screen.blit(tube1_op_img, (tube1_x, tube1_height+d_2tube))
    tube2_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600 - (tube2_height + d_2tube)))
    tube2_op = screen.blit(tube2_op_img, (tube2_x, tube2_height + d_2tube))
    tube3_op_img = pygame.transform.scale(tube_op_img, (tube_width, 600-(tube3_height+d_2tube)))
    tube3_op = screen.blit(tube3_op_img, (tube3_x, tube3_height+d_2tube))
    # left move
    tube1_x -= tube_velocity
    tube2_x -= tube_velocity
    tube3_x -= tube_velocity
    # create new tube
    if tube1_x<-tube_width:
        tube1_x = 550
        tube1_height = randint(100,400)
        tube1_pass = False
    if tube2_x<-tube_width:
        tube2_x = 550
        tube2_height = randint(100,400)
        tube2_pass = False
    if tube3_x<-tube_width:
        tube3_x = 550
        tube3_height = randint(100,400)
        tube3_pass = False
    #draw sand
    sand = screen.blit(sand_img,(0,570))
    # draw bird
    bird = screen.blit(bird_img,(x_bird,y_bird))
    #bird drop
    y_bird += bird_drop_velocity
    bird_drop_velocity += gravity
    #score
    score_txt = font.render("Score: "+ str(score),True,"RED")
    screen.blit(score_txt,(5,5))
    #Cộng điêmr
    if tube1_x+tube_width<= x_bird and tube1_pass == False:
        score +=1
        tube1_pass = True
    if tube2_x+tube_width<= x_bird and tube2_pass == False:
        score +=1
        tube2_pass = True
    if tube3_x+tube_width<= x_bird and tube3_pass == False:
        score +=1
        tube3_pass = True
    #Kiem tra sự va chạm
    tubes = [tube1,tube2,tube3,tube3_op,tube1_op,tube2_op,sand]
    for tube in tubes:
        if bird.colliderect(tube):
            pygame.mixer.pause()
            tube_velocity = 0
            bird_drop_velocity = 0
            game_over_txt = font1.render("Game over, Score:"+str(score),True,"RED")
            screen.blit(game_over_txt,(50,260))
            space_txt = font.render("Press Space to continue!" + str(score), True, "GREEN")
            screen.blit(space_txt, (100, 310))
            pausing = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_drop_velocity = 0
                bird_drop_velocity -= 7
                if pausing:
                    pygame.mixer.unpause()
                    x_bird = 50
                    y_bird = 350
                    tube1_x = 400
                    tube2_x = 600
                    tube3_x = 800
                    tube_velocity =2
                    score = 0
                    pausing = False

    pygame.display.flip()
pygame.quit()