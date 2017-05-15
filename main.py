# -*- coding: utf-8 -*-

import logging
import json
import csv
import random
from pokemon import Pokemon



def generateList(teamSize):
    fullList = getPokemon()
    smallList = []
    for i in range(0, teamSize):
        randomNumber = random.randint(1, len(fullList))
        smallList.append(fullList[randomNumber])
    return smallList

def getPokemon():
    return getPokemonFromCsv('firstStageNoLeg.csv')

def getPokemonFromCsv(filename):
    pokeList = []
    pokeFile = open(filename, 'r')
    pokeReader = csv.reader(pokeFile)
    for pokemon in pokeReader:
        pokeList.append(pokemon)
    return pokeList

if __name__ == '__main__':
    #do stuff
    pokeList = generateList(3)
    for pokemon in pokeList:
        print(pokemon)