import random
from .general_functions import display_choices, determine_winner

class Game:
    choices = ('r','p','s')
    yes_no_choices = ('y','n')

    def get_user_choice(self):
        while True:
            user_choice = input('Choose Rock, Paper or Scissor? (r/p/s): ').lower()
            if user_choice not in self.choices:
                print('Invalid choice!')
                continue
            else:
                return user_choice

    def play_game(self):
        while True:
            user_choice = self.get_user_choice()
            computer_choice = random.choice(self.choices)

            display_choices(user_choice, computer_choice)
            determine_winner(user_choice, computer_choice)

            should_continue = input('Continue? (y/n): ').lower()
            if should_continue not in self.yes_no_choices:
                print('Invalid option')
                break
            elif should_continue == 'n':
                break