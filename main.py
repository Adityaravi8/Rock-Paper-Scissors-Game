

import random
 
wins = 0 
losses = 0
ties = 0
rounds = 0
games = 0
dec = ""
com_lst = ["Rock","Paper","Scissors"]

print("Welcome to Rock, Paper, Scissors.\nHere are the instructions:")
print("-First pick how many rounds you would like to do.You can quit at anytime by typing QUIT.") 
print("-Then you are given 3 options which are Rock,Paper,Scissors. You can type in the full word with a capital letter or full word without a capital letter but make sure to type the full word.") 
print("-The computer will then select one of the three options.\nObjective:") 
print("Your goal is to beat the computer by choosing an option that beats the computer.") 
print("Rock beats Scissors ,Scissors beat Paper, Paper beats Rock") 

while(dec != "No" and dec != "no" and dec != "N" and dec != "n"):
 
   ask2 = ""
   while type(ask2) != int:
      try:
          ask2 = int(input("\nHow many rounds would you like to play: "))
      except ValueError:
          print("You did not enter a number.")
   while(ask2 <= 0):
      print("Please enter a number that is greater than 0.")
      ask2 = int(input("How many rounds would you like to do?: "))
  
   ask = input("What choice will you pick Rock, Paper, Scissors?: ")
   while(ask != "QUIT" and ask != "Rock" and ask != "rock" and ask != "Paper" and ask != "paper" and ask != "Scissors" and ask != "scissors"):
      print("Please enter a valid answer.")
      ask = input("What choice will you pick Rock, Paper, Scissors?: ")
   while(ask != "QUIT" and ask2 != 0):
      comp = random.choice(com_lst)
      if(ask == "Rock" and comp == "Rock" or ask == "rock" and comp == "Rock"):
          rounds += 1
          ties += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have tied to the computer.")
      if(ask == "Rock" and comp == "Paper" or ask == "rock" and comp == "Paper"):
          losses += 1
          rounds += 1
          ask2 -= 1 
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have lost the round.")
      if(ask == "Rock" and comp == "Scissors" or ask == "rock" and comp == "Scissors"):
        rounds += 1
        wins += 1
        ask2 -= 1
        print("You chose",ask)
        print("The computer chose",comp)
        print("Therefore you have won the round.")
     
      if(ask == "Paper" and comp == "Paper" or ask == "paper" and comp == "Paper"):
          rounds += 1
          ties += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have tied the computer.")
       
      if(ask == "Paper" and comp == "Scissors" or ask == "paper" and comp == "Scissors"):
          rounds += 1 
          losses += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have lost the round.")
      if(ask == "Paper" and comp == "Rock" or ask == "paper" and comp == "Rock"):
          rounds += 1
          wins += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have won the round.")
      
    
        
      if(ask == "Scissors" and comp == "Scissors" or ask == "scissors" and comp == "Scissors"):
          rounds += 1
          ties += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have tied the computer.")
      if(ask == "Scissors" and comp == "Rock" or ask == "scissors" and comp == "Rock"):
          rounds += 1
          losses += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have lost the round.")
      if(ask == "Scissors" and comp == "Paper" or ask == "scissors" and comp == "Paper"):
          rounds += 1
          wins += 1
          ask2 -= 1
          print("You chose",ask)
          print("The computer chose",comp)
          print("Therefore you have won the round.")
      
      
      if(ask2 != 0):
          ask = input("What choice will you pick Rock, Paper, Scissors?: ")
          while(ask != "QUIT" and ask != "Rock" and ask != "rock" and ask != "Paper" and ask != "paper" and ask != "Scissors" and ask != "scissors"):
            print("Sorry, what you have seemed to enter is not a givin option\nPlease enter a option from above")
            ask = input("\nWhat would you like to pick?: ")
   dec = input("Would you like to play again?(Yes or No): ")
   while(dec != "Yes" and dec != "yes" and dec != "y" and dec != "No" and dec != "no" and dec != "n"):
      print("Enter a valid input.")
      dec = input("Would you like to play again?(Yes or No): ")
    
 
print("Rounds:",rounds)
print("Ties:",ties)
print("Losses:",losses)
print("Wins:",wins)
print("Games:",games)
