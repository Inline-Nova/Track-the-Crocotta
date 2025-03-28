import pygame
import sys
import random

# Initialize Pygame
pygame.init()

#Functions:

def isSafe():
    global posx,posy
    
    adjacent_positions = [
        [posx - 1, posy],  # Up
        [posx + 1, posy],  # Down
        [posx, posy - 1],  # Left
        [posx, posy + 1]   # Right
    ]
    
    for pos in adjacent_positions:
        x, y = pos
        
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            
            if pos == corcotta_pos:
                return False
                # print("cor")
            if pos in pits_pos:
                return False
                # print("pit")
    return True

def isPlayerAdjacent():
    global isNearCorcotta, isNearPit
    isNearCorcotta = False
    isNearPit = False
    
    adjacent_positions = [
        [player_pos[0] - 1, player_pos[1]],  # Up
        [player_pos[0] + 1, player_pos[1]],  # Down
        [player_pos[0], player_pos[1] - 1],  # Left
        [player_pos[0], player_pos[1] + 1]   # Right
    ]
    
    for pos in adjacent_positions:
        x, y = pos
        
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            
            if pos == corcotta_pos:
                isNearCorcotta = True
                # print("cor")
            if pos in pits_pos:
                isNearPit = True
                # print("pit")
        
def displayResult():
    global result_str
    if(isNearPit and isNearCorcotta):
        result_str = "\"I hear panting and I feel a breeze\""
    elif(isNearPit):
        result_str = "\"I feel a breeze\""
    elif(isNearCorcotta):
        result_str = "\"I hear panting\""
    else:
        result_str = "\"Silence\""

def isPlayerDead():
    global player_pos
    global game_over_str
    if(player_pos[0] == corcotta_pos[0] and player_pos[1] == corcotta_pos[1]):
        game_over_str = "The Corcotta caught you"
    else:
        for pit in pits_pos:
            if(player_pos[0] == pit[0] and player_pos[1] == pit[1]):
                game_over_str = "You fell in a pit"

def reset_game():
    global player_pos, occupied, pits_pos, corcotta_pos, game_over_str, posx,posy,fire_mode, arrows
    
    # Reset firing
    fire_mode = False
    
    # Reset game_over_str
    game_over_str = "alive"
    displayInfo = False

    # Reset occupied positions
    occupied = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    #reset arrows
    arrows = 2


    # Reset pits
    pits_pos = [[0, 0] for _ in range(3)]
    for p in range(3):
        posx, posy = random.randint(0, 4), random.randint(0, 4)
        while occupied[posx][posy]:
            posx, posy = random.randint(0, 4), random.randint(0, 4)
        pits_pos[p] = [posx, posy]
        occupied[posx][posy] = True

    # Reset Corcotta position
    posx, posy = random.randint(0, 4), random.randint(0, 4)
    while occupied[posx][posy]:
        posx, posy = random.randint(0, 4), random.randint(0, 4)
    corcotta_pos = [posx, posy]
    occupied[posx][posy] = True
    
    # player place
    posx = random.randint(0,4)
    posy = random.randint(0,4)

    while(occupied[posx][posy] or not isSafe()):
        posx = random.randint(0,4)
        posy = random.randint(0,4)
    player_pos = [posx, posy] # Starting random
    occupied[posx][posy] = True
    print("player: [" + str(posx) + ", " + str(posy) + "]")

