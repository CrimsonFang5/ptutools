# -*- coding: utf-8 -*-

import logging
import json

logger = logging.getLogger(__name__)

class Pokemon:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fromJson(jsonString):
        logger.debug('jsonString=%s', jsonString)
        itemList = json.loads(jsonString)
        logger.debug('itemList = %s', itemList)
        name = ""
        try:
            name = itemList["name"]
        except:
            # do something
            print("Could not load pokemon from json")
        retVal = Pokemon(name)
        return retVal

    @staticmethod
    def toJson(poke):
        pokeJson = {
            "name": poke.name
            }
        jsonString = json.dumps(pokeJson)
        return jsonString
