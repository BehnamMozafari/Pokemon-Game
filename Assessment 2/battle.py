from poke_team import PokeTeam

class Battle():

    def __init__(self, trainer_one_name: str, trainer_two_name: str) -> None:
        self.team_1 = PokeTeam.__init__(trainer_one_name)
        self.team_2 = PokeTeam.__init__(trainer_two_name)
        self.battle_mode = None

    def set_mode_battle(self) -> str:
        team1_name = input("Trainer one name: ")
        team2_name = input("Trainer two name: ")
        self.__init__(team1_name, team2_name)
        self.battle_mode = 0
        self.team_1.choose_team(self.battle_mode, None)
        self.team_2.choose_team(self.battle_mode, None)

        while self.team_1.team.__len__() >= 1 and self.team_2.team.__len__() >= 1:
            u1: object = self.team_1.team.pop()
            u2: object = self.team_2.team.pop()
            if u1.get_speed() > u2.get.speed():
                u2.damage_after_attacked(u1.get_attack())
                if u2.get_hp() > 0:
                    u1.damage_after_attacked(u2.get_attack())
                    if u1.get_hp() > 0:
                        self.team_1.push(u1)
                        self.team_2.push(u2)
                    else:
                        u2.update_level()
                        self.team_2.push(u2)
            else:
                u1.damage_after_attacked(u2.get_attack())
                if u1.get_hp() > 0:
                    u2.damage_after_attacked(u1.get_attack())
                    if u2.get_hp() > 0:
                        self.team_1.push(u1)
                        self.team_2.push(u2)
                    else:
                        u1.update_level()
                        self.team_2.push(u1)
        if self.team_1.team.__len__() == self.team_2.team.__len__() == 0:
            return "DRAW"
        elif self.team_1.team.__len__() >= 1 and self.team_2.team.__len__() == 0:
            return "TEAM 1 WIN"
        elif self.team_2.team.__len__() >= 1 and self.team_1.team.__len__() == 0:
            return "TEAM 2 WIN"


    # Task 4: Using ADT Circular Queue for combat
    def rotating_mode_battle(self) -> str:
        # Create 2 teams, ask for their team names
        team_1 = PokeTeam()
        team_1.choose_team(1, None)
        team_1.team_name = input("What is your team name, team 1?")

        team_2 = PokeTeam()
        team_2.choose_team(1, None)
        team_1.team_name = input("What is your team name, team 2?")


        # Check whether the length of both team_1 and team_2 is at least 1
        while team_1.is_empty() == False or team_2.is_empty() == False:

            # Take the first/front Pokemon of each team ready to combat
            pokemon_1 = team_1.front
            pokemon_2 = team_2.front

            # First check condition whether speed of pokemon_1 is larger than speed of pokemon_2
            if pokemon_1.get_speed() > pokemon_2.get_speed():
                #Calculate hp of pokemon_2 after attacked by pokemon_1
                pokemon_2.damage_after_attack(pokemon_1.get_attack())

                # If pokemon_2 dies (hp<=0), pokemon_2 get deleted from the team
                # Pokemon_1 is levelled up, that pokemon_1 get brought to the end of the queue
                if pokemon_2.get_hp() <= 0:
                    pokemon_2.serve()
                    pokemon_1.update_level()
                    temp_1 = pokemon_1.serve()
                    team_1.append(temp_1)

                # If pokemon_2 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
                # alive after the decrease, get sent back to the end of the array or deleted if hp less than equal 0
                elif pokemon_2.get_hp() > 0: 
                    pokemon_1.decrease_hp()
                    pokemon_2.decrease_hp()
                    temp_1 = pokemon_1.serve()  
                    temp_2 = pokemon_2.serve()
                    if pokemon_1.hp > 0:
                        team_1.append(temp_1)
                    if pokemon_2.hp > 0:
                        team_2.append(temp_2)

            # Second check condition whether speed of pokemon_2 is larger than speed of pokemon_1:
            elif pokemon_1.get_speed() < pokemon_2.get_speed():
                # Calculate hp of pokemon_1 after attacked by pokemon_2
                pokemon_1.damage_after_attack(pokemon_2.get_attack())

                # If pokemon_1 dies (hp<=0), pokemon_1 get deleted from the team
                # Pokemon_2 is levelled up, that pokemon_2 get brought to the end of the queue
                if pokemon_1.get_hp <= 0:
                    pokemon_1.serve()
                    pokemon_2.update_level()
                    temp_2 = pokemon_2.serve()
                    team_2.append(temp_2)

                # If pokemon_1 is alive after the attack, both pokemon's hp is decreased by 1. Whichever pokemon is
                # alive after the decrease, get sent back to the end of the array or deleted if hp <= 0
                elif pokemon_1.get_hp > 0:
                    pokemon_2.decrease_hp()
                    pokemon_1.decrease_hp()
                    temp_2 = pokemon_2.serve()
                    temp_1 = pokemon_1.serve()
                    if pokemon_2.hp > 0:
                        team_2.append(temp_2)
                    if pokemon_1.hp > 0:
                        team_1.append(temp_1)

            # Third check condition: if the speed of pokemon_1 and pokemon_2 equals, calculate the hp after attack
            # Each pokemon hp is decreased by 1 as well
            # If ones hp <= 0, that pokemon get removed from the arraylist
            # If ones hp > 0, that pokemon get sent to the back of the queue
            elif pokemon_1.get_speed() == pokemon_2.get_speed(): 
                pokemon_2.damage_after_attack(pokemon_1.get_attack())
                pokemon_1.damage_after_attack(pokemon_2.get_attack()) 
                pokemon_1.decrease_hp()
                pokemon_2.decrease_hp()
                temp_1 = pokemon_1.serve() 
                temp_2 = pokemon_2.serve()
                if pokemon_1.get_hp > 0:
                    team_1.append(temp_1)
                if pokemon_2.get_hp > 0:
                    team_2.append(temp_2)

        # If eventually both team is empty, print Draw to the console
        if team_1.is_empty() == True and team_2.is_empty() == True:
            return "Draw"
        else:
            # If team_1 has no pokemon left, print team_2 wins to the console
            if team_1.is_empty():
                return team_2.team_name + " wins the battle"
            # If team_2 has no pokemon left, print team_1 wins to the console
            elif team_2.is_empty():
                return team_1.team_name + " wins the battle"
