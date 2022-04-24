__author__ = "Nhu Nguyen"


from pokemon_base import PokemonBase


class Charmander(PokemonBase):
    EFFECTIVENESS_FIRE = 1
    EFFECTIVENESS_WATER = 0.5
    EFFECTIVENESS_GRASS = 2

    def __init__(self) -> None:
        PokemonBase.__init__(self, 7, "Fire")
        self.name = "Charmander"
        self.speed = 7

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed + self.level

    def get_attack_damage(self):
        return 6 + self.level


class Bulbasaur(PokemonBase):
    EFFECTIVENESS_FIRE = 2
    EFFECTIVENESS_WATER = 1
    EFFECTIVENESS_GRASS = 0.5

    def __init__(self) -> None:
        PokemonBase.__init__(self, 9, "Grass")
        self.name = "Bulbasaur"
        self.speed = 7

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed + self.level // 2

    def get_attack_damage(self):
        return 5


class Squirtle(PokemonBase):
    EFFECTIVENESS_FIRE = 0.5
    EFFECTIVENESS_WATER = 2
    EFFECTIVENESS_GRASS = 1

    def __init__(self) -> None:
        PokemonBase.__init__(self, 8, "Water")
        self.name = "Squirtle"
        self.speed = 7

    def get_name(self):
        return self.name

    def get_speed(self):
        return self.speed

    def get_attack_damage(self):
        return 4 + self.level // 2
