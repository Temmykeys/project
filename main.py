import random

import pygame

pygame.init()
BROWN = (139, 69, 19)
PURPLE = (188, 81, 235)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 240)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PI = 3.141592653
size = (700, 600)
button_WIDTH = 250
button_height = 45
button_colour = BLUE
text_colour = BLACK
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
pygame.init()
button_font = pygame.font.SysFont('Calibri', 40, True, False)
pygame.display.set_caption("Computing Project")
X_pos = 250
done = False


class Main_screen:
    def __init__(self):
        pass

    def draw(self, screen):
        screen.fill(GREEN)
        Play_button = button_font.render('Play Game', True, BLACK)
        pygame.draw.rect(screen, BLUE, [X_pos, 90, button_WIDTH, button_height])
        screen.blit(Play_button, [X_pos + 5, 95])

        High_scores_button = button_font.render('High Scores', True, BLACK)
        pygame.draw.rect(screen, BLUE, [X_pos, 240, button_WIDTH, button_height])
        screen.blit(High_scores_button, [X_pos + 5, 245])

        Help_button = button_font.render('Help', True, BLACK)
        pygame.draw.rect(screen, BLUE, [X_pos, 390, button_WIDTH, button_height])
        screen.blit(Help_button, [X_pos + 5, 395])

        Exit_button = button_font.render('Exit', True, BLACK)
        pygame.draw.rect(screen, BLUE, [X_pos, 440, button_WIDTH, button_height])
        screen.blit(Exit_button, [X_pos + 5, 445])


    def screenevent(self, action):
        if action.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if X_pos < x < X_pos + button_WIDTH:
                if 90 < y < 125:
                    return "play"
                elif 240 < y < 275:
                    return "high scores"
                elif 390 < y < 425:
                    return "help"
                elif 440 < y < 475:
                    return "exit"

    def update(self):
        pass

class Help_screen:
    def __init__(self):
        pass


    def draw(self, screen):
        screen.fill(RED)
        Instruction1 = button_font.render('''Move your way around obstacles''', True, BLACK)
        screen.blit(Instruction1, [100, 90])
        Instruction2 = button_font.render('''make use of the arrow keys''', True, BLACK)
        screen.blit(Instruction2, [100, 130])
        Instruction3 = button_font.render('''try not to die''', True, BLACK)
        screen.blit(Instruction3, [100, 170])

        Back_button = button_font.render('Back', True, BLACK)
        pygame.draw.rect(screen, BLUE, [X_pos, 440, button_WIDTH, button_height])
        screen.blit(Back_button, [X_pos + 5, 445])

    def screenevent(self, action):
        if action.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if X_pos < x < X_pos + button_WIDTH:
                if 440 < y < 475:
                    return "menu"

    def update(self):
        pass

class Game_screen:
    def __init__(self):
        self.ground_pos = 700
        self.game_start = self.ground_pos - 700
        self.mountain_height = random.randint(150, 300)
        self.mountain_width = random.randint(200, 350)
        self.moving = False

        self.x = 200
        self.y = 200
        self.scale = 3
        self.character = pygame.image.load('character.png')
        self.character = pygame.transform.scale(self.character, (int(self.character.get_width() * self.scale), int(self.character.get_height() * self.scale)))
        self.boundary = self.character.get_rect()
        self.boundary.centre = (self.x, self.y)




    def draw(self, screen):
        screen.fill(BLACK)
        Back_button = button_font.render('Back', True, WHITE)
        pygame.draw.rect(screen, BLUE, [X_pos-250, 2, button_WIDTH - 150, button_height])
        screen.blit(Back_button, [X_pos-250 + 5, 7])

        pygame.draw.rect(screen, GREEN, [self.game_start, 530, 550, 70])
        pygame.draw.rect(screen, BROWN, [self.ground_pos - 150, 350, 350, 250])

        screen.blit(self.character, self.boundary)





    def screenevent(self, action):
        if action.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if X_pos - 250 < x < X_pos - 250 + button_WIDTH - 150:
                if 2 < y < 47:
                    return "menu"
        elif action.type == pygame.KEYUP:
            if action.key == pygame.K_d:
                self.ground_pos -= 5
                if self.ground_pos <= 450:
                    pygame.draw.rect(screen, BROWN, [self.ground_pos, 600 - self.mountain_height, self.mountain_width, self.mountain_height])
            elif action.key == pygame.K_a:
                if self.game_start <= 0:
                    self.ground_pos += 5





    def update(self):
        pygame.display.update()



class High_scores:
    def __init__(self):
        pass

    def screenevent(self, action):
        pass

    def draw(self, screen):
        pass

    def update(self):
        pass

class Game_over:
    def __init__(self):
        pass

    def draw(self, screen):
        message = button_font.render('''Game Over, Click anywhere on screen to continue''', True, BLACK)
        screen.blit(message, [150, 90])

    def screenevent(self, action):
        if action.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 0 < x < size[0] and 0 < y < size[1]:
                return "menu"
    def update(self):
        pass

window = Main_screen()
# -------- Main Program Loop -----------
while not done:
    # If the user clicks the X button on the top tight hand side of the GUI, the GUI closes.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        else:
            call = window.screenevent(event)
            if call == "help":
                window = Help_screen()
            elif call == "play":
                window = Game_screen()
            elif call == "game over":
                window = Game_over()
            elif call == "high scores":
                window = High_scores()
            elif call == "exit":
                done = True
            elif call == "menu":
                window = Main_screen()
    window.update()
    window.draw(screen)

    # This command updates the screen with what we'll draw.
    pygame.display.flip()

    # Limits the frame per second at a smooth 120.
    clock.tick(150)

# Closes the window and quit.
pygame.quit()
