# -*- coding: utf-8 -*-

import logging
from pokemon import Pokemon

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def testPokemon():
    poke1 = Pokemon("Charmander")

    logger.info("Charmander toJSON: %s", Pokemon.toJson(poke1))

    poke1AsJson = '''{
        "name": "Charmander"
        }'''
    logger.info("Charmander fromJSON: %s", Pokemon.fromJson(poke1AsJson).name)


if __name__ == '__main__':
    testPokemon()