__author__ = "Nhu Nguyen"


from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Abstract class: PokemonBase"""
    hp: int = 0 
    level: int = 1

    """Raise exception if hp is negative or level is less than equal 0"""
    def __init__(self, hp: int, level: int) -> None:
        if hp < 0:
            raise ValueError("hp should not be negative")
        if level < 1:
            raise ValueError("level must be greater or equal to 1")
        self.hp = hp
        self.level = level

    """Check if hp is greater equal to 0"""
    def lose_hp(self, lost_hp: int) -> None:
        if lost_hp >= 0:
            self.hp = self.hp - lost_hp
        else:
            raise ValueError("ValueError exception thrown")

    """hp getter"""
    def get_hp(self):
        return self.hp
    """hp setter"""
    def set_hp(self, hp):
        self.hp = hp

    """level getter"""
    def get_level(self):
        return self.level

    """level setter"""
    def update_level(self):
        self.level += 1

    """increase hp by 1 function"""
    def increase_hp(self):
        self.hp += 1

    """decrease hp by 1 function"""
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
    def get_poke_type(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


    """Attack calculation based on poke type"""
    def attack_calculation(self, another_pokemon):
        if self.get_poke_type() == "water":
            water_damage = another_pokemon.get_attack() * another_pokemon.EFFECTIVENESS_WATER
            return water_damage 
        if self.get_poke_type() == "fire":
            fire_damage = another_pokemon.get_attack() * another_pokemon.EFFECTIVENESS_FIRE
            return fire_damage
        if self.get_poke_type() == "grass":
            grass_damage = another_pokemon.get_attack() * another_pokemon.EFFECTIVENESS_GRASS
            return grass_damage



