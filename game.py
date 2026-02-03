import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((1020,574))
pygame.display.set_caption("Adventures of a cat named Yasha")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
 
myfont = pygame.font.Font('fonts/Sekuya-Regular.ttf', 40)
text_surface = myfont.render('KOTIK YASHA', False, 'Pink')

bg = pygame.image.load('images/bg.png').convert()
shift_right = [
    pygame.image.load('images/cat_right/cat_right1.png').convert_alpha(),
    pygame.image.load('images/cat_right/cat_right2.png').convert_alpha(),
    pygame.image.load('images/cat_right/cat_right3.png').convert_alpha()
]
shift_left = [
    pygame.image.load('images/cat_left/cat_left1.png').convert_alpha(),
    pygame.image.load('images/cat_left/cat_left2.png').convert_alpha(),
    pygame.image.load('images/cat_left/cat_left3.png').convert_alpha()
]



mouse = pygame.image.load('images/mouse1.png')
mouse_list_timer = []

player_anim_count = 0

bg_x = 0

player_speed = 10
player_x = 200
player_y = 430
is_jump = False
jump = 8

bg_sound = pygame.mixer.Sound('sounds/music_bg.mp3')
bg_sound.play(loops = -1)

mouse_timer = pygame.USEREVENT + 1
pygame.time.set_timer(mouse_timer, 3000) 

label = pygame.font.Font('fonts/Sekuya-Regular.ttf', 40)
lose_label = label.render('GAME OVER!', False, (248, 24, 148))
label_size = pygame.font.Font('fonts/Sekuya-Regular.ttf', 20)
restart_label = label_size.render('try again', False, 'Red')
restart_label_rect = restart_label.get_rect(topleft=(425,325))
gameplay =  True


running = True
while running:

    keys = pygame.key.get_pressed()

    screen.blit(bg, (bg_x,0))
    screen.blit(bg, (bg_x + 1020,0))
    screen.blit(text_surface, (50,50))

    if gameplay:

        player_rect = shift_left[0].get_rect(topleft=(player_x, player_y))
        

        if mouse_list_timer:
            for (i, el) in enumerate(mouse_list_timer):
                screen.blit(mouse, el)
                el.x -= 10

                if el.x < -10:
                    mouse_list_timer.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        if keys[pygame.K_LEFT]:
            screen.blit(shift_left[player_anim_count], (player_x,player_y))
        else:
            screen.blit(shift_right[player_anim_count], (player_x,player_y))

        if keys[pygame.K_RIGHT] and player_x < 700:
            player_x += player_speed
        elif keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed

        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump >= -8:
                if jump > 0:
                    player_y -= (jump ** 2) / 2
                else:
                    player_y += (jump ** 2) / 2
                jump -= 1
            else:
                is_jump = False
                jump = 8


        if player_anim_count == 2:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 2
        if bg_x == -1024:
            bg_x = 0

    else:
        screen.fill((255, 179, 198))
        screen.blit(lose_label, (325,250))
        screen.blit(restart_label, restart_label_rect)

        mouse_pos = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 50
            mouse_list_timer.clear()



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == mouse_timer:
            mouse_list_timer.append(mouse.get_rect(topleft=(1024, 450)))

    
    

    clock.tick(15)


    