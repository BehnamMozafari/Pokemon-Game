""" PokeTeam class implementation.

Defines the PokeTeam class used to assemble a team.
"""

__author__ = "Behnam Mozafari, Zhongxun Pan, Nhu Nguyen"

from poke_team import PokeTeam


class Battle():

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        self.team_1 = PokeTeam(trainer_one_name)
        self.team_2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

    def set_mode_battle(self) -> str:
        self.battle_mode = 0
        self.team_1.choose_team(self.battle_mode, None)
        self.team_2.choose_team(self.battle_mode, None)

        while self.team_1.team.__len__() >= 1 and self.team_2.team.__len__() >= 1:
            u1 = self.team_1.team.pop()
            u2 = self.team_2.team.pop()
            if u1.get_speed() > u2.get_speed():
                u2.damage_after_attacked(u1)
                if u2.get_hp() > 0:
                    u1.damage_after_attacked(u2)
                    if u1.get_hp() > 0:
                        self.team_1.team.push(u1)
                        self.team_2.team.push(u2)
                    else:
                        u2.update_level()
                        self.team_2.team.push(u2)
                else:
                    u1.update_level()
                    self.team_1.team.push(u1)

            else:
                u1.damage_after_attacked(u2)
                if u1.get_hp() > 0:
                    u2.damage_after_attacked(u1)
                    if u2.get_hp() > 0:
                        self.team_1.team.push(u1)
                        self.team_2.team.push(u2)
                    else:
                        u1.update_level()
                        self.team_2.team.push(u1)
                else:
                    u2.update_level()
                    self.team_2.team.push(u2)

        if self.team_1.team.__len__() == self.team_2.team.__len__() == 0:
            return "DRAW"
        elif self.team_1.team.__len__() >= 1 and self.team_2.team.__len__() == 0:
            return self.team_1.team_name
        elif self.team_2.team.__len__() >= 1 and self.team_1.team.__len__() == 0:
            return self.team_2.team_name




    # Task 4: Using ADT Circular Queue for combat
    def rotating_mode_battle(self) -> str:
        # Create 2 teams, ask for their team names
        self.battle_mode = 1
        self.team_1.choose_team(self.battle_mode, None)
        self.team_2.choose_team(self.battle_mode, None)

        # Check whether the length of both team_1 and team_2 is at least 1
        while self.team_1.team.is_empty() == False and self.team_2.team.is_empty() == False:

            # Take the first/front Pokemon of each team ready to combat
            pokemon_1 = self.team_1.team.serve()
            pokemon_2 = self.team_2.team.serve()

            # First check condition whether speed of pokemon_1 is larger than speed of pokemon_2
            if pokemon_1.get_speed() > pokemon_2.get_speed():
                # Calculate hp of pokemon_2 after attacked by pokemon_1
                pokemon_2.damage_after_attacked(pokemon_1)

                # If pokemon_2 dies (hp<=0), pokemon_2 get deleted from the team
                # Pokemon_1 is levelled up, that pokemon_1 get brought to the end of the queue
                if pokemon_2.get_hp() <= 0:
                    pokemon_1.update_level()
                    self.team_1.team.append(pokemon_1)

                # If pokemon_2 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
                # alive after the decrease, get sent back to the end of the array or deleted if hp less than equal 0
                #  ~~~
                elif pokemon_2.get_hp() > 0:
                    pokemon_1.damage_after_attacked(pokemon_2)
                    if pokemon_1.get_hp() > 0 and pokemon_2.get_hp() > 0:
                        pokemon_1.decrease_hp()
                        pokemon_2.decrease_hp()
                        if pokemon_1.get_hp() > 0:
                            self.team_1.team.append(pokemon_1)
                        if pokemon_2.get_hp() > 0:
                            self.team_2.team.append(pokemon_2)
                    elif pokemon_1.get_hp() <= 0 and pokemon_2.get_hp() <= 0:
                        pass
                    elif pokemon_1.get_hp() <= 0 and pokemon_2.get_hp() > 0:
                        pokemon_1.update_level()
                        self.team_1.team.append(pokemon_1)
                    elif pokemon_2.get_hp() <= 0 and pokemon_1.get_hp() > 0:
                        pokemon_2.update_level()
                        self.team_2.team.append(pokemon_2)


            # Second check condition whether speed of pokemon_2 is larger than speed of pokemon_1:
            elif pokemon_1.get_speed() < pokemon_2.get_speed():
                # Calculate hp of pokemon_1 after attacked by pokemon_2
                pokemon_1.damage_after_attack(pokemon_2)

                # If pokemon_1 dies (hp<=0), pokemon_1 get deleted from the team
                # Pokemon_2 is levelled up, that pokemon_2 get brought to the end of the queue
                if pokemon_1.get_hp() <= 0:
                    pokemon_2.update_level()
                    self.team_2.team.append(pokemon_2)

                # If pokemon_1 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
                # alive after the decrease, get sent back to the end of the array or deleted if hp <= 0
                elif pokemon_1.get_hp() > 0:
                    pokemon_2.damage_after_attacked(pokemon_1)
                    if pokemon_1.get_hp() > 0 and pokemon_2.get_hp() > 0:
                        pokemon_1.decrease_hp()
                        pokemon_2.decrease_hp()
                        if pokemon_1.get_hp() > 0:
                            self.team_1.team.append(pokemon_1)
                        if pokemon_2.get_hp() > 0:
                            self.team_2.team.append(pokemon_2)
                    elif pokemon_1.get_hp() <= 0 and pokemon_2.get_hp() <= 0:
                        pass
                    elif pokemon_1.get_hp() <= 0 and pokemon_2.get_hp() > 0:
                        pokemon_1.update_level()
                        self.team_1.team.append(pokemon_1)
                    elif pokemon_2.get_hp() <= 0 and pokemon_1.get_hp() > 0:
                        pokemon_2.update_level()
                        self.team_2.team.append(pokemon_2)

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
                    if pokemon_1.get_hp() > 0:
                        self.team_1.team.append(pokemon_1)
                    if pokemon_2.get_hp() > 0:
                        self.team_2.team.append(pokemon_2)
                elif pokemon_1.get_hp() <= 0 and pokemon_2.get_hp() <= 0:
                    pass
                elif pokemon_1.get_hp() <= 0 and pokemon_2.get_hp() > 0:
                    pokemon_1.update_level()
                    self.team_1.team.append(pokemon_1)
                elif pokemon_2.get_hp() <= 0 and pokemon_1.get_hp() > 0:
                    pokemon_2.update_level()
                    self.team_2.team.append(pokemon_2)

        # If eventually both team is empty, print Draw to the console
        if self.team_1.team.is_empty() == True and self.team_2.team.is_empty() == True:
            return "Draw"
        else:
            # If team_1 has no pokemon left, print team_2 wins to the console
            if self.team_1.team.is_empty():
                return self.team_2.team_name
            # If team_2 has no pokemon left, print team_1 wins to the console
            elif self.team_2.team.is_empty():
                return self.team_1.team_name

if __name__ == '__main__':
    x  = Battle("AB","CD");
    print(x.rotating_mode_battle())