def fireAtCorcotta(dir):
    global arrows
    global game_over_str
    global occupied
    global corcotta_pos
    global posx,posy
    
    if(dir == 0): #up
        if(player_pos[1] > 0 and corcotta_pos[0] == player_pos[0] and corcotta_pos[1] == player_pos[1]-1):
            game_over_str = "You caught the Crocotta!"
        else:
            arrows -= 1
            while(occupied[posx][posy] == True):
                posx = random.randint(0,4)
                posy = random.randint(0,4)
            occupied[corcotta_pos[0]][corcotta_pos[1]] = False
            corcotta_pos = [posx,posy]
            occupied[posx][posy] = True
    elif(dir == 1): #right
        if(player_pos[0] < GRID_SIZE and corcotta_pos[0] == player_pos[0]+1 and corcotta_pos[1] == player_pos[1]):
            game_over_str = "You caught the Crocotta!"
        else:
            arrows -= 1
            while(occupied[posx][posy] == True):
                posx = random.randint(0,4)
                posy = random.randint(0,4)
            occupied[corcotta_pos[0]][corcotta_pos[1]] = False
            corcotta_pos = [posx,posy]
            occupied[posx][posy] = True
    elif(dir == 2): #down
        if(player_pos[1] < GRID_SIZE and corcotta_pos[0] == player_pos[0] and corcotta_pos[1] == player_pos[1]+1):
            game_over_str = "You caught the Crocotta!"
        else:
            arrows -= 1
            while(occupied[posx][posy] == True):
                posx = random.randint(0,4)
                posy = random.randint(0,4)
            occupied[corcotta_pos[0]][corcotta_pos[1]] = False
            corcotta_pos = [posx,posy]
            occupied[posx][posy] = True
    elif(dir == 3): #left
        if(player_pos[0] > 0 and corcotta_pos[0] == player_pos[0]-1 and corcotta_pos[1] == player_pos[1]):
            game_over_str = "You caught the Crocotta!"
        else:
            arrows -= 1
            while(occupied[posx][posy] == True):
                posx = random.randint(0,4)
                posy = random.randint(0,4)
            occupied[corcotta_pos[0]][corcotta_pos[1]] = False
            corcotta_pos = [posx,posy]
            occupied[posx][posy] = True
    else:
        arrows -= 1
        
        
    if arrows == 0:
        game_over_str = "Your ran out of arrows"
    




# Constants
GRID_SIZE = 5
CELL_SIZE = 80
WIDTH = 500
HEIGHT = 600
SQUARE_COLOR = (255, 0, 0)

# For Board
BACKGROUND_COLOR = (255, 255, 255)
RECT_COLOR = (217, 217, 217)
SHADOW_COLOR = (170,170,170)
shadow_offset = 0


TEXT_COLOR = (0,0,0)
START_X = 50
START_Y = 67
STAR = pygame.image.load('images/game_star.png')
STAR = pygame.transform.scale(STAR, (CELL_SIZE, CELL_SIZE))

game_over_str = "alive"
displayInfo = False

#For knowing what near
isNearCorcotta = False
isNearPit = False
result_str = "\"Silence\""

# For Title Font
font_path = 'Just_Me_Again_Down_Here/JustMeAgainDownHere-Regular.ttf'
pygame.font.init()
font = pygame.font.Font(font_path, 40)

# For Other Font
other_font_path = 'Inter/Inter-VariableFont_opsz,wght.ttf'
pygame.font.init()
other_font = pygame.font.Font(other_font_path, 16)

# For fighting Corcotta
fire_mode = False
arrows = 2

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Track the Corcotta")


# Track Occupied Positions
occupied = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Square starting position
posx = random.randint(0,4)
posy = random.randint(0,4)


# Pit positions - 3 pits
pits_pos = [[0,0],[0,0],[0,0]]
for p in range(3):
    while(occupied[posx][posy] == True):
        posx = random.randint(0,4)
        posy = random.randint(0,4)
    pits_pos[p] = [posx,posy]
    occupied[posx][posy] = True
    print("pit " + str(p) + ": [" + str(posx) + ", " + str(posy) + "]")

# Crocotta start pos
while(occupied[posx][posy] == True):
        posx = random.randint(0,4)
        posy = random.randint(0,4)
corcotta_pos = [posx,posy]
occupied[posx][posy] = True
print("corcotta: [" + str(posx) + ", " + str(posy) + "]")


