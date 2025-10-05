# rock paper scissors game
import random
count = 0
lose = 0
game_played = 1
while True:
    user_choice =input("enter ur choice - (rock, paper,scissors ):  "  ).lower()
    possible_choices = ["rock", "paper","scissors"]
    computer_choice = random.choice(possible_choices)
    if user_choice not in possible_choices:
        print("Invalid syntax , enter  choice - (rock, paper,scissors )")
    if user_choice == computer_choice:
         print("sorry it is tied ,you and the computer both chose "+ computer_choice)

         
    elif user_choice == "rock":
         if computer_choice == "paper":
              print(f"sorry, you lost {computer_choice} beats {user_choice}")
              lose += 1
         else :
            if  computer_choice == "scissors":
              print(f" you Won {computer_choice} loses to {user_choice}")
              count += 1

    elif user_choice == "paper":
         if computer_choice == "rock":
              print(f" you win {computer_choice} loses to {user_choice}")
              count += 1
         else :
            if  computer_choice == "scissors":
              print(f" you lost {computer_choice} beats {user_choice}")
              lose += 1

    elif user_choice == "scissors":
         if computer_choice == "paper":
              print(f" you win {computer_choice} loses to {user_choice}")
              count += 1

         else :
            if  computer_choice == "rock":
              print(f" you lost {computer_choice} beats  {user_choice}")
              lose += 1

    play_again = input("do you want to play again (y/n): ").lower()
    if play_again  == "y":
        game_played += 1
        continue

    elif play_again != "y":
        print("you won this many times :", count , "times after playing it",game_played ,"times" )
        
        if count > lose:
            print("you did a good job here is your prize")
        if count < lose:
            print("you can do better in the next game")


        break
    
    
        
    


    
            
              
    

      



