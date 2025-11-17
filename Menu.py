import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)

class Menu:
    def __init__(self, screen, options, title, additional_text=None, additional_text_size=24, bg=None, font=None, font_size=48, bg_color=BLACK, text_color=WHITE, highlight_color=BLUE, title_size=120, title_color=WHITE):
        # Initialize menu attributes
        self.screen = screen
        self.options = options
        self.selected = 0 # Currently selected option
        self.option_font = pygame.font.SysFont(font, font_size)

        # Defaults
        self.additional_text = additional_text   # Optional additional text to display
        self.additional_font = pygame.font.SysFont(font, additional_text_size)
        self.title_font = pygame.font.SysFont(font, title_size, bold=True)
        self.bg = bg
        self.bg_color = bg_color
        self.text_color = text_color
        self.highlight_color = highlight_color   # Color for highlighted option
        self.title = title
        self.title_color = title_color
        self.running = True
        self.button_rects = []

    # Draw the menu
    def draw(self):
        # Clear screen or draw background
        if self.bg:
            self.screen.blit(self.bg, (0, 0))
        else:
            self.screen.fill(self.bg_color)

        # Get screen dimensions
        h = self.screen.get_height()
        w = self.screen.get_width()
        self.button_rects = []

        # Draw Title
        title_surf = self.title_font.render(self.title, True, self.title_color)
        title_rect = title_surf.get_rect(center=(w // 2, h // 6))
        self.screen.blit(title_surf, title_rect)

        # Calculate start position for menu options
        total_h = len(self.options) * self.option_font.get_height()
        start_y = h // 3

        # Tracks mouse movement
        mouse_x, mouse_y = pygame.mouse.get_pos()
        hovered = None

        # Draw each option
        for i, opt in enumerate(self.options):
            color = self.text_color
            # Default state for button highlight
            text_surf = self.option_font.render(opt, True, color)
            text_rect = text_surf.get_rect(center=(w // 2, start_y + i * self.option_font.get_height() * 1.2))
            self.button_rects.append(text_rect)

            # Highlight if mouse is over OR selected by keyboard
            if text_rect.collidepoint(mouse_x, mouse_y):
                color = self.highlight_color
                hovered = i
            elif i == self.selected:
                color = self.highlight_color

            text_surf = self.option_font.render(opt, True, color)
            self.screen.blit(text_surf, text_rect)

        # Draw additional text if provided (works with newlines and tabs)
        if self.additional_text:
            lines = self.additional_text.split('\n')
            line_height = self.additional_font.get_height()
            total_text_height = len(lines) * line_height
            start_y = h - h // 6 - total_text_height // 2

            for idx, line in enumerate(lines):
                # Replace tabs with spaces for display
                text = line.replace('\t', '    ')
                add_surf = self.additional_font.render(text, True, self.text_color)
                add_rect = add_surf.get_rect(center=(w // 2, start_y + idx * line_height))
                self.screen.blit(add_surf, add_rect)
        pygame.display.flip()
        return hovered

    # Run the menu loop
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            hovered = self.draw()
            # For mouse hover, override selected with what the mouse is over
            if hovered is not None:
                self.selected = hovered
            # Handle events
            for event in pygame.event.get():
                # If window is closed
                if event.type == pygame.QUIT:
                    self.running = False
                    return None
                # If key is pressed
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        return self.selected
                # If mouse button is pressed
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # If mouse clicked a button
                    mouse_pos = event.pos
                    for i, rect in enumerate(self.button_rects):
                        if rect.collidepoint(mouse_pos):
                            self.selected = i
                            return self.selected
            clock.tick(30)