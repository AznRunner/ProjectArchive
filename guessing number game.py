import random

count = 0
random = random.randint(0, 100)

while count >= 0:
   guess = int(input('Give a guess: '))
   if guess == random:
         print("You have guessed correctly!! Congratulations!!!")
         break
   elif guess > random:
         print("Your guess is too high. Try again")
         count += 1
   elif guess < random:
         print("Your guess is too low. Try again")
         count += 1
   else:
        print ("That is not a number. Try again")

print('It took you ' + str(count) + ' guesses to get it right')   

        
      