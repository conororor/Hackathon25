import pygame
import sys

# Initialize Pygame
pygame.init()

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

# Screen resolution
res = (1200, 750)
screen = pygame.display.set_mode(res)

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
iceland = Country("images/IceLand.png",(82,82),(460,90),0.01,0,50)
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
                    # Convert mouse coordinates relative to the image's top-left corner
                    x, y = mouse_pos[0] - country.rect.x, mouse_pos[1] - country.rect.y

                    # Get pixel color at (x, y) to check for transparency
                    if country.image.get_at((x, y)).a > 0:  # 'a' is the alpha channel
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

    # Render and display the score
    font = pygame.font.Font(None, 36)
    goodText = font.render(f"Good Polution: {round(goodPol,2)}", True, "white")
    badText = font.render(f"Bad Polution: {round(badPol,2)}", True, "white")
    moneyText = font.render(f"Money: {round(money,2)}", True, "white")
    screen.blit(goodText, (10, 10))
    screen.blit(badText, (10, 35))
    screen.blit(moneyText, (10, 60))

    # Update the display
    pygame.display.update()
    clock.tick(10)