""" PokeTeam class implementation.

Defines the PokeTeam class used to assemble a team.
"""

__author__ = "Behnam Mozafari"

from stack_adt import ArrayStack
from queue_adt import CircularQueue
from array_sorted_list import ArraySortedList
from pokemon import Charmander, Bulbasaur, Squirtle


class PokeTeam:
    """ Class for assembling a team of Pokemon. """

    def __init__(self, team_name: str) -> None:
        self.team = None
        self.team_name = team_name
        self.battle_mode = 0
        self.limit = 6
        self.criterion = None

    def choose_team(self, battle_mode: int, criterion: str = None) -> None:
        """ Initialises team ADT, Asks for user to input team, calls assign_team method
        :param battle_mode: the desired battle mode, either 0, 1 or 2
        :param  criterion: attribute used to order team in Optimised Mode Battle
        :raises ValueError: if battle_mode is not 0, 1 or 2, or if criterion is not 'lvl', 'hp', 'atk', 'def' or 'spd'
        :complexity:
        """
        battle_modes = [0, 1, 2]
        possible_criterions = ['lvl', 'hp', 'atk', 'def', 'spd']
        if battle_mode not in battle_modes:
            raise ValueError("Invalid Battle Mode\n")
        if criterion not in possible_criterions:
            raise ValueError("Invalid Criterion\n")

        self.battle_mode = battle_mode
        if self.battle_mode == 0:
            self.team = ArrayStack(self.limit)
        elif self.battle_mode == 1:
            self.team = CircularQueue(self.limit)
        else:
            self.team = ArraySortedList(self.limit)

        team_prompt = "Howdy Trainer! Choose your team as C B S\nwhere C is the number of Charmanders\n      B is the" \
                      " number of Bulbasaurs\n      S is the number of Squirtles\n"
        correct_input = False
        while not correct_input:
            try:
                team_input = input(team_prompt).split()
                charm = int(team_input[0])
                bulb = int(team_input[1])
                squir = int(team_input[2])
                self.assign_team(charm, bulb, squir)
            except ValueError:
                print("Please enter a valid team\n")
            else:
                correct_input = True

    def assign_team(self, charm: int, bulb: int, squir: int) -> None:
        """ Populating the team based on the battle mode
        :param charm: number of Charmanders
        :param bulb: number of Bulbasaurs
        :param squir: number of Squirtles
        :raises ValueError: if total number of Pokemon is greater than the limit or if a negative number is input
        :complexity:
        """
        if charm + bulb + squir > self.limit:
            raise ValueError("Number of Pokemon exceeds limit\n")
        if charm < 0 or bulb < 0 or squir < 0:
            raise ValueError("Number of Pokemon cannot be negative\n")

        if self.battle_mode == 0:
            for _ in range(squir):
                squirtle = Squirtle()
                self.team.push(squirtle)
            for _ in range(bulb):
                bulbasaur = Bulbasaur()
                self.team.push(bulbasaur)
            for _ in range(charm):
                charmander = Charmander()
                self.team.push(charmander)
        elif self.battle_mode == 1:
            for _ in range(charm):
                charmander = Charmander()
                self.team.append(charmander)
            for _ in range(bulb):
                bulbasaur = Bulbasaur()
                self.team.append(bulbasaur)
            for _ in range(squir):
                squirtle = Squirtle()
                self.team.append(squirtle)
        else:


    def __str__(self) -> str:
        """ String representation of PokeTeam
        """
        output = ""
        team_length = len(self.team)
        if self.battle_mode == 0:
            for i in range(team_length):
                current_pokemon = self.team.item_at_index(team_length - 1 - i)
                output += str(current_pokemon)
                if i != team_length - 1:
                    output += ", "
            return output
        elif self.battle_mode == 1:
            for i in range(team_length):
                current_pokemon = self.team.item_at_index(i)
                output += str(current_pokemon)
                if not i == team_length - 1:
                    output += ", "
            return output
        else:
            pass
