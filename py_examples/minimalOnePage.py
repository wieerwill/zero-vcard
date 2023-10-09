#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.realpath(__file__), 'pic')
libdir = os.path.join(os.path.realpath(__file__), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import lib.waveshare_epd.epd2in13_V2 as epd2in13_V2
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)

try:
    epd = epd2in13_V2.EPD()
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)

    # import and set font
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    # clear the frame
    image = Image.new('1', (epd.height, epd.width), 255) 
    draw = ImageDraw.Draw(image)

    # add text
    draw.text((40, 5), 'Robert Jeutter', font = font24, fill = 0)
    draw.text((10, 35), 'FullStack Software Engineer', font = font15, fill = 0)
    draw.text((10, 55), 'Working @ AraCom IT Service AG', font = font15, fill = 0)
    draw.text((5, 100), 'find me on github.com/WieErWill', font = font15, fill = 0)

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
