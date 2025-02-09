import pygame
import random

# Initialize pygame
pygame.init()

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + ((" " if current_line else "") + word)
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

def upgradeScreen(money,country_Multiplier,GoodIncline,BadIncline):
    WIDTH, HEIGHT = 300, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Upgrade Country")

    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLACK = (0, 0, 0)
    LIGHT_GRAY = (211, 211, 211)
    GREEN = (0, 255, 0)

    Scenario = "You have the opportunity to plant trees in a forest. How many trees will you plant?"
    smallOption = "Plant 1 tree"
    bigOption = "Plant 5 trees"
    smallPercentChange = random.randint(10, 20)  # as a percentage
    bigPercentChange = random.randint(30, 40)  # as a percentage
    smallPercentChangeM = smallPercentChange / 100  # as a percentage
    bigPercentChangeM = bigPercentChange / 100  # as a percentage


    small_upgrade_cost = 100.00
    big_upgrade_cost = 300.00

    back_button = pygame.Rect(10, 10, 70, 35)
    small_upgrade_button = pygame.Rect(15, 140, 130, 90)
    big_upgrade_button = pygame.Rect(155, 140, 130, 90)

    font = pygame.font.Font(None, 20)
    large_font = pygame.font.Font(None, 25)

    running = True
    while running:
        screen.fill(WHITE)
        
        mouse_pos = pygame.mouse.get_pos()

        pygame.draw.rect(screen, GRAY, back_button)
        back_lines = wrap_text("Back", font, back_button.width)
        for i, line in enumerate(back_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (back_button.centerx - text_surface.get_width() // 2, back_button.centery - len(back_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        money_lines = wrap_text(f"Money: ${money:.2f}", large_font, WIDTH - 20)
        for i, line in enumerate(money_lines):
            text_surface = large_font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 30 + i * text_surface.get_height()))

        scenario_lines = wrap_text(Scenario, font, WIDTH - 20)
        for i, line in enumerate(scenario_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 60 + i * text_surface.get_height()))
        
        small_button_outline_color = GREEN if small_upgrade_button.collidepoint(mouse_pos) else BLACK
        pygame.draw.rect(screen, LIGHT_GRAY, small_upgrade_button)
        pygame.draw.rect(screen, small_button_outline_color, small_upgrade_button, 4)  # Thicker outline
        small_upgrade_lines = wrap_text(f"$ {small_upgrade_cost:.2f}", font, small_upgrade_button.width)
        for i, line in enumerate(small_upgrade_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (small_upgrade_button.centerx - text_surface.get_width() // 2, small_upgrade_button.top + (small_upgrade_button.height // 4) - len(small_upgrade_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        small_percent_text = f"-{smallPercentChange}%"
        small_percent_lines = wrap_text(small_percent_text, font, small_upgrade_button.width)
        for i, line in enumerate(small_percent_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (small_upgrade_button.centerx - text_surface.get_width() // 2, small_upgrade_button.centery - len(small_percent_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        small_option_lines = wrap_text(smallOption, font, small_upgrade_button.width)
        for i, line in enumerate(small_option_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (small_upgrade_button.centerx - text_surface.get_width() // 2, small_upgrade_button.bottom - (small_upgrade_button.height // 4) - len(small_option_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        big_button_outline_color = GREEN if big_upgrade_button.collidepoint(mouse_pos) else BLACK
        pygame.draw.rect(screen, LIGHT_GRAY, big_upgrade_button)
        pygame.draw.rect(screen, big_button_outline_color, big_upgrade_button, 4)  # Thicker outline
        big_upgrade_lines = wrap_text(f"$ {big_upgrade_cost:.2f}", font, big_upgrade_button.width)
        for i, line in enumerate(big_upgrade_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (big_upgrade_button.centerx - text_surface.get_width() // 2, big_upgrade_button.top + (big_upgrade_button.height // 4) - len(big_upgrade_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        big_percent_text = f"-{bigPercentChange}%"
        big_percent_lines = wrap_text(big_percent_text, font, big_upgrade_button.width)
        for i, line in enumerate(big_percent_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (big_upgrade_button.centerx - text_surface.get_width() // 2, big_upgrade_button.centery - len(big_percent_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        big_option_lines = wrap_text(bigOption, font, big_upgrade_button.width)
        for i, line in enumerate(big_option_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (big_upgrade_button.centerx - text_surface.get_width() // 2, big_upgrade_button.bottom - (big_upgrade_button.height // 4) - len(big_option_lines) * text_surface.get_height() // 2 + i * text_surface.get_height()))
        
        decision_lines = wrap_text("What will you decide?", font, WIDTH - 20)
        for i, line in enumerate(decision_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 250 + i * text_surface.get_height()))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos

                if GoodIncline >= 2:
                    GoodIncline = 2
                    BadIncline = 0
                    break                    
                
                
                if back_button.collidepoint(mouse_pos):
                    print(money,GoodIncline,BadIncline)
                    return money,GoodIncline,BadIncline
                
                elif small_upgrade_button.collidepoint(mouse_pos) and money >= small_upgrade_cost:
                    money = round(money - small_upgrade_cost, 2)
                    small_upgrade_cost = round(small_upgrade_cost * country_Multiplier, 2)
                    GoodIncline = round(GoodIncline +  smallPercentChangeM,2)
                    BadIncline = round(BadIncline -  smallPercentChangeM,2)

                elif big_upgrade_button.collidepoint(mouse_pos) and money >= big_upgrade_cost:
                    money = round(money - big_upgrade_cost, 2)
                    big_upgrade_cost = round(big_upgrade_cost * country_Multiplier, 2)
                    GoodIncline = round(GoodIncline + bigPercentChangeM,2)
                    BadIncline = round(BadIncline - bigPercentChangeM,2)
        
        pygame.display.flip()

    pygame.quit()

upgradeScreen(1000,1.5,1,1) # Example of how to call the function using 1000 money, cost multpiler of 1.5, and good and bad incline of 1