import pygame
import sounds

pygame.init()

#input: the button's text, x coordinate, y coordinate
#returns the list of the 4 components that need to be separately blit on the screen to create a button
#returns button surface, button text, text rectangle, and button rectangle
def button_creation(text, x, y):
    font = pygame.font.Font("resources/Grand9KPixel.ttf", 25)
    choose_char = pygame.Surface((200,50))
    choose_char.fill("#f2461f")
    char_text = font.render(text, True, "#ebfbfc")
    char_text_rect = char_text.get_rect(center=(choose_char.get_width()/2, choose_char.get_height()/2))
    button_rect = pygame.Rect(x, y, 200, 50)
    return [choose_char, char_text, char_text_rect, button_rect]

#create the screen and configure the screen size, background color, and caption
screen_info = pygame.display.Info()
screen = pygame.display.set_mode((screen_info.current_w, screen_info.current_h))
screen.fill("#32a0a8")
pygame.display.set_caption("SpartanDash")
pygame.display.flip()

#load custom font from ttf file and set size for different types of text
title_font = pygame.font.Font("resources/Grand9KPixel.ttf", 60)
subtitle_font = pygame.font.Font("resources/Grand9KPixel.ttf", 40)

segment_width = screen_info.current_w/4
#use button_creation function to create select buttons for both characters and next button
choose_neha = button_creation("Choose Neha", (segment_width - 75), 2 * (screen_info.current_h/3))
choose_anusri = button_creation("Choose Anusri", 2* (segment_width) - 75, 2 * (screen_info.current_h/3))
choose_erica = button_creation("Choose Erica", 3 * (segment_width) - 75, 2 * (screen_info.current_h/3))
next_button = button_creation("Next", screen_info.current_w - 300, screen_info.current_h - 200)

#load sprite images and resize them
DEFAULT_SIZE = (300, 300)
anusri_img = pygame.image.load("resources/Anusri_Sprite.png")
anusri_img = pygame.transform.scale(anusri_img, DEFAULT_SIZE)

neha_img = pygame.image.load("resources/Neha_Sprite.png")
neha_img = pygame.transform.scale(neha_img, DEFAULT_SIZE)

erica_img = pygame.image.load("resources/Erica_Sprite.png")
erica_img = pygame.transform.scale(erica_img, DEFAULT_SIZE)


#initialize variables before running the character_selection page
def run():
    running = True
    character_selected = ""
    #while the page is running
    while running:
        #register interactions with the screen
        for event in pygame.event.get():
            #exit the loop and close the screen in player quits
            if event.type == pygame.QUIT:
                return "Quit"
            #if player clicks on the screen
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                #store "neha" as selected character and configure button colors to show selection
                if choose_neha[3].collidepoint(mouse_position):
                    pygame.mixer.Sound.play(sounds.click)
                    choose_neha[0].fill("#f77a5e")
                    choose_anusri[0].fill("#f2461f")
                    choose_erica[0].fill("#f2461f")
                    character_selected = "Neha"
                    print("Neha")
                #store "anusri" as selected character and configure button colors to show selection
                elif choose_anusri[3].collidepoint(mouse_position):
                    pygame.mixer.Sound.play(sounds.click)
                    choose_anusri[0].fill("#f77a5e")
                    choose_neha[0].fill("#f2461f")
                    choose_erica[0].fill("#f2461f")
                    character_selected = "Anusri"
                    print("Anusri")
                elif choose_erica[3].collidepoint(mouse_position):
                    pygame.mixer.Sound.play(sounds.click)
                    choose_erica[0].fill("#f77a5e")
                    choose_anusri[0].fill("#f2461f")
                    choose_neha[0].fill("#f2461f")
                    character_selected = "Erica"
                    print("Erica")
                #create or open the existing "selected_character.txt" file and write the finally selected character to the file
                #move to the next page
                elif next_button[3].collidepoint(mouse_position) and character_selected != "":
                    pygame.mixer.Sound.play(sounds.click)
                    next_button[0].fill("#f77a5e")
                    with open("saved_states/selected_character.txt", "w") as file:
                        file.write(character_selected)
                    return "Next"
        
        #while the program is running, display the title and subtitle on the screen
        title = title_font.render("Spartan Dash: Campus Run", True, "#FFD700")
        screen.blit(title, ((screen_info.current_w / 2 - title.get_width() / 2), 50))
        instruction = subtitle_font.render("Choose your character.", True, "#ebfbfc")
        screen.blit(instruction, ((screen_info.current_w/2 - instruction.get_width()/2), 150))

        # while the program is running, display the Select character buttons
        choose_neha[0].blit(choose_neha[1], choose_neha[2])
        choose_anusri[0].blit(choose_anusri[1], choose_anusri[2])
        choose_erica[0].blit(choose_erica[1], choose_erica[2])
        screen.blit(choose_neha[0], (choose_neha[3].x, choose_neha[3].y))
        screen.blit(choose_anusri[0], (choose_anusri[3].x, choose_anusri[3].y))
        screen.blit(choose_erica[0], (choose_erica[3].x, choose_erica[3].y))

        #while the program is running, display the character images on the screen
        screen.blit(anusri_img, (choose_anusri[3].x - 50, choose_anusri[3].y - anusri_img.get_height() - 50))
        screen.blit(neha_img, (choose_neha[3].x - 50, choose_neha[3].y - neha_img.get_height() - 50))
        screen.blit(erica_img, (choose_erica[3].x - 50, choose_erica[3].y - erica_img.get_height() - 50))


        #display the next button only after one of the characters has been selected
        if character_selected != "":
            next_button[0].blit(next_button[1], next_button[2])
            screen.blit(next_button[0], (next_button[3].x, next_button[3].y))

        #update all the changes while the screen is running
        pygame.display.update()