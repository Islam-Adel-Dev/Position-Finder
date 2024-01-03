'''
    Position Finder is a tool designed to make the process of finding coordination points easy.
    Copyright © 2024 Islam Adel

    This file is part of Position Finder.

    Position Finder is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    Position Finder is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Position Finder. If not, see <https://www.gnu.org/licenses/>. 
'''

import pygame


#---------------[Module for UI elements]---------------#

class Text():
    def __init__(self, Font, Size, Text, Color, X, Y, surface, BGcolor=[0, 0, 0]):
        self.Font = Font
        self.Size = Size
        self.Text = Text
        self.Color = Color
        self.X = X
        self.Y = Y
        self.surface = surface
        self.BGcolor = BGcolor

    def draw(self):
        font = pygame.font.Font(f"Assets/Fonts/{self.Font}", self.Size)
        text = font.render(self.Text, True, self.Color, None)
        textRect = text.get_rect()
        textRect.topleft = self.X, self.Y
        self.surface.blit(text, textRect)



def Cursor(surface, resolution: list, color: list = [0,255,0]):
    pygame.mouse.set_visible(False) # Hide mouse
    Mpos = pygame.mouse.get_pos() # Get mouse position

    if Mpos[1] <= resolution[1]: # Check if mouse's Y position is within the range of original height
        pygame.draw.line(surface, color, [0, Mpos[1]], [resolution[0], Mpos[1]]) # Drawing the horizontal line
    pygame.draw.line(surface, color, [Mpos[0], 0], [Mpos[0], resolution[1]]) # Drawing the vertical line



def Grid(surface, resolution, size, color:list = [0,0,255]):
    RangeY = int(resolution[1]/size) if (resolution[1]%size) == 0 else int(resolution[1]/size)+1
    nY = 0
    for i in range(RangeY):
        pygame.draw.line(surface, color, [0, nY], [resolution[0], nY])
        nY += size
    
    RangeX = int(resolution[0]/size) if (resolution[0]%size) == 0 else int(resolution[0]/size)+1
    nX = 0
    for i in range(RangeX):
        pygame.draw.line(surface, color, [nX, 0], [nX, resolution[1]])
        nX += size


