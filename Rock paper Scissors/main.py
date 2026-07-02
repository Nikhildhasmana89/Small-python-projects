import random
computer = random.randint(0, 2)
you = input("Enter your choice (rock, paper, scissors): ").lower()
youDict = {"rock": 0, "paper": 1, "scissors": 2}
you = youDict.get(you)

print(f"Computer chose: {['rock', 'paper', 'scissors'][computer]}")
print(f"You chose: {['rock', 'paper', 'scissors'][you]}")

if you is None:
    print("Invalid input! Please enter rock, paper, or scissors.")
elif computer == you:
    print("It's a tie!")
elif (you == 0 and computer == 2) or (you == 1 and computer == 0) or (you == 2 and computer == 1):
    print("You win!")
else:
    print("Computer wins!")
    