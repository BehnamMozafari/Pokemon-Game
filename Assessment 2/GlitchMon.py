""" GlitchMon and MissingNo implementation.

Defines the Battle class used to conduct pokemon battles.
"""
__author__ = "Zhongxun Pan"

import random
from abc import ABC, abstractmethod
from pokemon_base import PokemonBase


class GlitchMon(ABC, PokemonBase):

    def __init__(self, hp: int, level: int) -> None:
        PokemonBase.__init__(self, hp, level, "")

    def increase_hp(self):
        self.hp += 1

    def superpower(self):
        n = random.randint(0, 2)
        if n == 0:
            self.update_level()
        elif n == 1:
            self.increase_hp()
        elif n == 2:
            self.update_level()
            self.increase_hp()


class MissingNo(GlitchMon):
    EFFECTIVENESS_FIRE = 1
    EFFECTIVENESS_WATER = 1
    EFFECTIVENESS_GRASS = 1

    def __init__(self):
        GlitchMon.__init__(self, int((7 + 8 + 9) / 3), 1)

    def get_name(self) -> str:
        return "MissingNo"

    def get_speed(self) -> int:
        return int((((7 + 1) + (7 + 1 // 2) + 7) / 3) + self.level)

    def get_attack(self) -> int:
        return int((((6 + 1) + 5 + (4 + 1 // 2)) / 3) + self.level)

    def get_defence(self) -> int:
        return int(((4 + 5 + (6 + 1)) / 3) + self.level)

    def defend(self, damage: int) -> None:
        rand = random.randint(0,2)
        if rand == 0:
            if damage > self.defence:
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif rand == 1:
            if damage > (self.defence + 5):
                self.hp -= damage
            else:
                self.hp -= damage // 2
        elif rand == 2:
            if damage > (self.defence * 2):
                self.hp -= damage
            else:
                self.hp -= damage // 2

        n = random.randint(0, 3)
        if n == 2:
            self.superpower()

    def __str__(self):
        return "MissingNo's hp = " + str(self.hp) + " and level = " + str(self.level)
