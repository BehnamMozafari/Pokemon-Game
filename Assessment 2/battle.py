from poke_team import PokeTeam
from pokemon_base import attack_calculation 


class Battle():
    def rotating_mode_battle(self) -> str:
        team_1 = PokeTeam() 
        team_1.choose_team(1, None)
        team_2 = PokeTeam()
        team_2.choose_team(1, None)
        pokemon_1 = team_1.front
        pokemon_2 = team_2.front 
        if pokemon_1.get_speed() > pokemon_2.get_speed():
            pokemon_1.get_attack()
            pokemon_2.get_defend() 
            if pokemon_2.hp <= 0: 
                pokemon_2.serve()  
                pokemon_1.update_level()
                temp_1 = pokemon_1.serve() 
                team_1.append(temp_1)
            elif pokemon_2.hp > 0: 
                pokemon_1.get_defend() 
                pokemon_2.get_attack() 
                if (pokemon_1.hp<0 and pokemon_2.hp>0) or (pokemon_1>0 and pokemon_2.hp<0): 




                      

            if pokemon_2.hp > 0:
                if pokemon_1.hp <= 0: 
                    pokemon_2.get_level() + 1;
                elif pokemon_2.hp > 0: 



                temp_1 = pokemon_1.serve() 
                team_1.append(temp_1)
                temp_2 = pokemon_2.serve() 
                team_2.append(temp_2)

        elif pokemon_1.get_speed() < pokemon_2.get_speed(): 
            pokemon_1.get_defend()
            pokemon_2.get_attack()  



