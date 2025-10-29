import pygame
import Cantrip

SCALE_FACTOR = 1                                     # Constant scale factor for tile size
TILE_SIDE_LENGTH = 16 * SCALE_FACTOR                 # Side length of each tile in pixels relative to screen
GRID_WIDTH = Cantrip.screen_w // TILE_SIDE_LENGTH    # Number of tiles that fit horizontally on the screen
GRID_LENGTH = Cantrip.screen_h // TILE_SIDE_LENGTH   # Number of tiles that fit vertically on the screen
MIN_GRID_POS = (0, 0)                                # Minimum grid position
MAX_GRID_POS = (GRID_WIDTH - 1, GRID_LENGTH - 1)     # Maximum grid position

# Functions for converting between screen coordinates and grid positions
def resolveScreenCoordsToGridPos(x, y):
    if x < 0 or y < 0:
        return None # Invalid screen coordinates
    
    if x >= Cantrip.screen_w or y >= Cantrip.screen_h:
        return None # Coordinates exceed screen dimensions
    
    if x % TILE_SIDE_LENGTH != 0 or y % TILE_SIDE_LENGTH != 0:
        return None # Coordinates not aligned to grid
    
    grid_x = x // TILE_SIDE_LENGTH
    grid_y = y // TILE_SIDE_LENGTH
    return (grid_x, grid_y)

# Function to convert grid position back to screen coordinates
def resolveGridPosToScreenCoords(grid_x, grid_y):
    if grid_x < MIN_GRID_POS[0] or grid_y < MIN_GRID_POS[1]:
        return None # Invalid grid position
    
    if grid_x > MAX_GRID_POS[0] or grid_y > MAX_GRID_POS[1]:
        return None # Grid position exceeds maximum limits

    x = grid_x * TILE_SIDE_LENGTH
    y = grid_y * TILE_SIDE_LENGTH
    return (x, y)

# Function to draw an image at a specific grid position
def drawToScreenWithGridPos(screen, grid_x, grid_y, image):
    screen_coords = resolveGridPosToScreenCoords(grid_x, grid_y)
    if screen_coords is None:
        return # Invalid grid position
    
    screen.blit(image, screen_coords)