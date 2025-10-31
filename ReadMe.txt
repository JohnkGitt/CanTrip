run cantrip.py

John Aragon:
    - CanRobot (the player)
    - Door
    - Obj Blocks
    - Attribute Blocks

Bode Hooker:
    - Assoc_Block.py (including prox_check() and assoc_handler() and related bug fixes for majority of logic)
        - This class creates a new block type: the association block. This is the block that associates an attribute to an object.
        - The basic functionality makes sure that a valid association has been made with an object block and attribute block.
        - prox_check() determined the blocks are in the places intended locations to assign an association to.
        - assoc_handler() resolves what method to call in order to create the valid association.
        - Handled most of the bug fixes related to Assoc_Block
    - Grid.py
        - This class simplifies drawing tiles to a screen by converting pixel integers to a grid position.
        - This is useful for building levels with tiles (which will mostly be used for every level, minus any objects we intend to place by pixel placement)
        - This is also useful for resolving a tile image from the tileset.
    - Level.py
        - This class will be used for loading, deloading, and storing levels based on predefined tile placement and object placement
    - Tileset.py
        - This class utilizes Grid.py to resolve tiles from our tileset asset to variables we can refer to for building levels in the future
    - Base functionality for GameObjects.py
        - GameObjects.py acts as an interface for all objects in our game, requiring (x,y) coordinates, width, height, and a unique including

