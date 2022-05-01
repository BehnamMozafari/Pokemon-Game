""" Battle class implementation.

Defines the Battle class used to conduct pokemon battles.
"""
__author__ = "Zhongxun Pan"

import random
from abc import ABC, abstractmethod
from pokemon_base import PokemonBase


class GlitchMon(ABC, PokemonBase):

    def __init__(self, hp: int, level: int) -> None:
        PokemonBase.__init__(self, hp, level, "fire")

    def increase_hp(self):
        self.hp += 1

    def superpower(self):
        n = random.randint(0, 2)
        if n == 0:
            self.level_up()
        elif n == 1:
            self.increase_hp()
        elif n == 2:
            self.level_up()
            self.increase_hp()


class MissingNo(GlitchMon):
    EFFECTIVENESS_FIRE = 1
    EFFECTIVENESS_WATER = 1
    EFFECTIVENESS_GRASS = 1

    def __init__(self):
        GlitchMon.__init__(self, int((7 + 8 + 9) / 3), 1)
        self.attack = int(((6 + self.level) + 5 + (4 + self.level // 2) / 3))
        self.speed = int(((7 + self.level) + (7 + self.level // 2) + 7) / 3)
        self.defence = int(((4 + 5 + (6 + self.level)) / 3))

    def level_up(self) -> None:
        self.hp += 1
        self.defence += 1
        self.speed += 1
        self.attack += 1

    def get_speed(self) -> int:
        return self.speed

    def get_attack(self) -> int:
        return self.attack

    def get_defence(self) -> int:
        return self.defence

    def defend(self, damage: int) -> None:
        if damage > self.defence:
            self.hp -= damage
        else:
            self.hp -= damage // 2

        n = random.randint(0, 3)
        if n == 2:
            self.superpower()

    def get_poke_type(self) -> str:
        return ""

    def __str__(self):
        return "MissingNo's hp = " + str(self.hp) + " and level = " + str(self.level)
