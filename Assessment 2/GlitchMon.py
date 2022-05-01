""" GlitchMon and MissingNo implementation.

Defines the Battle class used to conduct pokemon battles.
"""
__author__ = "Behnam Mozafari, Zhongxun Pan, Nhu Nguyen"

import random
from abc import ABC

from pokemon_base import PokemonBase


class GlitchMon(PokemonBase):
    """GlitchMon class is an Abstract class, which also inherits PokemonBase"""

    def __init__(self, hp: int, level: int) -> None:
        PokemonBase.__init__(self, hp, level, "")

    def increase_hp(self):
        """This method increase hp level by 1"""
        """Best and worst complexity: O(1)"""
        self.hp += 1

    def superpower(self):
        """This method gives random chance to choose 1 of 3 effects: gain 1 level, gain 1 hp, gain 1 hp and 1 level """
        """Best and worst complexity: O(1)"""
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
        """get_name method returns the name of MissingNo pokemon
        :complexity: Best and worst complexity: O(1)
        """
        return "MissingNo"

    def get_speed(self) -> int:
        """get_speed method takes the average of 3 defined pokemon speed formula and average them to get the formula
        for MissingNo speed"""
        """Best and worst complexity: O(1)"""
        return int((((7 + 1) + (7 + 1 // 2) + 7) / 3) + self.level)

    def get_attack(self) -> int:
        """get_attack method takes the average of 3 defined pokemon attack formula and average them to get the formula
        for MissingNo attack"""
        """Best and worst complexity: O(1)"""
        return int((((6 + 1) + 5 + (4 + 1 // 2)) / 3) + self.level)

    def get_defence(self) -> int:
        """get_defence method takes the average of 3 defined pokemon defence formula and average them to get the formula
        for MissingNo defence"""
        """Best and worst complexity: O(1)"""
        return int(((4 + 5 + (6 + 1)) / 3) + self.level)

    def damage_after_attacked(self, another_pokemon: PokemonBase) -> None:
        """defend method: creates probability 25% chance everytime Pokemon has to defend from an attack"""
        """Best and worst complexity: O(1)"""
        damage = self.attack_calculation(another_pokemon)
        n = random.randint(0, 3)
        if n == 2:
            self.superpower()
        else:
            rand = random.randint(0, 2)
            if rand == 0:
                if damage > self.get_defence():
                    self.hp -= damage
                else:
                    self.hp -= damage // 2
            elif rand == 1:
                if damage > (self.get_defence() + 5):
                    self.hp -= damage
                else:
                    self.hp -= damage // 2
            elif rand == 2:
                if damage > (self.get_defence() * 2):
                    self.hp -= damage
                else:
                    self.hp -= damage // 2

    def __str__(self):
        """String statement returns Charmander HP and its level"""
        """Best and worst complexity: O(1)"""
        return "MissingNo's HP = " + str(self.hp) + " and level = " + str(self.level)
