import random
import sys
import math


lower_limit = int(sys.argv[1])
upper_limit = int(sys.argv[2])
print(f"Hi, You have  to guess the number between {lower_limit} and {upper_limit}")
class RandomGame:
     def __init__(self):

        self.lower = lower_limit
        self.upper = upper_limit
        self.trials = int(math.pow((upper_limit-lower_limit), 0.5))
        self.rand = 0

     def random_number_generator(self):

        self.rand = random.randint(self.lower,self.upper)


     def guess_number(self):

        i = -10

        while self.trials > 0:

            i = int(input())

            if i>self.rand:
                print("Guess a little lower")
                self.trials=self.trials-1
                print(f"You have {self.trials} left")
            elif i<self.rand:
                print("Guess a little higher")
                self.trials = self.trials - 1
                print(f"You have {self.trials} left")

            else:
                print("Congratulations You've guessed the right number")
                break


play = RandomGame()
play.random_number_generator()
play.guess_number()
