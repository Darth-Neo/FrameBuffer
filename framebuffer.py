#!/usr/bin/env python
import os
import pygame
import time
import random

from Logger import *
logger = setupLogging(__name__)
logger.setLevel(DEBUG)

class PyDisplay:
    screen = None

    def __init__(self):
        u"""Ininitializes a new pygame screen using the framebuffer"""

        disp_no = os.getenv(u"DISPLAY")
        if disp_no:
            logger.debug(u"I'm running under X display = %s" % disp_no)

        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = [u'fbcon', u'directfb', u'svgalib']
        found = False
        for driver in drivers:
            # Make sure that SDL_VIDEODRIVER is set
            if not os.getenv(u'SDL_VIDEODRIVER'):
                logger.debug(u"Setting SDL_VIDEODRIVER ...")
                os.putenv(u'SDL_VIDEODRIVER', driver)
            try:
                pygame.display.init()
                logger.debug(u"PyGame Initialized ...")
            except pygame.error:
                logger.debug(u'Driver: %s failed.' % driver)
                continue
            found = True
            break

        if not found:
            raise Exception(u'No suitable video driver found!')

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        logger.debug(u"Frame buffer size: %d x %d" % (size[0], size[1]))
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

        logger.debug(u"Clear the screen to start")
        self.screen.fill((0, 0, 0))

        logger.debug(u"Initialise font support")
        pygame.font.init()

        logger.debug(u"Render the screen")
        pygame.display.update()

    def __del__(self):
        """"Destructor to make sure pygame shuts down, etc."""

    def test(self):
        logger.debug(u"test run")

        logger.debug(u"Fill the screen with red (255, 0, 0)")
        red = (255, 0, 0)
        self.screen.fill(red)

        logger.debug(u"Update the display")
        pygame.display.update()


if __name__ == u"__main__":
    sleep_time = 10

    # Create an instance of the PyScope class
    scope = PyDisplay()
    scope.test()
    logger.debug(u"Sleep for %d seconds" % sleep_time)
    time.sleep(sleep_time)
    logger.debug(u"Bye ...")
