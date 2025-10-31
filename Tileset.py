import pygame
from Grid import Grid

tileset = "Cantrip/Resources/Robo_Sprites_All.png"
tileset_image = pygame.image.load(tileset).convert_alpha() # Load tileset image

# Resolves a grid position to a tile's image using a generic tileset image
def resolveTilesetGridPosToImage(grid_x, grid_y):
    x, y = Grid.resolveGridPosToScreenCoords(grid_x, grid_y)                                   # Resolves grid pos to screen coordinates (x, y)
    crop_rect = pygame.Rect(x, y, Grid.ACTUAL_TILE_SIDE_LENGTH, Grid.ACTUAL_TILE_SIDE_LENGTH)  # Builds rectangle size of what specific tile to crop from tileset image
    tile_image = tileset_image.subsurface(crop_rect)                                           # Crops tile image from the tileset, then returns
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
HALF_TILE = resolveTilesetGridPosToImage(9, 0)
TOPLEFT_NxN_TILE = resolveTilesetGridPosToImage(0, 1)
TOPMIDDLE_NxN_TILE = resolveTilesetGridPosToImage(1, 1)
TOPRIGHT_NxN_TILE = resolveTilesetGridPosToImage(2, 1)
LEFTMIDDLE_NxN_TILE = resolveTilesetGridPosToImage(0, 2)
MIDDLE_NxN_TILE = resolveTilesetGridPosToImage(1, 2)
RIGHTMIDDLE_NxN_TILE = resolveTilesetGridPosToImage(2, 2)
BOTTOMLEFT_NxN_TILE = resolveTilesetGridPosToImage(0, 3)
BOTTOMMIDDLE_NxN_TILE = resolveTilesetGridPosToImage(1, 3)
BOTTOMRIGHT_NxN_TILE = resolveTilesetGridPosToImage(2, 3)