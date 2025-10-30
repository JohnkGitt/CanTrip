import pygame
from Grid import Grid

tileset = "Cantrip/Resources/Robo_Sprites_All.png"

def resolveTilesetGridPosToImage(grid_x, grid_y):
    tileset_image = pygame.image.load(tileset).convert_alpha()
    tile_width = Grid.TILE_SIDE_LENGTH
    tile_height = Grid.TILE_SIDE_LENGTH
    rect = pygame.Rect(grid_x * tile_width, grid_y * tile_height, tile_width, tile_height)
    tile_image = pygame.Surface((tile_width, tile_height), pygame.SRCALPHA)
    return tile_image

ONE_BY_ONE_TILE = resolveTilesetGridPosToImage(0, 0)
LEFTMOST_THIN_PLATFORM = resolveTilesetGridPosToImage(1, 0)
MIDDLE_THIN_PLATFORM = resolveTilesetGridPosToImage(3, 0)
