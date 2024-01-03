'''
    Position Finder is a tool designed to make the process of finding coordination points easy.
    Copyright © 2024 Islam Adel

    This file is part of Position Finder.

    Position Finder is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

    Position Finder is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along with Position Finder. If not, see <https://www.gnu.org/licenses/>. 
'''

import pygame
#---------------[Module for Precise Movement]---------------#

def PreciseMovement(Increment):
    Mpos = pygame.mouse.get_pos()

    if pygame.key.get_pressed()[pygame.K_LEFT]:
            pygame.mouse.set_pos([Mpos[0]-Increment, Mpos[1]])
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
            pygame.mouse.set_pos([Mpos[0]+Increment, Mpos[1]])
    if pygame.key.get_pressed()[pygame.K_DOWN]:
            pygame.mouse.set_pos([Mpos[0], Mpos[1]+Increment])
    if pygame.key.get_pressed()[pygame.K_UP]:
           pygame.mouse.set_pos([Mpos[0], Mpos[1]-Increment])