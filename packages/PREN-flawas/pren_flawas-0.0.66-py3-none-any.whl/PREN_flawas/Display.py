import os, sys, logging, time
import logging
import logging.config
from waveshare_epd import epd1in54_V2
from PIL import Image, ImageDraw, ImageFont
from os import path

log_file_path = path.join(path.dirname(path.abspath(__name__)), 'logger.config')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger("Display")

def __init__(epd, fontTTC, backgroundBMP ):
    logging.debug("Display init")
    font = ImageFont.truetype(os.path.join(fontTTC), 16)
    epd.init(1)
    background = Image.open(os.path.join(backgroundBMP))
    epd.displayPartBaseImage(epd.getbuffer(background))

    # epd.init(1) # into partial refresh mode
    ImageDraw.Draw(background)
    logging.debug("Display init done")

def clearDisplay(epd):
    logging.debug("Display clear")
    try:
        epd.init(0)
        epd.Clear(0xFF)
        epd.init(1)
        time.sleep(1)

    except IOError as e:
        logging.info(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def drawPicture(epd, picture):
    logging.debug("Display draw picture")
    try:
        epd.init(0)
        image = Image.open(os.path.join(picture))
        epd.display(epd.getbuffer(image))
        time.sleep(15)

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def shutdownDisplay(epd):
    logging.debug("Display shutdown")
    epd.init(0)
    epd.Clear(0xFF)
    epd.sleep()

def drawInitialDisplay(epd, background, backgroundmodified, font):
    logging.debug("Display draw initial display")
    try:
        updateDisplay(epd, 10, 10, 'PREN TEAM 33', background, backgroundmodified, font)
        updateDisplay(epd, 10, 30, '', background, backgroundmodified, font)

        updateDisplay(epd, 10, 80, 'Beanspruchte Zeit', background, backgroundmodified, font)
        updateDisplay(epd, 10, 100, '', background, backgroundmodified, font)

        updateDisplay(epd, 10, 150, 'Energieverbrauch', background, backgroundmodified, font)
        updateDisplay(epd, 10, 170, '', background, backgroundmodified, font)

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()

def updateDisplay(epd, x, y, text, backgroundBMP, backgroundModified, font):
    try:
        background = Image.open(os.path.join(backgroundModified))
        draw = ImageDraw.Draw(background)
        draw.rectangle((x, y, 200, y + 20), fill=0)
        newimage = background.crop([x, y, 200, y + 20])
        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        draw.rectangle((x, y, 200, y + 20), fill=(255, 255, 255))
        newimage = background.crop([x, y, 200, y + 20])
        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        fontdisplay = ImageFont.truetype(font, 16)

        draw.text((x, y), text, font=fontdisplay, fill=0)
        newimage = background.crop([x, y, 200, y + 20])

        background.paste(newimage, (x, y))
        epd.displayPart(epd.getbuffer(background))

        background.save("pic/background_modified.bmp")
        logging.debug("Display updated with text: " + text)

    except IOError as e:
        logging.error(e)

    except KeyboardInterrupt:
        logging.warning("ctrl + c:")
        epd1in54_V2.epdconfig.module_exit()
        exit()
