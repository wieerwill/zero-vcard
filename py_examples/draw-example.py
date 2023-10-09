#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
from PIL import Image,ImageDraw

logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    # clear the frame
    image = Image.new('1', (epd.height, epd.width), 255) 
    draw = ImageDraw.Draw(image)

    # add text
    # x/y coordinates start at left top with 0,0 

    # empty reactangle with crossed lines inside
    draw.rectangle([(5,5),(55,55)], outline = 0)
    draw.line([(5,5),(55,55)], fill = 0, width = 1)
    draw.line([(5,55),(55,5)], fill = 0, width = 1)

    # filled rectangle
    draw.rectangle([(60,5),(110,55)],fill = 0)

    # draw a chord rotating in the middle
    draw.chord((10, 80, 55, 120), 0, 360, fill = 0)

    # draw a simple circe
    draw.ellipse((55, 60, 95, 100), outline = 0)

    # draw four forth parts of a circle to create a single one 
    draw.pieslice((55, 60, 95, 100), 90, 180, outline = 0)
    draw.pieslice((55, 60, 95, 100), 270, 360, fill = 0)
    draw.polygon([(110,0),(110,50),(150,25)], outline = 0)
    draw.polygon([(190,0),(190,50),(150,25)], fill = 0)

    # add new image to display
    epd.display(epd.getbuffer(image))
    # set display to sleep mode
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()