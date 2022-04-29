__author__ = "Nhu Nguyen"


from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Abstract class: PokemonBase"""

    def __init__(self, hp: int, poke_type: str) -> None:
        self.hp = hp
        self.poke_type = poke_type
        self.level = 1

    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def get_poke_type(self):
        return self.poke_type


    # Getter for name, speed, attack, defend, damage_after_attack
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def get_attack(self):
        pass

    @abstractmethod
    def get_name(self):
        pass 

    @abstractmethod
    def get_defend(self):
        pass

    @abstractmethod
    def damage_after_attacked(self): 
        pass 


    # Damage calculating function when attacked by another Pokemon 
    def attack_calculation(self, another_pokemon):
        if self.get_poke_type() == "water":
            water_damage = another_pokemon.get_attack * another_pokemon.EFFECTIVENESS_WATER
            return water_damage 
        if self.get_poke_type() == "fire":
            fire_damage = another_pokemon.get_attack * another_pokemon.EFFECTIVENESS_FIRE
            return fire_damage
        if self.get_poke_type() == "grass":
            grass_damage = another_pokemon.get_attack * another_pokemon.EFFECTIVENESS_GRASS
            return grass_damage


    # String return function 
    def __str__(self) -> str:
        return str(self.get_name()) + "'s HP = " + str(self.hp) + " and level = " + str(self.level)

