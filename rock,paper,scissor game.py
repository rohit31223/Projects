rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
bro = input("what do you choose? type 0 for rock, 1 for paper and 2 for scissors\n ")
if bro == "0":
    print(rock)
elif bro == "1":
    print(paper)
elif bro == "2":
    print(scissors)
else:
    print("sorry")
import random
computer = [rock , paper , scissors]
rohit = random.choice(computer)
name = rohit
print(name)
if name == rock and bro == "0":
    print("draw")
elif name == paper and bro == "0":
    print("you lose")
elif name == scissors and bro == "0":
    print("you win")
elif name == rock and bro == "1":
    print("you win")
elif name == paper and bro =="1":
    print("Draw")
elif name == scissors and bro == "1":
    print("you lose")
elif name == rock and bro == "2":
    print("you lose")
elif name == paper and bro == "2":
    print("you win")
elif name == scissors and bro == "2":
    print("Draw")
else:
    print("GAME OVER TRY LATER")


