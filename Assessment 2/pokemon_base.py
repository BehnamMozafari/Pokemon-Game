""" PokemonBase class implementation:

    Define abstract methods, getters and setters for base of each Pokemon

"""

__author__ = "Nhu Nguyen"


from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Abstract class: PokemonBase"""
    hp: int = 0 
    level: int = 1


    def __init__(self, hp: int, level: int, poke_type: str) -> None:
        """Raise exception if hp is negative or level is less than equal 0
        Best and worst complexity: O(1)"""
        if hp < 0:
            raise ValueError("hp should not be negative")
        if level < 1:
            raise ValueError("level must be greater or equal to 1")
        self.hp = hp
        self.level = level
        self.poke_type = poke_type


    def lose_hp(self, lost_hp: int) -> None:
        """Check if hp is greater equal to 0
        Best and worst complexity: O(1)"""
        if lost_hp >= 0:
            self.hp = self.hp - lost_hp
        else:
            raise ValueError("ValueError exception thrown")

    """ Hp getter
        :complexity: best and worst case complexity of O(1)"""    
    def get_hp(self) -> int:
        return int(self.hp)

    """ Hp setter
        :complexity: best and worst case complexity of O(1)"""
    def set_hp(self, hp) -> None:
        self.hp = hp

    """ Level getter 
        :complexity: best and worst case complexity of O(1)"""
    def get_level(self) -> int:
        return self.level

    """ Level setter
        :complexity: best and worst case complexity of O(1)"""
    def update_level(self) -> None:
        self.level += 1

    """ Decrease hp by 1 function. 
        :complexity: best and worst case complexity of O(1)"""
    def decrease_hp(self) -> None:
        self.hp -= 1


    # Abstract method for name, speed, attack, defend, damage_after_attack
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_attack(self) -> int:
        pass

    @abstractmethod
    def get_defence(self) -> int:
        pass

    @abstractmethod
    def damage_after_attacked(self, Pokemonbase) -> int:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass



    def attack_calculation(self, another_pokemon):
        """Attack calculation based on poke type
        :complexity: best and worst case complexity O(1)"""
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



