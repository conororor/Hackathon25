import pygame
import sys
import numpy as np
from upgrades import upgradeScreen

# Initialize Pygame
pygame.init()

res = (1200, 750)
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Game Menu")
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
        instructions_text = font.render("In this simulation/game you are tasked with expanding your Renewable energy plants ", True, (0, 0, 0))  # Black text
        instructions_text2 = font.render("across the world.", True, (0, 0, 0))
        instructions_text3 = font.render("", True, (0, 0, 0))
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
    def __init__(self, url, scale, pos, badInc, goodInc, cost):
        self.url = url
        self.scale = scale
        self.pos = pos
        self.badInc = badInc
        self.goodInc = goodInc
        self.cost = cost
        self.image = pygame.image.load(url).convert_alpha()
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(topleft=pos)
        self.opacity = 255
        self.original_image = self.image.copy()  # Keep a copy to restore pixel colors

    def adjust_green_intensity(self):
        """
        Adjust the green intensity of the image based on badInc.
        Higher badInc will reduce the green component, simulating pollution.
        Restore the original image if badInc is zero.
        """
        self.image = self.original_image.copy()  # Reset to the original image first

        if self.badInc > 0:
            pixel_array = pygame.surfarray.pixels3d(self.image)
            adjustment_factor = max(1 - self.badInc, 0)  # Ensure the factor is within [0, 1]
            pixel_array[..., 1] = (pixel_array[..., 1] * adjustment_factor).astype(np.uint8)
            del pixel_array  # Release pixel array lock

# Screen resolution


badPol = 0
worldPol = 0
goodPol = 0
money = 0

# Clock for frame rate control
clock = pygame.time.Clock()


# If Mouse is hovering over image
mouse_hover = False
opa = 255
opacity = 255  # Full opacity (range: 0 to 255)

#Values of Positive and negative carbon emissions taken from real world data
greenland = Country("images/Greenland.png",(165,165),(315,2),0.1,0.9,50)
iceland = Country("images/IceLand.png",(82,82),(460,90),0.1,0.9,50)
greatBritan = Country("images/GreatBritan.png",(115,115),(420,168),0.6,0.4,50)
alaska = Country("images/Alaska.png",(120,120),(5,62),0.3,0.7,50)
northWestTerritory = Country("images/NorthWestTerritory.png",(210,100),(98,45),0.3,0.7,50)
alberta = Country("images/Alberta.png",(110,90),(110,127),0.85,0.15,50)
quebec = Country("images/Quebec.png",(110,130),(277,127),0.05,0.95,50)
ontario = Country("images/Ontario.png",(110,100),(210,130),0.7,0.3,50)
westernUnitedStates = Country("images/WesternUnitedStates.png",(120,120),(117,207),0.6,0.4,50)
easternUnitedStates = Country("images/EasternUnitedStates.png",(153,164),(187,185),0.5,0.5,50)
centralAmerica = Country("images/CentralAmerica.png",(110,135),(125,290),0.75,0.25,50)
venezuela = Country("images/Venezuela.png",(150,80),(210,387),0.70,0.3,50)
brazil = Country("images/Brazil.png",(215,205),(233,410),0.2,0.8,50)
peru = Country("images/Peru.png",(150,175),(195,410),0.6,0.4,50)
argentina = Country("images/Argentina.png",(110,205),(252,530),0.35,0.65,50)
indonesia = Country("images/Indonesia.png",(135,110),(922,495),0.15,0.85,50)
newGuinea = Country("images/NewGuinea.png",(110,80),(1042,480),0.8,0.2,50)
westernAustralia = Country("images/WesternAustralia.png",(150,145),(980,578),0.4,0.6,50)
easternAustralia = Country("images/EasternAustralia.png",(128,169),(1067,568),0.5,0.5,50)
madagascar = Country("images/Madagascar.png",(80,110),(725,610),0.6,0.4,50)
japan = Country("images/Japan.png",(85,138),(1058,190),0.75,0.25,50)
northAfrica = Country("images/NorthAfrica.png",(185,185),(464,375),0.1,0.9,50)
egypt = Country("images/Egypt.png",(117,78),(587,397),0.15,0.85,50)
congo = Country("images/Congo.png",(120,120),(580,504),0.8,0.2,50)
eastAfrica = Country("images/EastAfrica.png",(140,185),(635,455),0.7,0.3,50)
southAfrica = Country("images/SouthAfrica.png",(134,157),(590,575),0.8,0.2,50)
westernEurope = Country("images/WesternEurope.png",(110,128),(450,265),0.35,0.65,50)
southernEurope = Country("images/SouthernEurope.png",(113,120),(545,260),0.35,0.65,50)
northernEurope = Country("images/NorthernEurope.png",(116,110),(532,187),0.80,0.2,50)
scandonavia = Country("images/Scandonavia.png",(111,122),(550,79),0.1,0.9,50)
middleEast = Country("images/MiddleEast.png",(195,175),(630,320),0.8,0.2,50)
ukraine = Country("images/Ukraine.png",(185,250),(620,85),0.5,0.5,50)
siam = Country("images/Siam.png",(100,120),(925,372),0.6,0.4,50)
india = Country("images/India.png",(150,190),(800,314),0.7,0.3,50)
afganistan = Country("images/Afganistan.png",(140,145),(733,200),0.8,0.2,50)
mongolia = Country("images/Mongolia.png",(154,120),(915,187),0.9,0.1,50)
china = Country("images/China.png",(210,173),(845,233),0.9,0.1,50)
russia = Country("images/Russia.png",(390,280),(785,17),0.7,0.3,50)



