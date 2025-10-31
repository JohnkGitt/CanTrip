import pygame
from Grid import Grid

# Tileset pixels are 16x16
ACTUAL_TILE_SIDE_LENGTH = 16
tileset = "Cantrip/Resources/Robo_Sprites_All.png"

# Resolves a grid position to a tile's image using a generic tileset image
def resolveTilesetGridPosToImage(grid_x, grid_y):
    tileset_image = pygame.image.load(tileset).convert_alpha()                       # Loads tileset image
    x, y = Grid.resolveGridPosToScreenCoords(grid_x, grid_y)                         # Resolves grid pos to screen coordinates (x, y)
    crop_rect = pygame.Rect(x, y, ACTUAL_TILE_SIDE_LENGTH, ACTUAL_TILE_SIDE_LENGTH)  # Builds rectangle size of what specific tile to crop from tileset image
    tile_image = tileset_image.subsurface(crop_rect)                                 # Crops tile image from the tileset, then returns
    return tile_image

# A tileset reference sheet can be found on Google Docs called "Tileset Reference Sheet"
ONE_BY_ONE_TILE = resolveTilesetGridPosToImage(0, 0)
LEFTMOST_THIN_PLATFORM = resolveTilesetGridPosToImage(1, 0)
LEFT_LEG_TRUSS = resolveTilesetGridPosToImage(2, 0)
RIGHT_LEG_TRUSS = resolveTilesetGridPosToImage(3,0)
MIDDLE_THIN_PLATFORM = resolveTilesetGridPosToImage(4, 0)
RIGHTMOST_THIN_PLATFORM = resolveTilesetGridPosToImage(5, 0)
LEFTMOST_LEFT_LEG_TRUSS = resolveTilesetGridPosToImage(6, 0)
X_TRUSS = resolveTilesetGridPosToImage(7, 0)
RIGHTMOST_RIGHT_LEG_TRUSS = resolveTilesetGridPosToImage(8, 0)