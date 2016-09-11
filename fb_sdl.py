#!/usr/bin/env python
import os
import pygame
import time
import random

from Logger import *

logger = setupLogging(__name__)
logger.setLevel(DEBUG)


# morrisspid.james@hotmail.com

class PyDisplay:
    screen = None

    def __init__(self):

        disp_no = os.getenv(u"DISPLAY")
        if disp_no:
            logger.debug(u"I'm running under X display = %s" % disp_no)

        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output

        os.putenv(u'SDL_VIDEODRIVER', u'fbcon')
        os.putenv(u'SDL_FBDEV', u'/dev/fb1')
        os.putenv(u'SDL_MOUSEDRV', u'TSLIB')
        os.putenv(u'SDL_MOUSEDEV', u'/dev/input/touchscreen')

        try:
            pygame.display.init()
            logger.debug(u"PyGame Initialized ...")
        except pygame.error, msg:
            logger.debug(u'%s' % msg)

        self.size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        logger.debug(u"Frame buffer size: %d x %d" % (self.size[0], self.size[1]))
        self.screen = pygame.display.set_mode(self.size, pygame.FULLSCREEN)

        logger.debug(u"Clear the screen to start")
        self.screen.fill((0, 0, 0))

        logger.debug(u"Initialise font support")
        pygame.font.init()

        pygame.mouse.set_visible(False)

        logger.debug(u"Render the screen")
        pygame.display.update()

    def __del__(self):
        """"Destructor to make sure pygame shuts down, etc."""

    def drawGraticule(self):
        """"Renders an empty graticule"""

        offset = 10
        height = self.size[1] - offset
        width = self.size[0] - offset

        start_h = height - offset
        start_w = width - offset
        start_x = offset
        start_y = offset

        borderColor = (255, 255, 255)
        lineColor = (64, 64, 64)
        subDividerColor = (128, 128, 128)

        # Outer border: 2 pixels wide
        border = 2
        rect = [start_x - border, start_y - border, width - border, height - border]

        pygame.draw.rect(self.screen, borderColor, rect, 2)

        # Horizontal lines apart
        hla = 40
        h_lines = (start_h / hla) + 1
        logger.debug(u"h_lines : %d" % h_lines)
        for i in range(0, h_lines):
            y = i * hla
            logger.debug("y : %d" % y)
            pygame.draw.line(self.screen, lineColor, (start_x, y), (start_w + offset, y))

        # Vertical lines apart
        vla = 40
        v_lines = (start_w / vla) + 1
        logger.debug(u"v_lines  : %d" % v_lines)
        for i in range(0, v_lines):
            x = i * vla
            logger.debug("x : %d : %d : %d" % (x, start_y, start_h))
            pygame.draw.line(self.screen, lineColor, (x, start_y), (x, start_h + offset))

        # Horizontal sub-divisions (10 pixels apart)
        hsp = 10
        h_middle = height / 2
        sd_h_mp = h_middle + (hsp / 2) + (offset / 2)
        sd_h_mn = h_middle - (hsp / 2) + (offset / 2)
        sd_h_lines = start_w / hsp

        for i in range(0, sd_h_lines):
            x = start_x + i * hsp
            logger.debug("sd x : %d" % x)
            pygame.draw.line(self.screen, subDividerColor, (x, sd_h_mp), (x, sd_h_mn))

        # Vertical sub-divisions (10 pixels apart)
        vsp = 10
        v_middle = width / 2
        sd_v_mp = v_middle + (vsp / 2) + (offset / 2)
        sd_v_mn = v_middle - (vsp / 2) + (offset / 2)
        sd_v_lines = start_h / vsp

        for i in range(0, sd_v_lines):
            y = start_y + i * vsp
            logger.debug("sd y : %d" % y)
            pygame.draw.line(self.screen, subDividerColor, (sd_v_mp, y), (sd_v_mn, y))

        # Update the display
        pygame.display.update()

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

    scope.drawGraticule()

    logger.debug(u"Sleep for %d seconds" % sleep_time)
    time.sleep(sleep_time)

    logger.debug(u"Bye ...")
