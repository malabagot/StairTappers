import pygame
import random

from sys import exit
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("StairTappers")
clock = pygame.time.Clock()

#This is to load the background image

background_surface = pygame.image.load('Sky.png').convert_alpha()
text_font = pygame.font.Font('freesansbold.ttf', 24)
click = pygame.mixer.Sound('Click.aiff')
home_title = pygame.image.load('HomeScreen.png').convert_alpha()
play_button = pygame.image.load('PlayButton.png').convert_alpha()
select_button = pygame.image.load('Select.png').convert_alpha()
weakly_damaged_sky = pygame.image.load('WeaklyDamagedSky.png').convert_alpha()
damaged_sky = pygame.image.load('DamagedSky.png').convert_alpha()
main_menu_music = pygame.mixer.music.load('MenuMusic.wav')
start_sound = pygame.mixer.Sound('Start.wav')
customize_button = pygame.image.load('Customize.png').convert_alpha()
border = pygame.image.load('Border.png').convert_alpha()

def correct_step_checker(a_or_d, randint_list):
    if a_or_d == "a":
        if randint_list[0] == -1:
            return True
        else:
            return False

    if a_or_d == "d":
        if randint_list[0] == 1:
            return True
        else:
            return False

def fail_sequence(stunned):
    fail_sound = pygame.mixer.Sound('Fail.wav')
    fail_sound.play()
    stunned = True
    return stunned


def step_generation(step1x, step1y, randint1, step2x, step2y, randint2, step3x, step3y, randint3, step4x, step4y,
                    randint4, step5x, step5y, randint5, step6x, step6y, randint6, step7x, step7y, randint7, step8x,
                    step8y, randint8, step9x, step9y, randint9, randint_list,eight_click_counter):
    if eight_click_counter == 5:
        randint1 = random.choice([1, -1])

def cloud_generator(available_cloudy,which_cloud):
    cloud1_direction = random.choice([1, -1])

    if which_cloud == 1:
        if cloud1_direction == 1:
            cloud1x = 0 - 200
            cloud1x_end = 600
        else:
            cloud1x = 600
            cloud1x_end = 0 - 200

        cloud1y = available_cloudy[random.randint(0,len(available_cloudy)-1)]
        print(available_cloudy, "before removing cloud1 after first generation")
        if cloud1y in available_cloudy:
            print(cloud1y, "found in available_cloudy")
            available_cloudy.remove(cloud1y)
            print(available_cloudy, "After removing cloud1 after first generation")
        return cloud1x, cloud1y, cloud1_direction, cloud1x_end, available_cloudy

    elif which_cloud == 2:
        cloud2_direction = random.choice([1, -1])
        if cloud2_direction == 1:
            cloud2x = 0 - 100
            cloud2x_end = 600
        else:
            cloud2x = 600
            cloud2x_end = 0 - 100

        cloud2y = available_cloudy[random.randint(0,len(available_cloudy)-1)]
        if cloud2y in available_cloudy:
            available_cloudy.remove(cloud2y)
        return cloud2x, cloud2y, cloud2_direction, cloud2x_end, available_cloudy

    elif which_cloud == 3:
        cloud3_direction = random.choice([1, -1])
        if cloud3_direction == 1:
            cloud3x = 0 - 100
            cloud3x_end = 600
        else:
            cloud3x = 600
            cloud3x_end = 0 - 100

        cloud3y = available_cloudy[random.randint(0,len(available_cloudy)-1)]
        if cloud3y in available_cloudy:
            available_cloudy.remove(cloud3y)
        return cloud3x, cloud3y, cloud3_direction, cloud3x_end, available_cloudy

    elif which_cloud == 4:
        cloud4_direction = random.choice([1, -1])
        if cloud4_direction == 1:
            cloud4x = 0 - 100
            cloud4x_end = 600
        else:
            cloud4x = 600
            cloud4x_end = 0 - 100

        cloud4y = available_cloudy[random.randint(0,len(available_cloudy)-1)]
        if cloud4y in available_cloudy:
            available_cloudy.remove(cloud4y)
        return cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy

def cloud_mover(cloud1x, cloud1_direction, cloud2x, cloud2_direction, cloud3x, cloud3_direction, cloud4x,
                cloud4_direction):
    cloud1x += cloud1_direction
    cloud2x += cloud2_direction*1.1
    cloud3x += cloud3_direction*0.9
    cloud4x += cloud4_direction

    return cloud1x, cloud2x, cloud3x, cloud4x

