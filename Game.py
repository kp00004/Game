import pygame

# setup basics
pygame.init()
screen_size = 810
screen = pygame.display.set_mode((screen_size, screen_size)) #screen dimensions
clock = pygame.time.Clock() #if its just moment game with amount of time dectedion 
running = True  #loop
dt = 0 #nvm see end of code
pygame.display.set_caption("Knight Movement") #used to set name of the program

player_image = pygame.image.load(r"C:\Users\spsan\OneDrive\Desktop\main\game\knight.png").convert_alpha()  #importing image
player_size = 50
player_image = pygame.transform.scale(player_image, (player_size, player_size))   #resizing it

box_width = 600
box_height = 600
box_x = (screen_size - box_width) // 2  # Center the box horizontally
box_y = (screen_size - box_height) // 2  # Center the box vertically
box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
player_pos = pygame.Vector2(box_x + player_size, box_y + player_size)    #make the position of the palyer in vector

speed = 50 #speed of character

mapmap = [
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
    ["W", "F", "F", "F", "W", "F", "F", "F", "F", "F", "F", "W"],
    ["W", "F", "W", "F", "W", "F", "W", "W", "W", "W", "F", "W"],
    ["W", "F", "W", "F", "F", "F", "W", "F", "F", "F", "F", "W"],
    ["W", "F", "W", "W", "W", "F", "W", "W", "W", "W", "F", "W"],
    ["W", "F", "F", "F", "F", "F", "F", "F", "F", "W", "F", "W"],
    ["W", "F", "W", "F", "W", "W", "F", "W", "F", "W", "F", "W"],
    ["W", "F", "F", "F", "F", "F", "F", "W", "F", "F", "F", "W"],
    ["W", "F", "W", "W", "W", "W", "F", "W", "W", "W", "F", "W"],
    ["W", "F", "F", "F", "F", "F", "F", "F", "F", "F", "F", "W"],
    ["W", "F", "W", "W", "W", "W", "W", "W", "W", "W", "F", "W"],
    ["W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W", "W"],
]


wall_image = pygame.image.load(r"C:\Users\spsan\OneDrive\Desktop\Main\game\wall.png").convert_alpha()  #importing image
floor_image = pygame.image.load(r"C:\Users\spsan\OneDrive\Desktop\Main\game\floor.png").convert_alpha()  #importing image
wall_size = 50
wall_image = pygame.transform.scale(wall_image, (wall_size, wall_size))
floor_size = 50
floor_image = pygame.transform.scale(floor_image, (floor_size, floor_size)) 

while running:
    
    # pygame.QUIT = window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:        #takes input when a key is pressed
            new_x, new_y = player_pos.x, player_pos.y  # Store new position

            if event.key == pygame.K_w:
                new_y -= speed  # Move up
            elif event.key == pygame.K_s:
                new_y += speed  # Move down
            elif event.key == pygame.K_a:
                new_x -= speed  # Move left
            elif event.key == pygame.K_d:
                new_x += speed  # Move right

            grid_x, grid_y = (new_x - box_x) // floor_size, (new_y - box_y) // floor_size  # next position in terms of square
            
            if 0 <= grid_y < len(mapmap) and 0 <= grid_x < len(mapmap[0]) and mapmap[int(grid_y)][int(grid_x)] == "F":
                player_pos.x, player_pos.y = new_x, new_y  # Move the player if it's a floor


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # Draw the grid map
    for row_index, row in enumerate(mapmap):
        for col_index, tile in enumerate(row):
            x, y = box_x + col_index * floor_size, box_y + row_index * floor_size
            if tile == "W":
                screen.blit(wall_image, (x, y))
            else:
                screen.blit(floor_image, (x, y))

    grid = 50
    # vertical lines
    for x in range(box_rect.left, box_rect.right, grid):
        #pygame.draw.line(surface, color, start_pos, end_pos, width)
        pygame.draw.line(screen, "grey", (x, box_rect.top), (x, box_rect.bottom), 1)
    # Horizontal lines
    for y in range(box_rect.top, box_rect.bottom, grid):
        pygame.draw.line(screen, "grey", (box_rect.left, y), (box_rect.right, y), 1)
        
    # Draw the box
    pygame.draw.rect(screen, "black", box_rect, 2)  # 2 is the border thickness

    #placing the image
    screen.blit(player_image, player_pos)

    #pygame.draw.circle(screen, "red", player_pos, 40)

    # Handle key presses (one pixel movement per press)
    #print(event)
    #print(event.type)
    #print(event)

    # make sure the player doesnt leave the box
    #max(left,min(player,right))
    player_pos.x = max(box_rect.left, min(player_pos.x, box_rect.right - player_size))
    player_pos.y = max(box_rect.top, min(player_pos.y, box_rect.bottom - player_size))

    # flip() the display to put your work on screen
    pygame.display.flip()

    #clock.tick(60) = maintains fps
    #and it returns the time interval btw it and its last call like readline
    clock.tick(60)

pygame.quit()
