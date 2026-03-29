def display_choices(user_choice, computer_choice):
    print(f'Your choice was {user_choice}')
    print(f'Computer choice was {computer_choice}')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Its a Tie')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 'p' and computer_choice == 'r') or
        (user_choice == 's' and computer_choice == 'p')):
        print('You win')
    else:
        print('You loose')