def cloud_regenerator(cloud1x, cloud1y, cloud1_direction, cloud1x_end, cloud2x, cloud2y, cloud2_direction, cloud2x_end,
                      cloud3x, cloud3y, cloud3_direction, cloud3x_end, cloud4x, cloud4y, cloud4_direction, cloud4x_end,
                      available_cloudy):
    if cloud1_direction == 1:
        if cloud1x > cloud1x_end:
            available_cloudy.append(cloud1y)
            cloud1x, cloud1y, cloud1_direction, cloud1x_end, available_cloudy = cloud_generator(available_cloudy,1)
    else:
        if cloud1x < cloud1x_end:
            available_cloudy.append(cloud1y)
            cloud1x, cloud1y, cloud1_direction, cloud1x_end, available_cloudy = cloud_generator(available_cloudy,1)

    if cloud2_direction == 1:
        if cloud2x > cloud2x_end:
            available_cloudy.append(cloud2y)
            cloud2x, cloud2y, cloud2_direction, cloud2x_end, available_cloudy = cloud_generator(available_cloudy,2)
    else:
        if cloud2x < cloud2x_end:
            available_cloudy.append(cloud2y)
            cloud2x, cloud2y, cloud2_direction, cloud2x_end, available_cloudy = cloud_generator(available_cloudy, 2)

    if cloud3_direction == 1:
        if cloud3x > cloud3x_end:
            available_cloudy.append(cloud3y)
            cloud3x, cloud3y, cloud3_direction, cloud3x_end, available_cloudy = cloud_generator(available_cloudy,3)
    else:
        if cloud3x < cloud3x_end:
            available_cloudy.append(cloud3y)
            cloud3x, cloud3y, cloud3_direction, cloud3x_end, available_cloudy = cloud_generator(available_cloudy,3)

    if cloud4_direction == 1:
        if cloud4x > cloud4x_end:
            available_cloudy.append(cloud4y)
            cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy = cloud_generator(available_cloudy,4)
    else:
        if cloud4x < cloud4x_end:
            available_cloudy.append(cloud4y)
            cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy = cloud_generator(available_cloudy,4)

    return cloud1x, cloud1y, cloud1_direction, cloud1x_end, cloud2x, cloud2y, cloud2_direction, cloud2x_end, cloud3x, cloud3y, cloud3_direction, cloud3x_end, cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy

def main_menu():
    global background_surface, text_font, click, home_title, screen, play_button, main_menu_music, start_sound, customize_button, border
    screen.blit(background_surface, (0, 0))
    screen.blit(home_title, (0, 0))
    time_elapsed = 0
    pygame.mixer.music.play(loops=-1)

    while True:
        time_elapsed += round(clock.tick(60) / 1000, 2)
        screen.blit(background_surface, (0, 0))
        screen.blit(home_title, (0, 0))
        screen.blit(border, (50,330))
        screen.blit(play_button, (100, 420))
        screen.blit(customize_button, (70,540))

        mousex, mousey = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if (mousey > 450 and mousey < 650):
                    if (mousex > 100 and mousex < 500):
                        pygame.mixer.music.stop()
                        start_sound.play()
                        main_game()


        if time_elapsed > 1:
            print(mousex, mousey)
            time_elapsed = 0

        if (mousey > 450 and mousey < 650):
            if (mousex > 100 and mousex < 500):
                screen.blit(select_button,(115,410))

        clock.tick(60)


        pygame.display.update()


