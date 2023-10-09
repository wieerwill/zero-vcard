#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

min_x=0
max_x=249
min_y=0
max_y=121

print_pause=10

try:
    logging.info("vCARD startup")
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    time.sleep(0.5)
    logging.info("clear frame")
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    time.sleep(0.5)
    logging.info("update frame")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    time.sleep(0.5)

    # Settings FONTS
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    font20 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 20)
    font25 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 25)
    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
    font35 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 35)
    font45 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 45)
    font50 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 60)
    
    image = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame    
    draw = ImageDraw.Draw(image)
    
    draw.rectangle([(min_x,min_y),(40,40)], outline = 0) #emtpy rectangle
    draw.line([(min_x,min_y),(40,40)], fill = 0,width = 1)
    draw.line([(min_x,40),(40,min_y)], fill = 0,width = 1)
    draw.rectangle([(45,min_y),(85,40)],fill = 0) #filled rectangle

    draw.chord((90, min_y, 130, 40), 0, 360, fill = 0) #filled circle
    draw.ellipse((135, min_y, 175, 40), outline = 0) 
    draw.pieslice((135, min_y, 175, 40), 90, 180, outline = 0)
    draw.pieslice((135, min_y, 175, 40), 270, 360, fill = 0)

    draw.line([(min_x,max_y-60),(min_x,max_y)], fill = 0,width = 1)
    draw.line([(min_x+4,max_y-50),(min_x+4,max_y)], fill = 0,width = 1)
    draw.line([(min_x+8,max_y-30),(min_x+8,max_y)], fill = 0,width = 1)
    draw.line([(min_x+12,max_y-10),(min_x+12,max_y)], fill = 0,width = 1)

    draw.line([(max_x,min_y),(max_x,max_y)], fill = 0,width = 1)
    draw.line([(max_x-4,min_y),(max_x-4,max_y/2)], fill = 0,width = 1)
    draw.line([(max_x-8,min_y),(max_x-8,max_y/3)], fill = 0,width = 1)
    draw.line([(max_x-12,min_y),(max_x-12,max_y/4)], fill = 0,width = 1)
    draw.line([(max_x-16,min_y),(max_x-16,max_y/5)], fill = 0,width = 1)
    draw.line([(max_x-20,min_y),(max_x-20,max_y/6)], fill = 0,width = 1)

    draw.text((20, 40), 'e-Paper vCard', font = font25, fill = 0)
    draw.text((30, 70), 'by WieErWill', font = font35, fill = 0)
    epd.display(epd.getbuffer(image))
    time.sleep(3)

    while True:
        # clear the frame
        image = Image.new('1', (epd.height, epd.width), 255) 
        draw = ImageDraw.Draw(image)
        draw.rectangle([(min_x,min_y),(max_x,max_y)], outline = 0) #emtpy rectangle
        draw.rectangle([(min_x+3,min_y+3),(max_x-3,max_y-3)], outline = 0) #emtpy rectangle
        draw.text((10, 10), 'Robert Jeutter', font = font35, fill = 0)
        draw.text((10, 60), 'Software Engineer', font = font25, fill = 0)
        draw.text((10, 85), 'working @ AraCom', font = font25, fill = 0)
        epd.display(epd.getbuffer(image))
        time.sleep(print_pause)

        image = Image.new('1', (epd.height, epd.width), 255) 
        draw = ImageDraw.Draw(image)
        draw.text((2, 5), 'Social Robotics', font = font35, fill = 0)
        draw.text((2, 50), 'Machine Learning &', font = font25, fill = 0)
        draw.text((2, 85), 'Human-Machine-Coop', font = font20, fill = 0)
        epd.display(epd.getbuffer(image))
        time.sleep(print_pause)

        # clear the frame
        imageARA = Image.new('1', (epd.height, epd.width), 255) 
        #bmp = Image.open(os.path.join(picdir, 'ara.bmp'))
        #bmp2 = bmp.resize((250,100))
        #imageARA.paste(bmp, (2,5))
        draw = ImageDraw.Draw(imageARA)
        draw.text((15, 5), 'AraCom', font = font50, fill = 0)
        draw.text((13, 65), 'IT Services GmbH', font = font30, fill = 0)
        draw.text((14, 100), 'Mail: robert.jeutter@aracom.de', font = font15, fill = 0)
        epd.display(epd.getbuffer(imageARA))
        time.sleep(print_pause)
            
        # clear the frame
        epd.init(epd.FULL_UPDATE)
        image = Image.new('1', (epd.height, epd.width), 255) 
        draw = ImageDraw.Draw(image)
        draw.text((50, 5), 'Write me', font = font25, fill = 0)
        draw.text((20, 35), 'robert.jeutter', font = font35, fill = 0)
        draw.text((20, 70), '@aracom.de', font = font35, fill = 0)
        epd.display(epd.getbuffer(image))
        time.sleep(print_pause)

        # clear the frame
        epd.init(epd.FULL_UPDATE)
        image = Image.new('1', (epd.height, epd.width), 255) 
        draw = ImageDraw.Draw(image)
        draw.text((25, 2), 'find me on', font = font25, fill = 0)
        draw.text((15, 25), 'GitHub.com/', font = font35, fill = 0)
        draw.text((20, 60), 'WieErWill', font = font45, fill = 0)
        epd.display(epd.getbuffer(image))
        time.sleep(print_pause)

        imageQR = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
        bmp = Image.open(os.path.join(picdir, 'qr.bmp'))
        imageQR.paste(bmp, (2,2))    
        draw = ImageDraw.Draw(imageQR)
        draw.text((130, 5), 'SCAN ME', font = font25, fill = 0)
        draw.text((140, 45), '\(0^0)/', font = font25, fill = 0)
        draw.text((130, 90), 'SCAN ME', font = font25, fill = 0)
        epd.display(epd.getbuffer(imageQR))
        time.sleep(print_pause)

    # set display to sleep mode
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    epd.sleep()
    time.sleep(print_pause)

except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()