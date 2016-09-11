#!/usr/bin/env python
import os
import time
import pygame


# Number of seconds to wait between clicks events. Set to a
# few hunded milliseconds to prevent accidental double clicks
# from hard screen presses.
CLICK_DEBOUNCE = 0.4

# Color configuration (RGB tuples, 0 to 255).
MAIN_BG = (0, 0, 0)  # Black
INPUT_BG = (60, 255, 255)  # Cyan-ish
INPUT_FG = (0, 0, 0)  # Black
CANCEL_BG = (128, 45, 45)  # Dark red
ACCEPT_BG = (45, 128, 45)  # Dark green
BUTTON_BG = (60, 60, 60)  # Dark gray
BUTTON_FG = (255, 255, 255)  # White
BUTTON_BORDER = (200, 200, 200)  # White/light gray
INSTANT_LINE = (0, 255, 128)  # Bright yellow green.

# Alignment constants.
ALIGN_LEFT = 0.0
ALIGN_TOP = 0.0
ALIGN_CENTER = 0.5
ALIGN_RIGHT = 1.0
ALIGN_BOTTOM = 1.0


def align(child, parent, horizontal=ALIGN_CENTER, vertical=ALIGN_CENTER, hpad=0, vpad=0):
    """Return tuple of x, y coordinates to render the provided child rect
    aligned inside the parent rect using the provided horizontal and vertical
    alignment.  Each alignment value can be ALIGN_LEFT, ALIGNT_TOP, ALIGN_CENTER,
    ALIGN_RIGHT, or ALIGN_BOTTOM.  Can also specify optional horizontal padding
    (hpad) and vertical padding (vpad).
    """
    cx, cy, cwidth, cheight = child
    px, py, pwidth, pheight = parent
    return (px + (horizontal * pwidth - horizontal * cwidth) + hpad,
            py + (vertical * pheight - vertical * cheight) + vpad)


if __name__ == u'__main__':
    # Initialize pygame and SDL to use the PiTFT display and touchscreen.
    os.putenv(u'SDL_VIDEODRIVER', u'fbcon')
    os.putenv(u'SDL_FBDEV', u'/dev/fb1')
    os.putenv(u'SDL_MOUSEDRV', u'TSLIB')
    os.putenv(u'SDL_MOUSEDEV', u'/dev/input/touchscreen')
    pygame.display.init()
    pygame.font.init()
    pygame.mouse.set_visible(False)

    # Get size of screen and create main rendering surface.
    size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    # Display splash screen.
    splash = pygame.image.load(u'freqshow_splash.png')
    screen.fill(MAIN_BG)
    screen.blit(splash, align(splash.get_rect(), (0, 0, size[0], size[1])))
    pygame.display.update()

    splash_start = time.time()

    # Main loop to process events and render current view.
    lastclick = 0
    while True:
        # Process any events (only mouse events for now).
        for event in pygame.event.get():
            if event.type is pygame.MOUSEBUTTONDOWN \
                    and (time.time() - lastclick) >= CLICK_DEBOUNCE:
                lastclick = time.time()

        pygame.display.update()