def main_game():
    #playerx = 280
    #playery = 400
    global background_surface
    playerx = 500
    playery = 400
    stunned = False
    stun_timer = 0
    step1x = playerx - 20
    step1y = playery + 40
    cps = 0
    time_elapsed = 0
    last_step = None
    #movement clicks used for determining cps
    movement_clicks = 0
    randint1 = 1
    #counter used to determine generation of stairs
    eight_click_counter = 0
    cloud_count = 0
    available_cloudy = [100,200,300,400,500,600,700]
    # This is to load the sprite of the player
    player_surface = pygame.Surface((40, 40))
    player_surface.fill('orange')
    text_surface = text_font.render(f"Your speed is {cps}", False, (255, 255, 255))
    cloud1_surface = pygame.image.load('cloud1.png')
    cloud1_surface = pygame.transform.scale(cloud1_surface, (200, 100))

    cloud2_surface = pygame.image.load('cloud2.png')
    cloud2_surface = pygame.transform.scale(cloud2_surface, (100, 100))

    cloud3_surface = pygame.image.load('cloud3.png')
    cloud3_surface = pygame.transform.scale(cloud3_surface, (100, 100))

    cloud4_surface = pygame.image.load('cloud4.png')
    cloud4_surface = pygame.transform.scale(cloud4_surface, (100, 100))

    step_surface1 = pygame.image.load('Platform.png').convert_alpha()

    step_surface2 = pygame.image.load('Platform.png').convert_alpha()
    randint2 = random.choice([1, -1])
    step2x = step1x + 60 * randint2
    step2y = step1y - 100

    step_surface3 = pygame.image.load('Platform.png').convert_alpha()
    randint3 = random.choice([1, -1])
    step3x = step2x + 60 * randint3
    step3y = step2y - 100

    step_surface4 = pygame.image.load('Platform.png').convert_alpha()
    randint4 = random.choice([1, -1])
    step4x = step3x + 60 * randint4
    step4y = step3y - 100

    step_surface5 = pygame.image.load('Platform.png').convert_alpha()
    randint5 = random.choice([1, -1])
    step5x = step4x + 60 * randint5
    step5y = step4y - 100

    step_surface6 = pygame.image.load('Platform.png').convert_alpha()
    randint6 = random.choice([1, -1])
    step6x = step5x + 60 * randint6
    step6y = step5y - 100

    step_surface7 = pygame.image.load('Platform.png').convert_alpha()
    randint7 = random.choice([1, -1])
    step7x = step6x + 60 * randint7
    step7y = step6y - 100

    step_surface8 = pygame.image.load('Platform.png').convert_alpha()
    randint8 = random.choice([1, -1])
    step8x = step7x + 60 * randint8
    step8y = step7y - 100

    step_surface9 = pygame.image.load('Platform.png').convert_alpha()
    randint9 = random.choice([1, -1])
    step9x = step8x + 60 * randint9
    step9y = step8y - 100

    randint_list = [randint2, randint3, randint4, randint5]



    cloud1x, cloud1y, cloud1_direction, cloud1x_end, available_cloudy = cloud_generator(available_cloudy,1)
    cloud2x, cloud2y, cloud2_direction, cloud2x_end, available_cloudy = cloud_generator(available_cloudy,2)
    cloud3x, cloud3y, cloud3_direction, cloud3x_end, available_cloudy = cloud_generator(available_cloudy,3)
    cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy = cloud_generator(available_cloudy,4)

    while True:
        dt = round(clock.tick(100)/1000,2)
        time_elapsed += dt
        if time_elapsed > 1:
            cps = movement_clicks
            time_elapsed = 0
            movement_clicks = 0
        if stunned:
            stun_timer += dt
            if stun_timer < 0.5:
                background_surface = pygame.image.load('DamagedSky.png').convert_alpha()
            elif 0.5 < stun_timer < 2:
                background_surface = pygame.image.load('WeaklyDamagedSky.png').convert_alpha()

            if stun_timer > 2:
                stunned = False
                stun_timer = 0
                background_surface = pygame.image.load('Sky.png').convert_alpha()
    #This is to allow you to exit the game when you press the 'x' button
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                if stunned:
                    pass
                else:
                    # These are the immediate changes that occur when pressing 'a'
                    if event.key == K_a:
                        if correct_step_checker("a",randint_list):
                            playerx -= 60
                            playery -= 100
                            click.play()
                            movement_clicks += 1
                            eight_click_counter += 1
                            if eight_click_counter > 8:
                                eight_click_counter = 0
                            del randint_list[0]
                            last_step = True
                        else:
                            stunned = fail_sequence(stunned)
                            last_step = False

                #These are the immediate changes that occur when pressing 'd'
                    elif event.key == K_d:
                        if correct_step_checker("d", randint_list):
                            playerx += 60
                            playery -= 100
                            click.play()
                            movement_clicks += 1
                            eight_click_counter += 1
                            if eight_click_counter > 8:
                                eight_click_counter = 0
                            del randint_list[0]
                            last_step = True
                        else:
                            stunned = fail_sequence(stunned)
                            last_step = False

                    if eight_click_counter == 5 and last_step:
                        randint1 = random.choice([1, -1])
                        step1y = step9y - 100
                        step1x = step9x + 60 * randint1
                        randint_list.append(randint1)

                    if eight_click_counter == 6 and last_step:
                        randint2 = random.choice([1, -1])
                        step2y = step1y - 100
                        step2x = step1x + 60 * randint2
                        randint_list.append(randint2)

                    if eight_click_counter == 7 and last_step:
                        randint3 = random.choice([1, -1])
                        step3y = step2y - 100
                        step3x = step2x + 60 * randint3
                        randint_list.append(randint3)

                    if eight_click_counter == 8 and last_step:
                        randint4 = random.choice([1, -1])
                        step4y = step3y - 100
                        step4x = step3x + 60 * randint4
                        randint_list.append(randint4)

                    if eight_click_counter == 0 and last_step:
                        randint5 = random.choice([1, -1])
                        step5y = step4y - 100
                        step5x = step4x + 60 * randint5
                        randint_list.append(randint5)

                    if eight_click_counter == 1 and last_step:
                        randint6 = random.choice([1, -1])
                        step6y = step5y - 100
                        step6x = step5x + 60 * randint6
                        randint_list.append(randint6)

                    if eight_click_counter == 2 and last_step:
                        randint7 = random.choice([1, -1])
                        step7y = step6y - 100
                        step7x = step6x + 60 * randint7
                        randint_list.append(randint7)

                    if eight_click_counter == 3 and last_step:
                        randint8 = random.choice([1, -1])
                        step8y = step7y - 100
                        step8x = step7x + 60 * randint8
                        randint_list.append(randint8)

                    if eight_click_counter == 4 and last_step:
                        randint9 = random.choice([1, -1])
                        step9y = step8y - 100
                        step9x = step8x + 60 * randint9
                        randint_list.append(randint9)

                    print(randint_list)
                # This is where all platforms are regenerated when they leave the screen



        cloud1x, cloud2x, cloud3x, cloud4x = cloud_mover(cloud1x, cloud1_direction, cloud2x, cloud2_direction, cloud3x, cloud3_direction, cloud4x, cloud4_direction)
        cloud1x, cloud1y, cloud1_direction, cloud1x_end, cloud2x, cloud2y, cloud2_direction, cloud2x_end, cloud3x, cloud3y, cloud3_direction, cloud3x_end, cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy = cloud_regenerator(cloud1x, cloud1y, cloud1_direction, cloud1x_end, cloud2x, cloud2y, cloud2_direction, cloud2x_end, cloud3x, cloud3y, cloud3_direction, cloud3x_end, cloud4x, cloud4y, cloud4_direction, cloud4x_end, available_cloudy)
    #These are the transitions i made for it to look cool when leaping up the steps
        if playery < 400:
            smooth_y_shift = (400-playery)/10
            playery += smooth_y_shift
            step1y += smooth_y_shift
            step2y += smooth_y_shift
            step3y += smooth_y_shift
            step4y += smooth_y_shift
            step5y += smooth_y_shift
            step6y += smooth_y_shift
            step7y += smooth_y_shift
            step8y += smooth_y_shift
            step9y += smooth_y_shift
        if playerx != 280:
            smooth_x_shift = (280-playerx)/10
            playerx += smooth_x_shift
            step1x += smooth_x_shift
            step2x += smooth_x_shift
            step3x += smooth_x_shift
            step4x += smooth_x_shift
            step5x += smooth_x_shift
            step6x += smooth_x_shift
            step7x += smooth_x_shift
            step8x += smooth_x_shift
            step9x += smooth_x_shift

    #This is me actually putting the platforms, character and background onto the screen every single frame
        screen.blit(background_surface,(0,0))

        screen.blit(cloud1_surface, (cloud1x, cloud1y))
        screen.blit(cloud2_surface, (cloud2x, cloud2y))
        screen.blit(cloud3_surface, (cloud3x, cloud3y))
        screen.blit(cloud4_surface, (cloud4x, cloud4y))

        text_surface = text_font.render(f"Stairs per second: {cps} ", False, (255, 255, 255))
        text_surface2 = text_font.render(f"Your stun time is {stun_timer}", False, (255, 255, 255))

        screen.blit(step_surface1, (step1x,step1y))
        screen.blit(step_surface2, (step2x,step2y))
        screen.blit(step_surface3, (step3x,step3y))
        screen.blit(step_surface4, (step4x,step4y))
        screen.blit(step_surface5, (step5x,step5y))
        screen.blit(step_surface6, (step6x,step6y))
        screen.blit(step_surface7, (step7x,step7y))
        screen.blit(step_surface8, (step8x,step8y))
        screen.blit(step_surface9, (step9x,step9y))
        screen.blit(player_surface,(playerx,playery))
        screen.blit(text_surface,(0,0))
        screen.blit(text_surface2,(0,20))
    #This is to actually allow the game to run
        pygame.display.update()

main_menu()