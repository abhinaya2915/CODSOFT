import random
def determine_winner(user_option,computer_option):
   if user_option == computer_option:
      return "tie"
   elif (user_option == "rock" and computer_option == "scissors")or\
   (user_option == "scissors" and computer_option == "spaper")or\
   (user_option == "paper" and computer_option == "rock"):
      return "user"
   else:
      return "computer"
   
def display_result(user_option,computer_option,winner):
   print(f"You chose: {user_option}")
   print(f"Computer chose: {computer_option}")

   if winner == "tie":
      print("It's a tie!")
   elif winner == "user":
      print("You win this round!")
   else:
      print("Computer win this round!")
   

def play_game():
    choices = ["rock","paper","scissors"]
    user_score = 0
    computer_score = 0
    
    while True:
        print("Let's play Rock, Paper, Scissors! ")
        user_option = input("Enter your choice (rock,paper,scissors): ").lower()

        while user_option not in choices:
            print("Invalid input. Please try again.")
            user_option = input("Enter your choice (rock,paper,scissors): ").lower()
        computer_option = random.choice(choices)
        winner = determine_winner(user_option,computer_option)

        display_result(user_option , computer_option ,winner)
        if winner == "user":
           user_score+= 1
        elif winner == "computer":
           computer_score += 1
        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ").lower()

        if play_again != "yes":
           break  
    print("Thanks for playing!") 
play_game()
