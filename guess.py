import random

# generate random number between 1 and 10
secret_num = random.randint(1, 10)

while True:
  # get guess from player
  guess = int(input("Guess a number between 1 and 10: "))
  # compare guess to computer number
  if guess == secret_num:
    print("You got it! My num was {}".format(secret_num))
    break
  else:
    print("That's not it!")
 
