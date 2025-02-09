import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen resolution
res = (1200, 750)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Game Menu")

# Load the main menu image and hover images
menu_image = pygame.image.load("images/MainMenuImage.png").convert()
menu_image = pygame.transform.scale(menu_image, res)
GameStart = pygame.image.load("images/GameStartHover.png").convert_alpha()
Help = pygame.image.load("images/HelpHover.png").convert_alpha()
Quit = pygame.image.load("images/QuitHover.png").convert_alpha()

# Create button rectangles
start_button = GameStart.get_rect(center=(600, 330))  # Centered at (600, 300)
help_button = Help.get_rect(center=(600, 500))  # Below start
quit_button = Quit.get_rect(center=(600, 660))  # Below help

def StartMenu():
    while True:
        screen.blit(menu_image, (0, 0))
        mouse_pos = pygame.mouse.get_pos()

        # Check if mouse is hovering over buttons
        start_hover = start_button.collidepoint(mouse_pos)
        help_hover = help_button.collidepoint(mouse_pos)
        quit_hover = quit_button.collidepoint(mouse_pos)

        # Draw buttons only if hovering
        if start_hover:
            screen.blit(GameStart, start_button.topleft)
        if help_hover:
            screen.blit(Help, help_button.topleft)
        if quit_hover:
            screen.blit(Quit, quit_button.topleft)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_hover:
                    print("Start Game")  # Replace with your game function
                    return
                if help_hover:
                    print("Help Menu")  # Replace with a help screen function
                    HelpMenu()
                if quit_hover:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def HelpMenu():
    while True:
        screen.fill((211, 211, 211))  # Light grey background

        font = pygame.font.Font(None, 36)

        # Title Text
        title_text = font.render("Help Menu", True, (0, 0, 0))  # Black text
        screen.blit(title_text, (500, 100))

        # Customizable Instructions Text
        instructions_text = font.render("This is your help screen.", True, (0, 0, 0))  # Black text
        instructions_text2 = font.render("You can change this text to explain the game.", True, (0, 0, 0))
        instructions_text3 = font.render("Click 'Back' to return to the main menu.", True, (0, 0, 0))

        # Render instructions
        screen.blit(instructions_text, (200, 200))
        screen.blit(instructions_text2, (200, 250))
        screen.blit(instructions_text3, (200, 300))

        # Back Button
        back_button = pygame.Rect(10, 10, 150, 50)  # Back button rectangle at the top-left corner
        pygame.draw.rect(screen, (0, 255, 0), back_button)  # Green button
        back_text = font.render("Back", True, (0, 0, 0))  # Black text
        screen.blit(back_text, (40, 20))  # Positioning the text on the button

        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(mouse_pos):
                    return  # Return to the main menu

        pygame.display.update()

# Start the menu
StartMenu()



class Country:
    def __init__(self,url,scale,pos,badInc,goodInc,cost):
        self.url = url
        self.scale = scale
        self.pos = pos
        self.badInc = badInc
        self.goodInc = goodInc
        self.cost = cost
        self.image = pygame.image.load(url).convert_alpha()
        self.image = pygame.transform.scale(self.image,scale)
        self.rect = self.image.get_rect(topleft=pos)
        self.opacity = 255

badPol = 0
worldPol = 0
goodPol = 0
money = 100

# Clock for frame rate control
clock = pygame.time.Clock()

# If Mouse is hovering over image
mouse_hover = False
opa = 255
opacity = 255  # Full opacity (range: 0 to 255)

greenland = Country("images/Greenland.png",(165,165),(315,2),0.01,0,50)
iceland = Country("images/Iceland.png",(82,82),(460,90),0.01,0,50)
greatBritan = Country("images/GreatBritan.png",(115,115),(420,168),0.01,0,50)
alaska = Country("images/Alaska.png",(120,120),(5,62),0.01,0,50)
northWestTerritory = Country("images/NorthWestTerritory.png",(210,100),(98,45),0.01,0,50)
alberta = Country("images/Alberta.png",(110,90),(110,127),0.01,0,50)
quebec = Country("images/Quebec.png",(110,130),(277,127),0.01,0,50)
ontario = Country("images/Ontario.png",(110,100),(210,130),0.01,0,50)
westernUnitedStates = Country("images/WesternUnitedStates.png",(120,120),(117,207),0.01,0,50)
easternUnitedStates = Country("images/EasternUnitedStates.png",(153,164),(187,185),0.01,0,50)
centralAmerica = Country("images/CentralAmerica.png",(110,135),(125,290),0.01,0,50)
venezuela = Country("images/Venezuela.png",(150,80),(210,387),0.01,0,50)
brazil = Country("images/Brazil.png",(215,205),(233,410),0.01,0,50)
peru = Country("images/Peru.png",(150,175),(195,410),0.01,0,50)
argentina = Country("images/Argentina.png",(110,205),(252,530),0.01,0,50)

countries = [greenland,iceland,greatBritan,alaska,northWestTerritory,alberta,quebec,ontario,westernUnitedStates,easternUnitedStates,
             centralAmerica,venezuela,brazil,peru,argentina]
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, res)

while True:
    # Handle events
    mouse_hover = {country: False for country in countries}
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse click
        if event.type == pygame.MOUSEMOTION:
            for country in countries:
                mouse_hover[country] = False
                if country.rect.collidepoint(mouse_pos):
                    x, y = mouse_pos[0] - country.rect.x, mouse_pos[1] - country.rect.y
                    if country.image.get_at((x, y)).a > 0:
                        mouse_hover[country] = True
                    else:
                        country.opacity = 255
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if click is within the image rectangle
            for country in countries:
                if country.rect.collidepoint(mouse_pos):
                    x, y = mouse_pos[0] - country.rect.x, mouse_pos[1] - country.rect.y

                    # Get pixel color at (x, y) to check for transparency
                    if country.image.get_at((x, y)).a > 0:
                        country.opacity = 170
                        country.goodInc += 0.01
                        if country.badInc > 0:
                            country.badInc -= 0.005
    
    screen.fill("lightblue")
    background.set_alpha(125)
    screen.blit(background, (0, 0))

    for country in countries:
        badPol += country.badInc
        goodPol += country.goodInc
        country.opacity = 220 if mouse_hover[country] else country.opacity
        country.image.set_alpha(country.opacity)
        screen.blit(country.image,country.rect.topleft)

    font = pygame.font.Font(None, 36)
    goodText = font.render(f"Good Polution: {round(goodPol,2)}", True, "white")
    badText = font.render(f"Bad Polution: {round(badPol,2)}", True, "white")
    moneyText = font.render(f"Money: {round(money,2)}", True, "white")
    screen.blit(goodText, (10, 10))
    screen.blit(badText, (10, 35))
    screen.blit(moneyText, (10, 60))

    pygame.display.update()
    clock.tick(10)
