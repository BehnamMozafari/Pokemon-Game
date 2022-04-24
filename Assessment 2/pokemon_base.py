from abc import ABC, abstractmethod


class PokemonBase(ABC):
    """Abstract class: PokemonBase"""
    GAME_LEVEL = 1

    def __init__(self, hp: int, poke_type: str) -> None:
        self.hp = hp
        self.poke_type = poke_type
        self.level = PokemonBase.GAME_LEVEL

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

    # Getter for name, speed and attack damage
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def get_attack_damage(self):
        pass

    # Damage calculating function when attacked by another Pokemon 
    def attack_calculation(self, another_pokemon):
        if self.get_poke_type() == "water":
            return another_pokemon.get_attack_damage * another_pokemon.EFFECTIVENESS_WATER
        if self.get_poke_type() == "fire":
            return another_pokemon.get_attack_damage * another_pokemon.EFFECTIVENESS_FIRE
        if self.get_poke_type() == "grass":
            return another_pokemon.get_attack_damage * another_pokemon.EFFECTIVENESS_GRASS

    def __str__(self) -> str:
        return str(self.get_name()) + "'s HP = " + str(self.hp) + " and level = " + str(self.level)
