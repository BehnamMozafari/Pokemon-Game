__author__ = "Zhongxun Pan"

import random
from abc import ABC, abstractmethod


class GlitchMon(ABC):
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

    def get_hp(self) -> int:
        return self.hp

    def level_up(self) -> None:
        self.level += 1

    def get_level(self) -> int:
        return self.level

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
    def defend(self, damage: int) -> None:
        n = random.randint(0, 3)
        if n == 2:
            self.superpower()

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

    @abstractmethod
    def get_poke_type(self) -> str:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class MissingNo(GlitchMon):

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
        return self.speed

    def get_defence(self) -> int:
        return self.defence

    def defend(self, damage: int) -> None:
        if damage > self.defence:
            self.hp -= damage
        else:
            self.hp -= damage // 2

    def get_poke_type(self) -> str:
        return "MissingNo"

    def __str__(self):
        return "MissingNo's hp = " + str(self.hp) + " and level = " + str(self.level)
