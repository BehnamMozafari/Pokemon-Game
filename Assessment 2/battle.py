from poke_team import PokeTeam


class Battle():

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        self.team_1 = PokeTeam(trainer_one_name)
        self.team_2 = PokeTeam(trainer_two_name)
        self.battle_mode = None

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
        # set battle mode to 0
        self.battle_mode = 0
        self.team_1.choose_team(self.battle_mode, None)
        self.team_2.choose_team(self.battle_mode, None)

        while self.team_1.team.__len__() >= 1 and self.team_2.team.__len__() >= 1:
            # set u1 as the first pokemon to fight from stack for team 1, same goes for team 2 with u2
            u1 = self.team_1.team.pop()
            u2 = self.team_2.team.pop()
            # if they have the same speed, attack at the same time
            if u1.get_speed() == u2.get_speed():
                # both defend
                u1.damage_after_attacked(u2)
                u2.damage_after_attacked(u1)
                if u1.get_hp() > 0 and u2.get_hp() > 0:
                    # lose 1 hp
                    u1.decrease_hp()
                    u2.decrease_hp()
                    if u1.get_hp() > 0 and u2.get_hp() > 0:
                        # if both survive, push them back to stack
                        self.team_1.team.push(u1)
                        self.team_2.team.push(u2)
                    elif u1.get_hp() > 0:
                        # if u1 survive, level up and push to stack
                        u1.update_level()
                        self.team_1.team.push(u1)
                    elif u2.get_hp() > 0:
                        # if u2 survive, level up and push to stack
                        u2.update_level()
                        self.team_2.team.push(u2)
                elif u1.get_hp() > 0:
                    # if u1 survive, level up and push to stack
                    u1.update_level()
                    self.team_1.team.push(u1)
                elif u2.get_hp() > 0:
                    # if u2 survive, level up and push to stack
                    u2.update_level()
                    self.team_2.team.push(u2)

            # if u1 has faster speed, u2 defend first
            if u1.get_speed() > u2.get_speed():
                u2.damage_after_attacked(u1)
                # if u2 is still alive, u2 attacks and then u1 defends
                if u2.get_hp() > 0:
                    u1.damage_after_attacked(u2)
                    # if both pokemon is alive, push them back to the array
                    if u1.get_hp() > 0:
                        u1.decrease_hp()
                        u2.decrease_hp()
                        self.team_1.team.push(u1)
                        self.team_2.team.push(u2)
                    # if u1 die after get attacked back u2, u2 levels up and add to the stack
                    else:
                        u2.update_level()
                        self.team_2.team.push(u2)
                # if u2 die after get attacked back u1, u1 levels up and add to the stack
                else:
                    u1.update_level()
                    self.team_1.team.push(u1)
            # else u2 attack u1 beacuse of faster speed
            else:
                # u1 defends attack from u2
                u1.damage_after_attacked(u2)
                # if u1 still alive, attacks u2
                if u1.get_hp() > 0:
                    # u2 defends u1 attack
                    u2.damage_after_attacked(u1)
                    # if u2 and u1 both still alive
                    if u2.get_hp() > 0:
                        # push them back to the stack
                        u1.decrease_hp()
                        u2.decrease_hp()
                        self.team_1.team.push(u1)
                        self.team_2.team.push(u2)
                    # if u2 die after get attacked back u1, u1 levels up and add to the stack
                    else:
                        u1.update_level()
                        self.team_2.team.push(u1)
                # if u1 die after get attacked back u2, u2 levels up and add to the stack
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
                    temp_1 = pokemon_1
                    self.team_1.team.append(temp_1)

                # If pokemon_2 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
                # alive after the decrease, get sent back to the end of the array or deleted if hp less than equal 0
                elif pokemon_2.get_hp() > 0:
                    pokemon_1.decrease_hp()
                    pokemon_2.decrease_hp()
                    temp_1 = pokemon_1
                    temp_2 = pokemon_2
                    if pokemon_1.hp > 0:
                        self.team_1.team.append(temp_1)
                    if pokemon_2.hp > 0:
                        self.team_2.team.append(temp_2)

            # Second check condition whether speed of pokemon_2 is larger than speed of pokemon_1:
            elif pokemon_1.get_speed() < pokemon_2.get_speed():
                # Calculate hp of pokemon_1 after attacked by pokemon_2
                pokemon_1.damage_after_attack(pokemon_2)

                # If pokemon_1 dies (hp<=0), pokemon_1 get deleted from the team
                # Pokemon_2 is levelled up, that pokemon_2 get brought to the end of the queue
                if pokemon_1.get_hp <= 0:
                    pokemon_2.update_level()
                    temp_2 = pokemon_2
                    self.team_2.team.append(temp_2)

                # If pokemon_1 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
                # alive after the decrease, get sent back to the end of the array or deleted if hp <= 0
                elif pokemon_1.get_hp > 0:
                    pokemon_2.decrease_hp()
                    pokemon_1.decrease_hp()
                    temp_2 = pokemon_2
                    temp_1 = pokemon_1
                    if pokemon_2.hp > 0:
                        self.team_2.team.append(temp_2)
                    if pokemon_1.hp > 0:
                        self.team_1.team.append(temp_1)

            # Third check condition: if the speed of pokemon_1 and pokemon_2 equals, calculate the hp after attack
            # Each pokemon hp is decreased by 1 as well
            # If ones hp <= 0, that pokemon get removed from the arraylist
            # If ones hp > 0, that pokemon get sent to the back of the queue
            elif pokemon_1.get_speed() == pokemon_2.get_speed():
                pokemon_2.damage_after_attacked(pokemon_1)
                pokemon_1.damage_after_attacked(pokemon_2)
                pokemon_1.decrease_hp()
                pokemon_2.decrease_hp()
                temp_1 = pokemon_1
                temp_2 = pokemon_2
                if pokemon_1.hp > 0:
                    self.team_1.team.append(temp_1)
                if pokemon_2.hp > 0:
                    self.team_2.team.append(temp_2)

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
