__author__ = "Nhu Nguyen"

from pokemon_base import PokemonBase

"""Charmander class"""


class Charmander(PokemonBase):
    """Charmander type effectiveness"""
    EFFECTIVENESS_FIRE = 1
    EFFECTIVENESS_WATER = 0.5
    EFFECTIVENESS_GRASS = 2

    def __init__(self) -> None:
        PokemonBase.__init__(self, 7, 1)

    # Charmander name getter
    def get_name(self):
        return "Charmander"

    # Charmander speed getter
    def get_speed(self):
        return 7 + self.level

    # Charmander attack getter
    def get_attack(self):
        return 6 + self.level

    # Charmander defence getter
    def get_defence(self):
        return 7

    # Charmander calculate damage after attack
    def damage_after_attacked(self, another_pokemon: PokemonBase):
        damage = self.attack_calculation(another_pokemon)
        if damage > self.get_defence():
            self.hp -= damage
        else:
            self.hp -= damage // 2

    # Charmander poke type getter
    def get_poke_type(self) -> str:
        return "fire"

    # String printing
    def __str__(self) -> str:
        return "Charmander's HP = " + str(self.hp) + " and level = " + str(self.level)


"""Bulbasaur class"""


class Bulbasaur(PokemonBase):
    """Bulbasaur type effectiveness"""
    EFFECTIVENESS_FIRE = 2
    EFFECTIVENESS_WATER = 1
    EFFECTIVENESS_GRASS = 0.5

    def __init__(self) -> None:
        PokemonBase.__init__(self, 9, 1)

    # Bulbasaur name getter
    def get_name(self):
        return "Bulbasaur"

    # Bulbasaur speed getter
    def get_speed(self):
        return 7 + self.level // 2

    # Bulbasaur attack getter
    def get_attack(self):
        return 5

    # Bulbasaur defence getter
    def get_defence(self):
        return 5

    # Bulbasaur calculate damage after attack
    def damage_after_attacked(self, another_pokemon: PokemonBase):
        damage = self.attack_calculation(another_pokemon)
        if damage > self.get_defence():
            self.hp -= damage
        else:
            self.hp -= damage // 2

    # Bulbasaur poke type getter
    def get_poke_type(self) -> str:
        return "grass"

    # String printing
    def __str__(self) -> str:
        return "Bulbasaur's HP = " + str(self.hp) + " and level = " + str(self.level)


"""Squirtle class"""


class Squirtle(PokemonBase):
    """Squirtle type effectiveness"""
    EFFECTIVENESS_FIRE = 0.5
    EFFECTIVENESS_WATER = 2
    EFFECTIVENESS_GRASS = 1

    def __init__(self) -> None:
        PokemonBase.__init__(self, 8, 1)

    def get_name(self):
        return "Squirtle"

    def get_speed(self):
        return 7

    def get_attack(self):
        return 4 + self.level // 2

    def get_defence(self):
        return 6 + self.level

    def damage_after_attacked(self, another_pokemon: PokemonBase):
        damage = self.attack_calculation(another_pokemon)
        if damage > self.get_defence():
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def get_poke_type(self) -> str:
        return "water"

    def __str__(self) -> str:
        return "Squirtle's HP = " + str(self.hp) + " and level = " + str(self.level)
