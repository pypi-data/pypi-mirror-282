import requests, json
from requests.structures import CaseInsensitiveDict
import logging
import logging.config
from os import path


#log_file_path = path.join(path.dirname(path.abspath(__name__)), 'logger.config')
#logging.config.fileConfig(log_file_path)
#logger = logging.getLogger("DataSend")

def checkAvailability(url):
    payload = {}
    headers = {}
    logging.info("Checking availability of " + url)
    response = requests.request("GET", url)
    if response.status_code == 200:
        logging.debug("checkAvailability" + response.content)
        return True
    else :
        logging.debug("checkAvailability" + response.content)
        return False


def sendStatus(url, token):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Auth"] = token
    resp  = requests.post(url, headers=headers)
    logging.debug("sendStatus" + str(resp.content))
    if resp.status_code == 204:
        logging.debug("sendStatus replied status OK")
        return True
    else:
        logging.debug("sendStatus something went wrong")
        return False


def sendData(url, token, config):
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    headers["Auth"] = token
    resp = requests.post(url, headers=headers, data=config)
    if resp.status_code == 204 or resp.status_code == 200 or resp.status_code == 201:
        logging.debug("sendData replied status OK")
        logging.info(resp.content)
        return True
    else:
        logging.error("sendData something went wrong")
        logging.error(resp.content)
        return False
