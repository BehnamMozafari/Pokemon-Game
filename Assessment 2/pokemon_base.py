__author__ = "Nhu Nguyen"


from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Abstract class: PokemonBase"""
    hp: int = 0 
    level: int = 1 

    def __init__(self, hp: int, level: int) -> None:
        if hp < 0:
            raise ValueError("hp should not be negative")
        if level < 1:
            raise ValueError("level must be greater or equal to 1")
        self.hp = hp
        self.level = level

    def lose_hp(self, lost_hp: int) -> None:
        if lost_hp >= 0:
            self.hp = self.hp - lost_hp
        else:
            raise ValueError("ValueError exception thrown")


    def get_hp(self):
        return self.hp

    def set_hp(self, hp):
        self.hp = hp

    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

    def increase_hp(self):
        self.hp += 1


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



