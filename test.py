import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen resolution
res = (1500, 900)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Interactive Map")

# Load and scale the background image
background = pygame.image.load("map.png").convert()
background = pygame.transform.scale(background, res)

# Define individual country regions (Polygon objects)
countries = {
    "Alaska": [(50, 100), (200, 120), (180, 200), (60, 180)],
    "Greenland": [(600, 50), (800, 50), (850, 150), (620, 180)],
    "Quebec": [(500, 250), (620, 260), (580, 350), (480, 320)],
    "Western US": [(200, 300), (400, 320), (380, 450), (220, 420)],
    "Eastern US": [(400, 300), (550, 320), (520, 450), (380, 420)],
    "Ontario": [(450, 200), (600, 220), (580, 280), (460, 260)],
    "Mexico": [(200, 500), (350, 520), (330, 650), (210, 630)],
    "Brazil": [(500, 600), (700, 620), (680, 800), (520, 780)],
    "Argentina": [(600, 800), (750, 820), (730, 900), (620, 880)],
    "UK": [(850, 250), (900, 230), (920, 270), (870, 280)],
    "France": [(900, 300), (970, 320), (940, 380), (880, 360)],
    "Germany": [(950, 270), (1020, 290), (990, 350), (930, 330)],
    "Russia": [(1100, 100), (1450, 120), (1400, 400), (1100, 350)],
    "China": [(1200, 200), (1350, 220), (1300, 400), (1150, 380)],
    "India": [(1100, 450), (1200, 470), (1150, 600), (1050, 580)],
    "South Africa": [(900, 750), (1000, 770), (970, 850), (880, 830)],
    "Australia": [(1200, 700), (1450, 720), (1400, 850), (1250, 830)],
}

# Colors
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

# Game loop
running = True
selected_country = None
while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    
    mouse_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for country, polygon in countries.items():
                if pygame.draw.polygon(screen, (0, 0, 0), polygon, 0).collidepoint(mouse_pos):
                    selected_country = country
                    print(f"Clicked on {country}")
    
    # Draw country highlights
    for country, polygon in countries.items():
        if pygame.draw.polygon(screen, (0, 0, 0), polygon, 0).collidepoint(mouse_pos):
            pygame.draw.polygon(screen, YELLOW, polygon, 3)
    
    pygame.display.update()
    
pygame.quit()
sys.exit()
