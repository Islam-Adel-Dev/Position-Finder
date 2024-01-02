'''
     This file is part of Position Finder.

    Position Finder is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    Position Finder is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Position Finder. If not, see <https://www.gnu.org/licenses/>. 
'''
print('''
.-----------------------------------------------------------------------------------.
| Welcome to Position Finder by Islam-Adel-Dev                                      |
| You may find the source code at https://github.com/Islam-Adel-Dev/Position-Finder |
| Make sure to read the LICENCE carefully                                           |
'-----------------------------------------------------------------------------------'
      ''')

import pygame
import sys
import os
from UI.UI import *
from Functionalities.PreciseMovement import *
from Functionalities.AxisLock import *

#---------------[SETTINGS]---------------#
Text_Size = 26  # Optimal for x = 500 and above, decrease accordingly for windows less than 500
Text_Color = [255,255,255] # White

Increment = 1 # Precise movement increment value (minimum = 1)

Cursor_Color = [0, 255, 0] # Green
Grid_Color = [0, 0, 255] # Blue
UI_line_Color = [255, 0, 0] # Red


pygame.init() # Initializing pygame

# Taking user input
ResolutionX = int(input("Input resolution X: "))
ResolutionY = int(input("Input resolution Y: "))
Grid_Size = int(input("Inout grid size: "))
OriginalResolution = [ResolutionX, ResolutionY] # Saving original resolution for later calculations



# Screen variables
UI_h = 50 # UI box height
BG_Color = [0,0,0] # Black (R,G,B)
Resolution = [ResolutionX, ResolutionY+UI_h] # Adding UI box height to the original resolution (Later removed from calculations)
screen = pygame.display.set_mode(Resolution, pygame.RESIZABLE) # Creating screen object
pygame.display.set_caption("Position Finder") # Change the title of window
icon = pygame.image.load("Assets/icon.ico")
pygame.display.set_icon(icon)

# Time variables
FPS = 60 # Frames per second
Clock = pygame.time.Clock() # Creating clock object

# Toggle variables
Cursor_State = True # Cursor enabled by default 
Grid_state = True # Grid enabled by default
Y_lock = False
Y_lockPos = None
X_lock = False
X_lockPos = None

Center = [OriginalResolution[0]/2, OriginalResolution[1]/2]

# Loop variables
Running = True

# Loop
while Running:
    screen.fill(BG_Color) # Filling screen with black to draw on it

#---------------[Checking for events]---------------#
    for event in pygame.event.get(): # Checking events
        if event.type == pygame.QUIT: # Checking if user quit the tool
            Running = False
            sys.exit()

        if pygame.mouse.get_pressed()[0] == 1: # If RMB is pressed toggle cursor
            Cursor_State = not Cursor_State 
        if event.type == pygame.KEYDOWN: # Detect keyboard presses
            if pygame.key.get_pressed()[pygame.K_g]: # If g is pressed toggle grid
                Grid_state = not Grid_state
            if pygame.key.get_pressed()[pygame.K_c]: # If c is pressed move cursos to center and print it
                pygame.mouse.set_pos(Center) 
                print(f"Center point: {Center}")
            if pygame.key.get_pressed()[pygame.K_y]: # If y is pressed toggle Y axis lock and get current Y value
                Y_lock = not Y_lock
                Y_lockPos = lock_Y()
            if pygame.key.get_pressed()[pygame.K_x]: # If X is pressed toggle X acis lock and get current X value
                X_lock = not X_lock
                X_lockPos = lock_X()

            PreciseMovement(Increment) # Use arrow keys to move cursor by 1 pixel for precise movement

            
        if event.type == pygame.VIDEORESIZE: # Checking for window resize
            # Redifining resolution variables and recalculating center
            OriginalResolution = [event.w, event.h-UI_h] # Deducted UI_h from it to maintain
            ResolutionX, ResolutionY = OriginalResolution
            Resolution = [event.w, event.h]
            Center = [OriginalResolution[0]/2, OriginalResolution[1]/2]
            
            if OriginalResolution[0] < 155:
                Text_Size = 20
            else:
                Text_Size = 26
            # Changing window size and printing new size
            os.system("cls")
            screen = pygame.display.set_mode(Resolution, pygame.RESIZABLE)
            print(f"Resolution: {OriginalResolution}")

    
#---------------[Applying settings changes]---------------#
    Mpos = pygame.mouse.get_pos()
    if X_lock == True:
        pygame.mouse.set_pos([X_lockPos, Mpos[1]]) # Only Y axis can change (Horizontal line moves)
    if Y_lock == True:
        pygame.mouse.set_pos([Mpos[0], Y_lockPos]) # Only X axis can change (Vertical line moves)
    if Y_lock == True and X_lock == True:
        pygame.mouse.set_pos([X_lockPos, Y_lockPos]) # No movement is allowed if both axis are locked

    match Grid_state: # Checkin grid state
        case True:
            Grid(screen, OriginalResolution, Grid_Size) # Draw grid if true
        case False:
            pass # Do nothing if false

    match Cursor_State: # Check cursor state
        case True:
            Cursor(screen, OriginalResolution) # Activate cursor if true
        case False:
            pygame.mouse.set_visible(True) # Making mouse visible again if false

    pygame.draw.line(screen, [255,0,0], [0, ResolutionY], [ResolutionX, ResolutionY], 1) # UI box line

#---------------[Showing information in the UI box]---------------#
    Mpos = pygame.mouse.get_pos() # Get mouse position
    OptimalY = OriginalResolution[1]+Text_Size/2 # The start of UI box + half the text's height
    
    Text("MinecraftBold.otf", Text_Size, f"{Mpos}", Text_Color, 0, OptimalY, screen).draw() # Render text to show mouse position

    Clock.tick(FPS) # Limiting FPS to 60
    pygame.display.update() # Updating to show changes

    