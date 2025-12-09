import pygame
import os
from GameObjects.player.Player import Player
from GameObjects.Door.Door import Door
from GameObjects.Assoc_Block import Assoc_Block

RESOURCES_FILEPATH = os.path.join('Resources', '')

class Level:
    def __init__(self, background, ground, level_id, screen, cutscene=False):
        self.background = background      # Background image for the level
        self.ground = ground              # Ground sprite for collision detection
        self.level_id = level_id          # Level identifier

        #all game objects that arent platforms go here
        self.spriteList = pygame.sprite.Group()
        #all block objects go here
        self.blockList = pygame.sprite.Group()
        #all platforms and blovks go here
        self.col_list = pygame.sprite.Group()
        self.col_list.add(ground)
        #all game objects also go here
        self.all_gameObjects = pygame.sprite.Group()
        self.cur_screen = screen
        self.canRobot = Player(0, 0, 16, 26, 1)
        self.endDoor = Door(0, 0, 58, 60, 2)
        self.spriteList.add(self.endDoor)
        self.all_gameObjects.add(self.endDoor)
        self.all_gameObjects.add(self.canRobot)
        self.gameOver = False
        self.eBufferCounter = 0
        self.clock = pygame.time.Clock()
        self.level_instructions = []
        self.assoc_status = {}
        self.horizontal_text_offset = 900  # Default horizontal offset for text display
        self.cutscene = cutscene

    # Resolve object ID to target object
    def resolveObjIDtoTargetObj(self, id):
        for key, value in self.all_gameObjects:
            if key == id:
                return value
        return None
    
    # Getters and setters
    def getLevelID(self):
        return self.level_id
    
    def getObjects(self):
        return self.object_dict
    
    def update_assoc_status(self):
        new_status = {}
        for block in self.blockList:
            if isinstance(block, Assoc_Block.Assoc_Block):
                status = {
                    "active": getattr(block, "associationActive", False),
                    "assoc_block": block,
                    "obj": getattr(block, "objBlockAssociation", None),
                    "att": getattr(block, "attBlockAssociation", None),
                    "remove": getattr(block, "removeAssociation", False)
                }
                # store by the assoc block's unique id (use rect.topleft as fallback if no id)
                try:
                    key = block.id
                except AttributeError:
                    key = (block.rect.x, block.rect.y)
                new_status[key] = status
        self.assoc_status = new_status

    def is_assoc_active_for_block(self, assoc_block):
        key = assoc_block.id if isinstance(assoc_block, Assoc_Block.Assoc_Block) else assoc_block
        entry = self.assoc_status.get(key)
        return bool(entry and entry.get("active"))

    def get_assoc_for_block(self, assoc_block):
        key = assoc_block.id if isinstance(assoc_block, Assoc_Block.Assoc_Block) else assoc_block
        entry = self.assoc_status.get(key)
        if not entry:
            return (False, None, None, False)
        return (entry.get("active", False), entry.get("obj"), entry.get("att"), entry.get("remove", False))

    def get_all_assoc_statuses(self):
        return self.assoc_status
    
    def printLevelInstructions(self):
        font = pygame.font.SysFont('arial', 30)
        y_offset = 50
        for line in self.level_instructions:
            text_surface = font.render(line, True, (255, 255, 255))
            self.cur_screen.blit(text_surface, (50, y_offset))
            y_offset += 40

    def runLevel(self):
        pygame.mixer.music.load(f'{RESOURCES_FILEPATH}Tea K Pea - mewmew.mp3')
        pygame.mixer.music.play(loops=-1)

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.cur_screen.blit(self.background, (0, 0))
            self.cur_screen.blit(self.ground.image, self.ground.rect)
            if self.eBufferCounter <= 5:
                self.eBufferCounter += 1

            # update each moveable sprite
            for sprite in self.spriteList:
                sprite.update(self.col_list)
                self.cur_screen.blit(sprite.image, sprite.rect)

            self.update_assoc_status()

            self.additionalLeveRunLogic()

            self.printLevelInstructions()

            if self.cutscene:
                self.canRobot.update('right', self.col_list)
            else:
                # player input
                keys = pygame.key.get_pressed()
                if keys[pygame.K_LEFT]:
                    self.canRobot.update('left', self.col_list)
                    if keys[pygame.K_UP]:
                        self.canRobot.update('up', self.col_list)
                elif keys[pygame.K_RIGHT]:
                    self.canRobot.update('right', self.col_list)
                    if keys[pygame.K_UP]:
                        self.canRobot.update('up', self.col_list)
                elif keys[pygame.K_UP]:
                    self.canRobot.update('up', self.col_list)
                elif keys[pygame.K_e] and self.eBufferCounter > 3:
                    if len(self.canRobot.grabbed) == 0:
                        self.canRobot.grab(self.blockList, self.col_list)
                        self.eBufferCounter = 0
                    else:
                        self.canRobot.place(self.col_list)
                        self.eBufferCounter = 0
                elif keys[pygame.K_SPACE] and self.endDoor.isOpen():
                    if self.canRobot.rect.colliderect(self.endDoor.rect):
                        pygame.display.set_caption("win")
                        self.gameOver = True
                        pass
                else:
                    self.canRobot.update('stand_right', self.col_list)
                    
            self.cur_screen.blit(self.canRobot.image, self.canRobot.rect)
            self.cur_screen.blit(self.canRobot.guide.image, self.canRobot.guide.rect)

            pygame.display.flip()
            self.clock.tick(20)

    
    def additionalLeveRunLogic(self):
        if not self.assoc_status:
            return
        
        # helper to get a display string from an object
        def text_of(o):
            if o is None:
                return ""
            # prefer a get_text() method if provided, else a .text attribute, else str()
            getter = getattr(o, "get_text", None)
            if callable(getter):
                try:
                    return getter()
                except Exception:
                    pass
            if hasattr(o, "text"):
                return getattr(o, "text")
            return str(o)
    
        assocsToPrint = []

        obj = None
        assoc_block = None
        att = None

        for key, entry in self.assoc_status.items():
            # entry should be a dict like {"active": bool, "assoc_block": ..., "obj": ..., "att": ...}
            obj = entry.get("obj")
            assoc_block = entry.get("assoc_block")
            att = entry.get("att")

        obj_text = text_of(obj)
        assoc_text = text_of(assoc_block)
        att_text = text_of(att)

        newLine = f'{obj_text} {assoc_text} {att_text}'

        color = (0, 255, 0) if entry.get("active") else (255, 0, 0)

        assocsToPrint.append((newLine, color))
      
        font = pygame.font.SysFont('arial', 30)
        y_offset = 50
        for line, color in assocsToPrint:
            text_surface = font.render(line, True, color)
            self.cur_screen.blit(text_surface, (self.horizontal_text_offset, y_offset))
            y_offset += 40




