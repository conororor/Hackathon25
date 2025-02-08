import pygame
import math

# Initialize pygame
pygame.init()

def wrap_text(text, font, max_width):
    """
    Wraps the text to fit within the specified width.
    """
    words = text.split(" ")
    lines = []
    current_line = ""
    
    for word in words:
        # Check if the current line plus the next word would overflow
        test_line = current_line + ((" " if current_line else "") + word)
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word  # Start a new line with the current word
    
    # Append the last line
    if current_line:
        lines.append(current_line)
    
    return lines

def upgradeScreen(country_Multiplier):
    # Screen settings
    WIDTH, HEIGHT = 300, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Upgrade Country")

    # Colors
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    LIGHT_GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    RED = (200, 0, 0)
    LIGHT_RED = (255, 0, 0)
    DARK_RED = (150, 0, 0)

    # Scenario
    Scenario = "You have the opportunity to plant trees in a forest. How many trees will you plant?" #placeholder
    smallOption = "Plant 1 tree" #placeholder
    bigOption = "Plant 5 trees" #placeholder

    # Player stats
    player_money = 1000.00
    small_upgrade_cost = 10.00
    big_upgrade_cost = 30.00

    # Button settings
    back_button = pygame.Rect(10, 10, 70, 35)
    small_upgrade_button = pygame.Rect(15, 140, 130, 90)
    big_upgrade_button = pygame.Rect(155, 140, 130, 90)

    # Fonts
    font = pygame.font.Font(None, 20)
    large_font = pygame.font.Font(None, 25)  # Larger font for the money text

    # Main loop
    running = True
    while running:
        screen.fill(WHITE)
        
        mouse_pos = pygame.mouse.get_pos()

        # Draw back button
        pygame.draw.rect(screen, GRAY, back_button)
        back_lines = wrap_text("Back", font, back_button.width)
        for i, line in enumerate(back_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (back_button.centerx - text_surface.get_width() // 2, back_button.centery - len(back_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        # Draw player money at the top center
        money_lines = wrap_text(f"Money: ${player_money:.2f}", large_font, WIDTH - 20)
        for i, line in enumerate(money_lines):
            text_surface = large_font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 30 + i * text_surface.get_height()))  # Adjusted position

        
        # Draw scenario text
        scenario_lines = wrap_text(Scenario, font, WIDTH - 20)
        for i, line in enumerate(scenario_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 60 + i * text_surface.get_height()))  
        
        # Draw small upgrade button with solution
        small_button_color = LIGHT_GREEN if small_upgrade_button.collidepoint(mouse_pos) else (GREEN if player_money >= small_upgrade_cost else DARK_GREEN)
        pygame.draw.rect(screen, small_button_color, small_upgrade_button)
        small_upgrade_lines = wrap_text(f"$ {small_upgrade_cost:.2f}", font, small_upgrade_button.width)
        for i, line in enumerate(small_upgrade_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (small_upgrade_button.centerx - text_surface.get_width() // 2, small_upgrade_button.top + (small_upgrade_button.height // 4) - len(small_upgrade_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        small_option_lines = wrap_text(smallOption, font, small_upgrade_button.width)
        for i, line in enumerate(small_option_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (small_upgrade_button.centerx - text_surface.get_width() // 2, small_upgrade_button.bottom - (small_upgrade_button.height // 4) - len(small_option_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        # Draw big upgrade button with solution
        big_button_color = LIGHT_RED if big_upgrade_button.collidepoint(mouse_pos) else (RED if player_money >= big_upgrade_cost else DARK_RED)
        pygame.draw.rect(screen, big_button_color, big_upgrade_button)
        big_upgrade_lines = wrap_text(f"$ {big_upgrade_cost:.2f}", font, big_upgrade_button.width)
        for i, line in enumerate(big_upgrade_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (big_upgrade_button.centerx - text_surface.get_width() // 2, big_upgrade_button.top + (big_upgrade_button.height // 4) - len(big_upgrade_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        big_option_lines = wrap_text(bigOption, font, big_upgrade_button.width)
        for i, line in enumerate(big_option_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (big_upgrade_button.centerx - text_surface.get_width() // 2, big_upgrade_button.bottom - (big_upgrade_button.height // 4) - len(big_option_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        # Decision text at the bottom
        decision_lines = wrap_text("What will you decide?", font, WIDTH - 20)
        for i, line in enumerate(decision_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 250 + i * text_surface.get_height()))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                
                if back_button.collidepoint(mouse_pos):
                    running = False  # Simulates going back
                elif small_upgrade_button.collidepoint(mouse_pos) and player_money >= small_upgrade_cost:
                    player_money = round(player_money - small_upgrade_cost, 2)
                    small_upgrade_cost = round(small_upgrade_cost * country_Multiplier, 2) # Increase cost
                elif big_upgrade_button.collidepoint(mouse_pos) and player_money >= big_upgrade_cost:
                    player_money = round(player_money - big_upgrade_cost, 2)
                    big_upgrade_cost = round(big_upgrade_cost * country_Multiplier, 2)  # Increase cost more drastically
        
        pygame.display.flip()

    pygame.quit()

upgradeScreen(1.5)
