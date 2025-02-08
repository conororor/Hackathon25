import pygame
import sys

# Initialize Pygame
pygame.init()


# Screen resolution
res = (750, 450)
screen = pygame.display.set_mode(res)

# Load and scale the image
imp = pygame.image.load(r"C:\Users\Conor\Desktop\Hackathon25\Flag-map_of_the_People's_Republic_of_China.svg.png").convert_alpha()
imp = pygame.transform.scale(imp, (200, 200))

# Clock for frame rate control
clock = pygame.time.Clock()

# Score variable
score = 0
incre = 0.001
money = 100

# Image rectangle for positioning
imp_rect = imp.get_rect(topleft=(750-250, 450/3-50))

# If Mouse is hovering over image
mouse_hover = False

opacity = 255  # Full opacity (range: 0 to 255)
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        

        # Check for mouse click
        if event.type == pygame.MOUSEMOTION:
            mouse_hover = False
            mouse_pos = event.pos
            if imp_rect.collidepoint(mouse_pos):
                x, y = mouse_pos[0] - imp_rect.x, mouse_pos[1] - imp_rect.y
                while imp.get_at((x, y)).a > 0:
                    mouse_hover = imp_rect.collidepoint(event.pos)
                    break
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if click is within the image rectangle
            if imp_rect.collidepoint(mouse_pos):
                # Convert mouse coordinates relative to the image's top-left corner
                x, y = mouse_pos[0] - imp_rect.x, mouse_pos[1] - imp_rect.y

                # Get pixel color at (x, y) to check for transparency
                if imp.get_at((x, y)).a > 0:  # 'a' is the alpha channel
                    incre += 0.5
                    
    score += incre
    # Clear the screen
    opacity = 128 if mouse_hover else 255
    imp.set_alpha(opacity)
    screen.fill("lightblue")

    # Display the image
    screen.blit(imp, imp_rect.topleft)

    # Render and display the score
    font = pygame.font.Font(None, 36)
    scoreText = font.render(f"Score: {round(score,2)}", True, "white")
    moneyText = font.render(f"Money: {round(money,2)}", True, "white")
    screen.blit(scoreText, (10, 10))
    screen.blit(moneyText, (10, 35))

    # Update the display
    pygame.display.update()
    clock.tick(10)
