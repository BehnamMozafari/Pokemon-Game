from poke_team import PokeTeam
from pokemon_base import attack_calculation 

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

    def rotating_mode_battle(self) -> str:

        team_1 = PokeTeam()
        team_1.choose_team(1, None)
        team_1.team_name = input("What is your team name, team 1?")

        team_2 = PokeTeam()
        team_2.choose_team(1, None)
        team_1.team_name = input("What is your team name, team 2?")

        pokemon_1 = team_1.front
        pokemon_2 = team_2.front

        while team_1.is_empty() == False or team_2.is_empty() == False: 
            if pokemon_1.get_speed() > pokemon_2.get_speed():
                pokemon_2.damage_after_attack(pokemon_1.get_attack())

                if pokemon_2.get_hp() <= 0:
                    pokemon_2.serve()
                    pokemon_1.update_level()
                    temp_1 = pokemon_1.serve()
                    team_1.append(temp_1)

                elif pokemon_2.get_hp() > 0: 
                    pokemon_1.decrease_hp()
                    pokemon_2.decrease_hp()
                    temp_1 = pokemon_1.serve()  
                    temp_2 = pokemon_2.serve()
                    if pokemon_1.hp > 0:
                        team_1.append(temp_1)
                    if pokemon_2.hp > 0:
                        team_2.append(temp_2)


                        
            elif pokemon_1.get_speed() < pokemon_2.get_speed(): 
                pokemon_1.damage_after_attack(pokemon_2.get_attack())

                if pokemon_1.get_hp <= 0:
                    pokemon_1.serve()
                    pokemon_2.update_level()
                    temp_2 = pokemon_2.serve()
                    team_2.append(temp_2)

                elif pokemon_1.get_hp > 0:
                    pokemon_2.decrease_hp()
                    pokemon_1.decrease_hp()
                    temp_2 = pokemon_2.serve()
                    temp_1 = pokemon_1.serve()
                    if pokemon_2.hp > 0:
                        team_2.append(temp_2)
                    if pokemon_1.hp > 0:
                        team_1.append(temp_1)


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

        if team_1.is_empty() == True and team_2.is_empty() == True:
            print("Draw")
        else:
            if team_1.is_empty() == True:
                print(team_1.team_name + " wins the battle")
            elif team_2.is_empty() == True:
                print(team_2.team_name + " wins the battle")
