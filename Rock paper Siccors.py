import random

choices = ['Rock','Paper','Siccors']
print('Welcome to Rock,Papers,Siccors!')
player = input('Choose your weapon: ')
random = random.choice(choices)
if player == 'Rock' and random == 'Paper':
        print ('The Computer Wins! Try Again')
elif player == 'Paper' and random == 'Siccors':
        print ('The Computer Wins! Try Again')
elif player == 'Siccors' and random == 'Rock':
        print ('The Computer Wins! Try Again')
elif player == 'Paper' and random == 'Rock':
        print ('You Win! Congratulations!')
elif player == 'Siccors' and random == 'Paper':
        print ('You Win! Congratulations!')
elif player == 'Rock' and random == 'Siccors':
        print ('You Win! Congratulations!')
elif player == 'Rock' and random == 'Rock':
        print ('Its a Tie!!!')
elif player == 'Siccors' and random == 'Siccors':
        print ('Its a Tie!!!')
elif player == 'Paper' and random == 'Paper':
        print ('Its a Tie!!!!')
else:
        print('Invalid Input. Please try again')
        