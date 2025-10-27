import pygame
from pygame.examples.moveit import GameObject


class Player(GameObject):
    def __init__(self, position):
        self.sheet = pygame.image.load('PSprites.png')

        #16x26
        self.sheet.set_clip(pygame.Rect(0, 0, 16, 26))

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()

        self.rect.topleft = position

        self.frame = 0

        self.leftWalkStates = {0:(0, 0, 16, 26), 1:(16, 0, 16, 26), 2:(32, 0, 16, 26), 3:(48, 0, 16, 26),
                               4:(64, 0, 16, 26), 5:(80, 0, 16, 26), 6:(96, 0, 16, 26), 7:(112, 0, 32, 26)}

        self.rightWalkStates = {0:(192, 20, 16, 26), 1:(176, 20, 16, 26), 2:(160, 20, 16, 26), 3:(144, 20, 16, 26),
                                4:(128, 20, 16, 26), 5:(112, 20, 16, 26), 6:(96,20, 16, 26), 7:(80, 20, 16, 26)}

        self.leftIdleStates = {0:(144, 0, 16, 26), 1:(160, 0, 16, 26), 2:(176, 0, 16, 26), 3:(192, 0, 16, 26)}

        self.rightIdleStates = {0:(48, 0, 16, 26), 1:(32, 0, 16, 26), 2:(16, 0, 16, 26), 3:(0, 0, 16, 26)}

        def get_frame(self, frame_set):  # Get the next frame in the given frame set (animation loop).
            # Increment the frame counter.
            self.frame += 1

            # Loop back to the first frame if the counter exceeds the number of frames.
            if self.frame > (len(frame_set) - 1):
                self.frame = 0

            print(frame_set[self.frame])  # Debugging: print the current frame's rectangle.
            return frame_set[self.frame]

        def clip(self, clipped_rect):  # Set the clipping region (current frame) based on a provided rectangle.
            if type(clipped_rect) is dict:  # If the clipped rect is a dictionary (animation set), get the next frame.
                self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
            else:
                # Set the clipping area directly if it's a specific rectangle.
                self.sheet.set_clip(pygame.Rect(clipped_rect))
            return clipped_rect  # Return the clipped rectangle.

        def update(self, direction):  # Update the character's position and animation based on the direction.
            if direction == 'left':  # Move left and play left walking animation.
                self.clip(self.leftWalkStates)
                self.rect.x -= 5  # Move the sprite left by 5 pixels.
            if direction == 'right':  # Move right and play right walking animation.
                self.clip(self.rightWalkStates)
                self.rect.x += 5


            # Standing still animations (no movement, just switching frames to standing).
            if direction == 'stand_left':
                self.clip(self.leftIdleStates)
            if direction == 'stand_right':
                self.clip(self.rightIdleStates)


            # Update the image with the current clipped frame.
            self.image = self.sheet.subsurface(self.sheet.get_clip())