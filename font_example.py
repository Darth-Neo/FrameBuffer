#!/usr/bin/env python

from fb_sdl import *

from Logger import *
logger = setupLogging(__name__)
logger.setLevel(DEBUG)


if __name__ == u"__main__":
    # Create an instance of the PyScope class
    scope = PyDisplay()

    # Get a refernce to the system font, size 30
    font = pygame.font.Font(None, 30)

    # Render some white text (pyDisplay 0.1) onto text_surface
    text_surface = font.render(u'pyDisplay (%s)' % u"0.1", True, (255, 255, 255))  # White text

    # Blit the text at 10, 0
    scope.screen.blit(text_surface, (10, 0))

    # Update the display
    pygame.display.update()

    # Wait 10 seconds
    time.sleep(10)