countries = [greenland,iceland,greatBritan,alaska,northWestTerritory,alberta,quebec,ontario,westernUnitedStates,easternUnitedStates,
             centralAmerica,venezuela,brazil,peru,argentina,indonesia,newGuinea,westernAustralia,easternAustralia,madagascar,
             japan,northAfrica,egypt,congo,eastAfrica,southAfrica,westernEurope,southernEurope,northernEurope,scandonavia,middleEast,
             ukraine,siam,india,afganistan,mongolia,china,russia]
background = pygame.image.load("images/background.png").convert()
background = pygame.transform.scale(background, res)

while True:
    # Handle events
    mouse_hover = {country: False for country in countries}
    mouse_pos = pygame.mouse.get_pos()
    font = pygame.font.Font(None, 36)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for mouse hover
        if event.type == pygame.MOUSEMOTION:
            for country in countries:
                if country.rect.collidepoint(mouse_pos):
                    x, y = mouse_pos[0] - country.rect.x, mouse_pos[1] - country.rect.y
                    if country.image.get_at((x, y)).a > 0:
                        mouse_hover[country] = True
                    else:
                        mouse_hover[country] = False
                country.opacity = 255
                
        # Handle country clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            for country in countries:
                if country.rect.collidepoint(mouse_pos):
                    x, y = mouse_pos[0] - country.rect.x, mouse_pos[1] - country.rect.y

                    if country.image.get_at((x, y)).a > 0:  # Ensure click is on visible part
                        country.opacity = 170

                        # OPEN UPGRADE MENU
                        new_money, new_goodInc, new_badInc = upgradeScreen(
                            money, 1.5, country.goodInc, country.badInc
                        )

                        # APPLY THE UPGRADE EFFECTS
                        if new_money is not None:
                            money = new_money  # Update global money
                        if new_goodInc is not None:
                            country.goodInc = new_goodInc  # Apply new good pollution
                        if new_badInc is not None:
                            country.badInc = new_badInc  # Apply new bad pollution

                        # Ensure pollution values remain within limits
                        country.badInc = max(0, country.badInc)  # No negative pollution
                        country.goodInc = min(2, country.goodInc)  # Capped at 2

                        # EXISTING FUNCTIONALITY: Pollution improvement on click
                        country.goodInc += 0.0002
                        if country.badInc > 0:
                            country.badInc -= 0.05

                        res = (1200, 750)
                        screen = pygame.display.set_mode(res)
        
    screen.fill("lightblue")
    background.set_alpha(150)
    screen.blit(background, (0, 0))
    
    for country in countries:
        money += country.goodInc*0.01
        badPol += country.badInc
        goodPol += country.goodInc
        country.adjust_green_intensity()
        country.opacity = 150 if mouse_hover[country] else country.opacity
        country.image.set_alpha(country.opacity)
        screen.blit(country.image,country.rect.topleft)
        if mouse_hover[country]:
            if country.goodInc > 0:  # Avoid division by zero
                ratio = (country.badInc / country.goodInc) * 100
                hover_text = font.render(f"Good Polution: {country.goodInc*100}", True, "white")
                hover_text2 = font.render(f"Bad Pollution {country.badInc*100}", True, "white")

                screen.blit(hover_text, (10,680))
                screen.blit(hover_text2, (10,700))

    # Render and display the score
    goodText = font.render(f"Good Polution: {round(goodPol,2)}", True, "white")
    badText = font.render(f"Bad Polution: {round(badPol,2)}", True, "white")
    moneyText = font.render(f"Money : £{round(money,2)}", True, "white")
    
    screen.blit(goodText, (10, 10))
    screen.blit(badText, (10, 35))
    screen.blit(moneyText, (10, 60))

    # Update the display
    pygame.display.update()
    clock.tick(15)