# player place
posx = random.randint(0,4)
posy = random.randint(0,4)

while(occupied[posx][posy] or not isSafe()):
    posx = random.randint(0,4)
    posy = random.randint(0,4)
player_pos = [posx, posy] # Starting random
occupied[posx][posy] = True
print("player: [" + str(posx) + ", " + str(posy) + "]")


# Main game loop - printed out is the option to transfer to the other side of board
while True:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if(fire_mode == False):
                if (event.key == pygame.K_UP or event.key == pygame.K_w):
                    if(player_pos[1] > 0):
                        player_pos[1] -= 1
                    # else:
                    #     player_pos[1] = GRID_SIZE -1
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    if(player_pos[1] < GRID_SIZE - 1):
                        player_pos[1] += 1
                    # else:
                    #     player_pos[1] = 0
                elif (event.key == pygame.K_LEFT  or event.key == pygame.K_a):
                    if(player_pos[0] > 0):
                        player_pos[0] -= 1
                    # else:
                    #     player_pos[0] = GRID_SIZE - 1
                elif (event.key == pygame.K_RIGHT  or event.key == pygame.K_d):
                    if(player_pos[0] < GRID_SIZE -1):
                        player_pos[0] += 1
                    # else:
                    #     player_pos[0] = 0
                elif (event.key == pygame.K_q):
                    fire_mode = not fire_mode
                elif event.key == pygame.K_RETURN:  # Check for Enter key
                    reset_game()  # Call the reset function
            else:
                if (event.key == pygame.K_UP or event.key == pygame.K_w):
                    fireAtCorcotta(0)
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s):
                    fireAtCorcotta(2)
                elif (event.key == pygame.K_LEFT  or event.key == pygame.K_a):
                    fireAtCorcotta(3)
                elif (event.key == pygame.K_RIGHT  or event.key == pygame.K_d):
                    fireAtCorcotta(1)
                elif (event.key == pygame.K_q):
                    fire_mode = not fire_mode
                elif event.key == pygame.K_RETURN:  # Check for Enter key
                    reset_game()  # Call the reset function
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 470 <= mouse[0] <= (WIDTH-16)  and 569 <= mouse[1] <= (HEIGHT-19):
                displayInfo = not displayInfo
            
        
        
        

    # Check if adjacency
    isPlayerAdjacent()
    displayResult()
    
    isPlayerDead()
    
    if(game_over_str != "alive"):
        # print(game_over_str)
        screen.fill((217, 217, 217))  # Fill the screen with gray
        game_over_title = font.render("Game Over", True, TEXT_COLOR)
        title_width = game_over_title.get_width()
        screen.blit(game_over_title, ((WIDTH//2)-(title_width/2), 198))
        
        game_over_result = other_font.render(game_over_str, True, TEXT_COLOR)
        result_width = game_over_result.get_width()
        screen.blit(game_over_result, ((WIDTH//2)-(result_width/2), 264))
        
        restart_info = other_font.render("press ENTER to restart", True, TEXT_COLOR)
        result_info_width = restart_info.get_width()
        screen.blit(restart_info, ((WIDTH//2)-(result_info_width/2), 560)) 
    elif(displayInfo):
        screen.fill((217, 217, 217))  # Fill the screen with gray
        instructions_title = font.render("Instructions", True, TEXT_COLOR)
        title_width = instructions_title.get_width()
        screen.blit(instructions_title, ((WIDTH//2)-(title_width/2), 51))
        
        pygame.draw.line(screen,TEXT_COLOR, (63, 125), (WIDTH-63, 125))
        
        instructions_text = "At each step you can do one of two actions:\n1. Click WASD or arrows to move any \ndirection left, up, right, down\n2. Click (Q) to go into firing mode then clock WASD or \narrows to shoot in a direction\n3. If you step into a pit or corcotta, game over\n \nYou have 2 arrows, When you shoot:\n1. If your arrow hits the corcotta, you win\n2. If your arrow misses, the corcotta will \nmove to a different random position\n3. If you run out of arrows, game over\n \nObservations:\na) \"I hear panting\" if corcotta is in any adjacent space\nb) \"I feel a breeze\" If there is a pit in any adjacent space\nc) \"Silence\" if neither\n"
        lines = instructions_text.split('\n')
        y_offset = 145 

        for line in lines:
            instructions = other_font.render(line, True, TEXT_COLOR)
            text_width = instructions.get_width()
            screen.blit(instructions, ((WIDTH // 2) - (text_width // 2), y_offset))
            y_offset += instructions.get_height()+2  #separation between points
        
        # Info button to leave
        info = pygame.Rect(440, 557, 500, 43)
        pygame.draw.rect(screen, (217, 217, 217), info)
        info_text_surface = other_font.render("(i)", True, TEXT_COLOR) 
        screen.blit(info_text_surface, (465,570))
            
    else:
        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the title
        text_surface = font.render("Track the Corcotta", True, TEXT_COLOR) 
        screen.blit(text_surface, (122,4))

        # Draw shadow
        for i in range(6):  # Adjust the range for more or fewer gradient layers
            alpha = 255 - (i * 40)  # Decrease opacity for gradient effect
            shadow_color = (SHADOW_COLOR[0], SHADOW_COLOR[1], SHADOW_COLOR[2], alpha)
            
            # Create a shadow surface with the alpha channel
            shadow_surface = pygame.Surface((CELL_SIZE * GRID_SIZE, CELL_SIZE * GRID_SIZE), pygame.SRCALPHA)
            shadow_surface.fill(shadow_color)
            
            # Blit the shadow surface with an offset
            screen.blit(shadow_surface, (START_X + shadow_offset, START_Y + shadow_offset))

            # Offset the rectangle slightly to create a gradient effect
            shadow_offset += 1

        shadow_offset = 0

        # Draw the grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                rect = pygame.Rect(START_X + (x * CELL_SIZE), START_Y + (y * CELL_SIZE), CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, (217, 217, 217), rect)
                pygame.draw.rect(screen, (100, 100, 100), rect, 1)

        # Draw the square
        square_rect = pygame.Rect(START_X + (player_pos[0] * CELL_SIZE), START_Y + (player_pos[1] * CELL_SIZE), CELL_SIZE, CELL_SIZE)
        screen.blit(STAR, square_rect.topleft)
        
        # For result of changing position
        result = pygame.Rect(80, 487, 340, 52)
        pygame.draw.rect(screen, (217, 217, 217), result)
        result_text_surface = other_font.render(result_str, True, TEXT_COLOR) 
        screen.blit(result_text_surface, (101,503))
        
        # For Information
        arrow_info = pygame.Rect(0, 557, 500, 43)
        pygame.draw.rect(screen, (217, 217, 217), arrow_info)
        arrow_info_text_surface = other_font.render("Arrows: " + str(arrows), True, TEXT_COLOR) 
        screen.blit(arrow_info_text_surface, (23,570))

        play_info = pygame.Rect(100, 557, 500, 43)
        pygame.draw.rect(screen, (217, 217, 217), play_info)
        if(fire_mode):
            play_info_text_surface = other_font.render(" press (Q) then direction to fire", True, (215,0,0))
        else:
             play_info_text_surface = other_font.render(" press (Q) then direction to fire", True, TEXT_COLOR)
         
        screen.blit(play_info_text_surface, (120,570))
        
        info = pygame.Rect(440, 557, 500, 43)
        pygame.draw.rect(screen, (217, 217, 217), info)
        info_text_surface = other_font.render("(i)", True, TEXT_COLOR) 
        screen.blit(info_text_surface, (465,570))
        
        # Update the display
    pygame.display.flip()

        # Frame rate
    pygame.time.Clock().tick(30)


        