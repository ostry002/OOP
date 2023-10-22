class Alchemist:
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory, recipes):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic 
        self.__ranged = ranged 
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = recipes 

class Laboratory: 
    def __init__(self, potions, herbs, catalysts):
        self.__potions = potions 
        self.__herbs = herbs 
        self.__catalysts = catalysts
        
