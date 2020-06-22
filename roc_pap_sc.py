import random 

print("""

 ____             __        ____                       
   / __ \____  _____/ /__     / __ \____ _____  ___  _____
  / /_/ / __ \/ ___/ //_/    / /_/ / __ `/ __ \/ _ \/ ___/
 / _, _/ /_/ / /__/ ,< _    / ____/ /_/ / /_/ /  __/ /  _ 
/_/ |_|\____/\___/_/|_( )  /_/    \__,_/ .___/\___/_/  ( )
                      |/              /_/              |/ 
   _____      _                              
  / ___/_____(_)_____________  __________    
  \__ \/ ___/ / ___/ ___/ __ \/ ___/ ___/    
 ___/ / /__/ (__  |__  ) /_/ / /  (__  )     
/____/\___/_/____/____/\____/_/  /____/      
                                             
             ____  __________________  __
            / __ )/  _/_  __/ ____/ / / /
           / __  |/ /  / / / /   / /_/ / 
          / /_/ // /  / / / /___/ __  /  
         /_____/___/ /_/  \____/_/ /_/   
                                         






    ____             ____                       __          
   / __ )__  ___    / __ )_________ _____  ____/ /___  ____ 
  / __  / / / (_)  / __  / ___/ __ `/ __ \/ __  / __ \/ __ \
 / /_/ / /_/ /    / /_/ / /  / /_/ / / / / /_/ / /_/ / / / /
/_____/\__, (_)  /_____/_/   \__,_/_/ /_/\__,_/\____/_/ /_/ 
      /____/                                                
 _       ___            __                   _ 
| |     / (_)___  _____/ /_____  ____     _ | |
| | /| / / / __ \/ ___/ __/ __ \/ __ \   (_)/ /
| |/ |/ / / / / (__  ) /_/ /_/ / / / /  _  / / 
|__/|__/_/_/ /_/____/\__/\____/_/ /_/  (_)/_/  
                                        /_/     





""")

class rock_paper_scissor():
        def paper_option(user_in):
                ai_in = random.randint(1,3)
                if ai_in == 2:
                        print("It's a tie! AI chose: Paper")
                elif ai_in == 1:
                        print("You win! AI chose: Rock")
                else:
                        print("You lose! AI chose: Scissors")   
        def scissor_option(user_in):
                ai_in = random.randint(1,3)
                if ai_in == 2:
                        print("You win! AI chose: Paper")
                elif ai_in == 1:
                        print("You lose! AI chose: Rock")
                else:
                        print("It's a tie! AI chose: Scissors")  

        def rock_option(user_in):
                ai_in = random.randint(1,3)
                if ai_in == 2:
                        print("You lose! AI chose: Paper")
                elif ai_in == 1:
                        print("Its a tie! AI chose: Rock")
                else:
                        print("You win! AI chose: Scissors")    



game_paper = rock_paper_scissor.paper_option
game_rock = rock_paper_scissor.rock_option
game_scissor = rock_paper_scissor.scissor_option

user_input = input("Rock, Paper, or Scissor: ")
paper = ["paper", 
         "Paper"]
rock = ["rock", 
        "Rock"]
scissor = ["scissor",
	  "Scissor"]

if user_input == rock[1]:
	game_rock(user_input)
if user_input == rock[0]:
        game_rock(user_input)
if user_input == paper[1]:
        game_paper(user_input)
if user_input == paper[0]:
        game_paper(user_input)
if user_input == scissor[1]:
        game_scissor(user_input)
if user_input == scissor[0]:
        game_scissor(user_input)
