""" PokemonBase class implementation:

    Define abstract methods, getters and setters for base of each Pokemon

"""

__author__ = "Nhu Nguyen"


from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Abstract class: PokemonBase"""
    hp: int = 0 
    level: int = 1

    """Raise exception if hp is negative or level is less than equal 0."""
    def __init__(self, hp: int, level: int, poke_type: str) -> None:
        """Best and worst complexity: O(1)"""
        if hp < 0:
            raise ValueError("hp should not be negative")
        if level < 1:
            raise ValueError("level must be greater or equal to 1")
        self.hp = hp
        self.level = level
        self.poke_type = poke_type

    """Check if hp is greater equal to 0"""
    def lose_hp(self, lost_hp: int) -> None:
        """Best and worst complexity: O(1)"""
        if lost_hp >= 0:
            self.hp = self.hp - lost_hp
        else:
            raise ValueError("ValueError exception thrown")

    """hp getter. Best and worst complexity: O(1)"""
    def get_hp(self):
        return int(self.hp)

    """hp setter. Best and worst complexity: O(1)"""
    def set_hp(self, hp):
        self.hp = hp

    """level getter. Best and worst complexity: O(1)"""
    def get_level(self):
        return self.level

    """level setter. Best and worst complexity: O(1)"""
    def update_level(self):
        self.level += 1

    """decrease hp by 1 function. Best and worst complexity: O(1)"""
    def decrease_hp(self):
        self.hp -= 1


    # Abstract method for name, speed, attack, defend, damage_after_attack
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
    def get_defence(self):
        pass

    @abstractmethod
    def damage_after_attacked(self, Pokemonbase): 
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


    """Attack calculation based on poke type"""
    def attack_calculation(self, another_pokemon):
        """Best and worst complexity: O(1)"""
        if self.poke_type == "water":
            water_damage = another_pokemon.get_attack() * another_pokemon.EFFECTIVENESS_WATER
            return water_damage 
        elif self.poke_type == "fire":
            fire_damage = another_pokemon.get_attack() * another_pokemon.EFFECTIVENESS_FIRE
            return fire_damage
        elif self.poke_type == "grass":
            grass_damage = another_pokemon.get_attack() * another_pokemon.EFFECTIVENESS_GRASS
            return grass_damage
        elif self.poke_type == "":
            return another_pokemon.get_attack()



