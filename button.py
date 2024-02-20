import pygame

class Button():
    def __init__(self, surface=None, pos=None, width=None, height=None, text_input=None, font=None, base_color=None, hovering_color=None, border_color=None):
        self.surface = surface
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.width = width
        self.height = height
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.border_color = border_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.surface is None:
            self.surface = pygame.Surface((width, height))
            self.surface.fill(base_color)
        else:
            self.surface = pygame.transform.smoothscale(self.surface, (width, height))
        self.rect = self.surface.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        screen.blit(self.surface, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self, position):
        return self.rect.collidepoint(position)

    def change_color(self, position):
        if self.rect.collidepoint(position):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
            pygame.draw.rect(self.surface, self.border_color, self.rect, 3)  # Draw border
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
            pygame.draw.rect(self.surface, self.base_color, self.rect, 3)  # Draw border
