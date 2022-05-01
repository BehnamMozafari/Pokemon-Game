""" Battle class implementation.

Defines the Battle class used to conduct pokemon battles.
"""

__author__ = "Behnam Mozafari, Zhongxun Pan, Nhu Nguyen"

from poke_team import PokeTeam


class Battle:

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        self.team1 = PokeTeam(trainer_one_name)
        self.team2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def create_teams(self, criterion_team1: str = None, criterion_team2: str = None) -> None:
        self.team1.choose_team(self.battle_mode, criterion_team1)
        self.team2.choose_team(self.battle_mode, criterion_team2)

    def pokemon_lvlup(self, pokemon, pokemon_team, dead_pokemon_index, dead_pokemon_team):
        pokemon.update_level()
        if self.battle_mode == 0:
            pokemon_team.team.push(pokemon)
        elif self.battle_mode == 1:
            pokemon_team.team.append(pokemon)
        else:
            dead_pokemon_team.team.delete_at_index(dead_pokemon_index)

    def attack_defend(self, team1, pokemon_1, pokemon_1_index, team2, pokemon_2, pokemon_2_index):
        # pokemon_1 attacks pokemon_2
        # Calculate hp of pokemon_2 after attacked by pokemon_1
        pokemon_2.damage_after_attacked(pokemon_1)
        # If pokemon_2 dies (hp<=0), pokemon_2 get deleted from the team, Pokemon_1 is levelled up
        if pokemon_2.get_hp() <= 0:
            self.pokemon_lvlup(pokemon_1, team1, pokemon_2_index, team2)
        # If pokemon_2 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
        # alive after the decrease, get deleted if hp less than equal 0
        elif pokemon_2.get_hp() > 0:
            pokemon_1.damage_after_attacked(pokemon_2)
            if pokemon_1.get_hp() > 0:
                pokemon_1.decrease_hp()
                pokemon_2.decrease_hp()
                if pokemon_1.get_hp() > 0 and pokemon_2.get_hp() > 0:
                    if self.battle_mode == 0:
                        self.team1.team.push(pokemon_1)
                        self.team2.team.push(pokemon_2)
                    elif self.battle_mode == 1:
                        self.team1.team.append(pokemon_1)
                        self.team2.team.append(pokemon_2)
                elif pokemon_2.get_hp() > 0:
                    self.pokemon_lvlup(pokemon_2, team2, pokemon_1_index, team1)
                elif pokemon_1.get_hp() > 0:
                    self.pokemon_lvlup(pokemon_1, team1, pokemon_2_index, team2)
            elif pokemon_1.get_hp() <= 0:
                self.pokemon_lvlup(pokemon_2, team2, pokemon_1_index, team1)

    def conduct_battle(self) -> str:
        # Check whether the length of both team1 and team2 is at least 1
        while self.team1.team.is_empty() is False and self.team2.team.is_empty() is False:

            # Take the first Pokemon of each team ready to combat for each different battle mode
            pokemon_1_index = len(self.team1.team) - 1
            pokemon_2_index = len(self.team2.team) - 1
            if self.battle_mode == 0:
                pokemon_1 = self.team1.team.pop()
                pokemon_2 = self.team2.team.pop()
            elif self.battle_mode == 1:
                pokemon_1 = self.team1.team.serve()
                pokemon_2 = self.team2.team.serve()
            else:
                pokemon_1 = self.team1.team[pokemon_1_index].value
                pokemon_2 = self.team2.team[pokemon_2_index].value

            # First check condition whether speed of pokemon_1 is larger than speed of pokemon_2
            if pokemon_1.get_speed() > pokemon_2.get_speed():
                self.attack_defend(self.team1, pokemon_1, pokemon_1_index, self.team2, pokemon_2, pokemon_2_index)

            # Second check condition whether speed of pokemon_2 is larger than speed of pokemon_1:
            elif pokemon_1.get_speed() < pokemon_2.get_speed():
                self.attack_defend(self.team2, pokemon_2, pokemon_2_index, self.team1, pokemon_1, pokemon_1_index)

            # Third check condition: if the speed of pokemon_1 and pokemon_2 equals, calculate the hp after attack
            # Each pokemon hp is decreased by 1 if they both alive
            # If ones hp <= 0, that pokemon get removed from the arraylist
            # If ones hp > 0, that pokemon get sent to the back of the queue
            elif pokemon_1.get_speed() == pokemon_2.get_speed():
                pokemon_2.damage_after_attacked(pokemon_1)
                pokemon_1.damage_after_attacked(pokemon_2)
                if pokemon_1.get_hp() > 0 and pokemon_2.get_hp() > 0:
                    pokemon_1.decrease_hp()
                    pokemon_2.decrease_hp()
                    if pokemon_1.get_hp() > 0 and pokemon_2.get_hp() > 0:
                        self.team1.team.append(pokemon_1)
                        self.team2.team.append(pokemon_2)
                    elif pokemon_2.get_hp() > 0:
                        self.pokemon_lvlup(pokemon_2, self.team2, pokemon_1_index, self.team1)
                    elif pokemon_1.get_hp() > 0:
                        self.pokemon_lvlup(pokemon_1, self.team1, pokemon_2_index, self.team2)
                elif pokemon_2.get_hp() > 0:
                    self.pokemon_lvlup(pokemon_2, self.team2, pokemon_1_index, self.team1)
                elif pokemon_1.get_hp() > 0:
                    self.pokemon_lvlup(pokemon_1, self.team1, pokemon_2_index, self.team2)

        # If eventually both team is empty, print Draw to the console
        if self.team1.team.is_empty() == True and self.team2.team.is_empty() == True:
            return "Draw"
        # If team1 has no pokemon left, print team2 wins to the console
        elif self.team1.team.is_empty():
            return self.team2.team_name
        # If team2 has no pokemon left, print team1 wins to the console
        elif self.team2.team.is_empty():
            return self.team1.team_name

    def set_mode_battle(self) -> str:
        """
            this method which asks the user for input and sets up the
            players’ teams in such an order where a pokemon fights until it faints. It is here where
            you set the team’s battle mode to 0. This method should not take any arguments.
            This method returns the name of the player that wins the battle, Draw otherwise

            NOTE: The order of the Pokemon in this battle mode MUST be Charmanders ->
            Bulbasaurs -> Squirtles


            An example of a set mode battle would be the following:
            Team 1: C1 C2 B1 B2 S1
            Team 2: B1 B2 S1
            Round 1: Team 1’s C1 faints Team 2’s B1
            Round 2: Team 1’s C1 faints Team 2’s B2
            Round 3: Team 1’s C1 is fainted by Team 2’s S1
            Round 4: Team 1’s C2 is fainted by Team 2’s S1
            Round 5: Team 1’s B1 faints Team 2’s S1
        """
        self.battle_mode = 0
        self.create_teams(None, None)
        # conducting battle
        return self.conduct_battle()

    # Task 4: Using ADT Circular Queue for combat
    def rotating_mode_battle(self) -> str:
        # setting battle mode
        self.battle_mode = 1
        self.create_teams(None, None)
        # conducting battle
        return self.conduct_battle()

    def optimised_mode_battle(self, criterion_team1: str, criterion_team2: str) -> str:
        # set battle mode, create 2 teams
        self.battle_mode = 2
        self.create_teams(criterion_team1, criterion_team2)
        # conducting battle
        return self.conduct_battle()


if __name__ == '__main__':
    x = Battle("AB", "CD");
    print(x.rotating_mode_battle())
