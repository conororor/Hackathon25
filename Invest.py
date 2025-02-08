import pygame

def wrap_text(text, font, max_width):
    words = text.split(" ")
    lines = []
    current_line = ""
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    
    if current_line:
        lines.append(current_line)
    
    return lines

def countryPurchaseMenu(country, country_cost, money):
    pygame.init()
    
    WIDTH, HEIGHT = 300, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Buy a Country")
    
    WHITE = (255, 255, 255)
    GRAY = (200, 200, 200)
    BLACK = (0, 0, 0)
    GREEN = (0, 200, 0)
    LIGHT_GREEN = (0, 255, 0)
    DARK_GREEN = (0, 150, 0)
    
    back_button = pygame.Rect(10, 10, 70, 35)
    buy_button = pygame.Rect(WIDTH // 2 - 65, 180, 130, 50)
    
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
        
        money_text = f"Money: ${money:.2f}"
        money_surface = large_font.render(money_text, True, BLACK)
        screen.blit(money_surface, (WIDTH // 2 - money_surface.get_width() // 2, 60))  # Adjusted y-coordinate
        
        prompt_text = f"Would you like to buy {country}?"
        prompt_lines = wrap_text(prompt_text, font, WIDTH - 20)
        for i, line in enumerate(prompt_lines):
            text_surface = font.render(line, True, BLACK)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, 100 + i * text_surface.get_height()))  # Adjusted y-coordinate
        
        buy_button_color = LIGHT_GREEN if buy_button.collidepoint(mouse_pos) else (GREEN if money >= country_cost else DARK_GREEN)
        pygame.draw.rect(screen, buy_button_color, buy_button)
        buy_text = f"Buy (${country_cost:.2f})"
        buy_surface = font.render(buy_text, True, BLACK)
        screen.blit(buy_surface, (buy_button.centerx - buy_surface.get_width() // 2, buy_button.centery - buy_surface.get_height() // 2))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_button.collidepoint(event.pos):
                    running = False
                    print("back")
                elif buy_button.collidepoint(event.pos) and money >= country_cost:
                    money -= country_cost  # Deduct cost
                    print(f"You bought {country}!")  # Placeholder action
                    running = False
        
        pygame.display.flip()
    
    pygame.quit()
    return money

# Example usage
money = 1000.00
money = countryPurchaseMenu("France", 500.00, money)