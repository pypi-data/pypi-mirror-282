import json
from time import gmtime, strftime
import logging
import logging.config
from os import path

__cube = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: ""
}

log_file_path = path.join(path.dirname(path.abspath(__name__)), 'logger.config')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger("DataPreparation")

def setPos(int, value):
    logging.debug("Setting position " + str(int) + " to " + str(value))
    __cube[int] = str(value).lower()

def getPos(int):
    logging.debug("Getting position " + str(__cube[int]))
    return __cube[int]

def getjson():
    data = {"time": strftime("%Y-%m-%d %H:%M:%S", gmtime()),
            "config": {'1': getPos(1), '2': getPos(2), '3': getPos(3), '4': getPos(4), '5': getPos(5), '6': getPos(6),
                       '7': getPos(7), '8': getPos(8)}}
    logging.debug("Getting getjson " + str(data))
    return json.dumps(data)

def getconfig():
    data = {1: getPos(1), 2: getPos(2), 3: getPos(3), 4: getPos(4), 5: getPos(5), 6: getPos(6),
                       7: getPos(7), 8: getPos(8)}
    logging.debug("Getting config " + str(data))
    return json.dumps(data)