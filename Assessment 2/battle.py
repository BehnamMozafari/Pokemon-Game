from poke_team import PokeTeam


class Battle():
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
                pokemon_1.get_attack()
                pokemon_2.get_defend() 

                if pokemon_2.hp <= 0: 
                    pokemon_2.serve()  
                    pokemon_1.update_level()
                    temp_1 = pokemon_1.serve() 
                    team_1.append(temp_1)


                elif pokemon_2.hp > 0: 
                    pokemon_1.hp -= 1  
                    pokemon_2.hp -= 1 
                    temp_1 = pokemon_1.serve()  
                    temp_2 = pokemon_2.serve()
                    if pokemon_1.hp > 0: 
                        team_1.append(temp_1)
                    if pokemon_2.hp > 0:  
                        team_2.append(temp_2)


                        
            elif pokemon_1.get_speed() < pokemon_2.get_speed(): 
                pokemon_2.get_attack()
                pokemon_1.get_defend() 

                if pokemon_1.hp <= 0: 
                    pokemon_1.serve()  
                    pokemon_2.update_level()
                    temp_2 = pokemon_2.serve() 
                    team_2.append(temp_2)

                elif pokemon_1.hp > 0: 
                    pokemon_2.hp -= 1  
                    pokemon_1.hp -= 1 
                    temp_2 = pokemon_2.serve()  
                    temp_1 = pokemon_1.serve()
                    if pokemon_2.hp > 0: 
                        team_2.append(temp_2)
                    if pokemon_1.hp > 0:  
                        team_1.append(temp_1)


            elif pokemon_1.get_speed() == pokemon_2.get_speed(): 
                pokemon_1.get_attack()
                pokemon_1.get_defend()  
                pokemon_2.get_attack()
                pokemon_2.get_defend() 
                pokemon_1.hp -= 1  
                pokemon_2.hp -= 1 
                temp_1 = pokemon_1.serve() 
                temp_2 = pokemon_2.serve()
                if pokemon_1.hp > 0: 
                    team_1.append(temp_1)
                if pokemon_2.hp > 0:  
                    team_2.append(temp_2)


        if team_1.is_empty() == True and team_2.is_empty() == True:  
            print("Draw")
        else: 
            if team_1.is_empty() == True: 
                print(team_1.team_name + " wins the battle")
            elif team_2.is_empty() == True: 
                print(team_2.team_name + " wins the battle")
