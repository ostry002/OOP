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

class Potion: 
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat 
        self.__boost = boost

class Reagent:
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency 

class SuperPotion(Potion):
    def __init__(self, herb, catalyst):
        self.__herb = herb
        self.__catalyst = catalyst 

class ExtremePotion(Potion):
    def __init__(self, reagent, potion):
        self.__reagent = reagent 
        self.__potion = potion 

class Herb(Reagent):
    def __init__(self, grimy):
        self.__grimy = grimy 

class Catalyst(Reagent):
    def __init__(self, quality):
        self.__quality = quality
