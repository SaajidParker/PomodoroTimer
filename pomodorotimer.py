import pygame
import sys
from button import Button

pygame.init()

WIDTH, HEIGHT = 1000, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Saiyan Timer")

CLOCK = pygame.time.Clock()

BACKDROP = pygame.image.load("assets/backdrop.png")
WHITE_BUTTON = pygame.image.load("assets/button.png")

FONT = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 120)
timer_text_rect = FONT.size("25:00")
timer_text_pos = (WIDTH // 2 - timer_text_rect[0] // 2, HEIGHT // 2 - timer_text_rect[1] // 2)

START_STOP_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2+100), 170, 60, "START", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#000000", "#0000FF", "#FFFF00")
POMODORO_BUTTON = Button(WHITE_BUTTON, (WIDTH/2-150, HEIGHT/2-140), 140, 40, "Pomodoro", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#000000", "#0000FF", "#FFFF00")
SHORT_BREAK_BUTTON = Button(WHITE_BUTTON, (WIDTH/2, HEIGHT/2-140), 140, 40, "Short Break", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#000000", "#0000FF", "#FFFF00")
LONG_BREAK_BUTTON = Button(WHITE_BUTTON, (WIDTH/2+150, HEIGHT/2-140), 140, 40, "Long Break", 
                    pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20), "#000000", "#0000FF", "#FFFF00")


POMODORO_LENGTH = 1500 # 1500 secs / 25 mins
SHORT_BREAK_LENGTH = 300 # 300 secs / 5 mins
LONG_BREAK_LENGTH = 900 # 900 secs / 15 mins

current_seconds = POMODORO_LENGTH
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if START_STOP_BUTTON.check_for_input(pygame.mouse.get_pos()):
                if started:
                    started = False
                else:
                    started = True
            if POMODORO_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = POMODORO_LENGTH
                started = False
            if SHORT_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = SHORT_BREAK_LENGTH
                started = False
            if LONG_BREAK_BUTTON.check_for_input(pygame.mouse.get_pos()):
                current_seconds = LONG_BREAK_LENGTH
                started = False
            if started:
                START_STOP_BUTTON.text_input = "STOP"
                START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
            else:
                START_STOP_BUTTON.text_input = "START"
                START_STOP_BUTTON.text = pygame.font.Font("assets/ArialRoundedMTBold.ttf", 20).render(
                                        START_STOP_BUTTON.text_input, True, START_STOP_BUTTON.base_color)
        if event.type == pygame.USEREVENT and started:
            current_seconds -= 1

    SCREEN.fill("#ba4949")
    SCREEN.blit(BACKDROP, BACKDROP.get_rect(center=(WIDTH/2, HEIGHT/2)))

    START_STOP_BUTTON.update(SCREEN)
    START_STOP_BUTTON.change_color(pygame.mouse.get_pos())
    POMODORO_BUTTON.update(SCREEN)
    POMODORO_BUTTON.change_color(pygame.mouse.get_pos())
    SHORT_BREAK_BUTTON.update(SCREEN)
    SHORT_BREAK_BUTTON.change_color(pygame.mouse.get_pos())
    LONG_BREAK_BUTTON.update(SCREEN)
    LONG_BREAK_BUTTON.change_color(pygame.mouse.get_pos())

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
    timer_text = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    timer_text_outline = FONT.render(f"{display_minutes:02}:{display_seconds:02}", True, "black")

    SCREEN.blit(timer_text_outline, (timer_text_pos[0] - 2, timer_text_pos[1] - 2))
    SCREEN.blit(timer_text_outline, (timer_text_pos[0] + 2, timer_text_pos[1] + 2))
    SCREEN.blit(timer_text_outline, (timer_text_pos[0] - 2, timer_text_pos[1] + 2))
    SCREEN.blit(timer_text_outline, (timer_text_pos[0] + 2, timer_text_pos[1] - 2))
    SCREEN.blit(timer_text, timer_text_pos)

    pygame.display.update()
    CLOCK.tick(60)
