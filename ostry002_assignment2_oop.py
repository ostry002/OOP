'''
File: ostry002_assignment2_oop.py
Description: Implementing the behaviour of an alchemist who is owned by a laboratory
Author: Roger Osterdahl
StudentID: 110410137
EmailID: ostry002
This is my own work as defined by the University's Academic Misconduct Policy.
'''
class Alchemist:
    """
    A class representing an Alchemist

    Attributes
    ----------
    attack: int

    strength: int

    magic: int

    ranged: int

    necromancy: int

    laboratory: Laboratory

    recipes: {}

    Methods
    -------
    getLaboratory(self): Laboratory
      Return the Laboratory instance associated with the Alchemist.

    getRecipes(self): List
      Returns a list of available potion recipes.

    mixPotion(self, recipe: str):
      Mixes a potion based on the recipe using the laboratory's functionality.

    drinkPotion(self, potion: Potion) -> str:
      Alchemist can drink a potion, increasing their attribute according to the potion's functionality.

    collectReagent(self, reagent: Reagent, amount: int):
      Adds a reagent to the alchemist's laboratory.

    refineReagents(self):
      Refines all herbs and catalysts in the laboratory, augmenting their quality and potency. 

    """
    def __init__(self, attack, strength, defense, magic, ranged, necromancy, laboratory, recipes):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic 
        self.__ranged = ranged 
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = []
    
    def getLaboratory():
        return Laboratory

    def getReceipes(self):
        return self.__recipes
    
    def mixPotion(self, recipe):
        """Making an object in which I am calling the Laboratory class with proper arguments - Composition."""
        self.objLaboratory = Laboratory(recipe, self)      

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        """Making an object in which I am calling the Laboratory class with proper arguments - Composition."""
        self.objLaboratory = Laboratory(reagent, amount)  
    
    def refineReagents(self):
        pass

class Laboratory: 
    """
    A class representing a laboratory

    Attributes
    ----------
    potions: []

    herbs: []

    catalysts: []

    Methods
    -------
    mixPotion(self, name: str, type: str, stat: str, primaryIngredient: str, secondaryIngredient: str)
        Mixes a potion based on the specified ingredients and their attributes. 

    addReagent(self, reagent: Reagent, amount: int):
        Adds a reagent (herb or catalyst) to the laboratory with the specified amount.
    """

    def __init__(self, potions, herbs, catalysts):
        self.__potions = potions 
        self.__herbs = herbs 
        self.__catalysts = catalysts
    
    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        """Creating a method in which I am mixing the first and second ingredients of a potion together."""
        pass

    def addReagent(self, reagent, amount):
        pass

class Potion: 
    """
    A class representing the potion

    Attributes
    ----------
    name: str

    stat: str

    boost: float

    Methods
    -------
    calculateBoost(self):
        Calculates and returns the attribute boost that the potion provides.

    getName(self):
        Acquires the name of the potion.

    getStat(self):
        Acquires the stat (attribute) that the potion affects.

    getBoost(self):
        Acquires the boost value of the potion.

    setBoost(self, boost: float):
        Sets the boost value of the potion to a value.
    """
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat 
        self.__boost = boost
    
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name
    
    def getStat(self):
        return self.__stat
    
    def getBoost(self):
        return self.__boost
    
    def setBoost(self):
        pass

class Reagent:
    """
    A class representing the reagent 

    Attributes
    ----------
    name: str

    potency: float

    Methods
    -------
    refine(self):
        Refines the reagent depending on the type used.

    getName(self):
        Returns the name of the reagent.

    getPotency(self):
        Returns the potency value of the reagent.

    setPotency(self, potency):
        Sets the potency value of the reagent to a value. 
    """
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency 
    
    def refine(self):
        pass

    def getName(self):
        return self.__name
    
    def getPotency(self):
        return self.__potency 
    
    def setPotency(self):
        pass 

class SuperPotion(Potion):
    """
    A class representing the super potion which inherits from the Potion class.

    Attributes
    ----------
    herb: Herb

    catalyst: Catalyst

    Methods
    -------
    calculateBoost(self):
      Calculates and returns the attribute boost of the super potion.
    
    getHerb(self):
      Returns the name of the herb.

    getCatalyst(self):
       Returns the name of the catalyst.
    """
    def __init__(self, name, stat, boost, herb, catalyst):
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst 
    
    def calculateBoost(self):
        return super().calculateBoost()
    
    def getHerb(self):
        return self.__herb 
    
    def getCatalyst(self):
        return self.__catalyst 

class ExtremePotion(Potion):
    """
    A class representing the extreme potion, which inherits from the Potion class.

    Attributes
    ----------
    reagent: Reagent

    potion: Potion

    Methods
    -------
    calculateBoost(self):
      Calculates and returns the attribute boost of the extreme potion.
    
    getReagent(self):
      Returns the name of the reagent.

    getPotion(self):
       Returns the name of the potion.
    """
    def __init__(self, name, stat, boost, reagent, potion):
        super().__init__(name, stat, boost)
        self.__reagent = reagent 
        self.__potion = potion 

    def calculateBoost(self):
        return super().calculateBoost()
    
    def getReagent(Reagent):
        return Reagent
    
    def getPotion(Potion):
        return Potion

class Herb(Reagent):
    """
    A class representing the herb, which inherits from the Reagent class.

    Attributes
    ----------
    grimy (bool) = True

    Methods
    -------
    refine(self):
      Refines the herb.

    setGrimy(self, grimy):
      Sets the grimy of the herb to a value.

    getGrimy(self):
      Returns whether the herb is grimy (True) or not (False).
    """
    def __init__(self, name, potency, grimy):
        super().__init__(name, potency)
        self.__grimy = grimy 

    def refine(self):
        return super().refine()

    def getGrimy(self):
        return self.__grimy 
    
    def setGrimy(self):
        pass

class Catalyst(Reagent):
    """
    A class representing the catalyst, which inherits from the Reagent class.

    Attributes
    ----------
    quality: float

    Methods
    -------
    refine(self):
      Refines the catalyst.

    getQuality(self):
      Returns the quality of the catalyst. 
    """
    def __init__(self, name, potency, quality):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        return super().refine()
    
    def getQuality(self):
        return self.__quality 


