print("Hello, welcome to my quiz! \n\nIt'll be a trivia of facts about me, the creator. Good luck!")
score = 0

print("\n\nQuestion 1: Which is my favorite color? ")
color = str(input("\nChoose between 'red', 'blue', or 'yellow'. "))
color = color.lower()
if color == 'red':
    score= score +1
    print("Correct!")
elif color == 'blue':
    print("Wrong!")
elif color == 'yellow':
    print("Wrong!")
else:
    print("I'm sorry, I didn't catch that!")

print("\n\nQuestion 2: Which is my favorite animal? ")
animal = str(input("\nChoose between elephant, bird, or cat. "))
animal = animal.lower()
if animal == 'bird':
    score = score +1
    print("Correct!")
elif animal == 'elephant':
    print("Wrong!")
elif animal == 'cat':
    print("Wrong!")
else:
    print("I'm sorry, I didn't catch that!")

print("\n\nQuestion 3: Which food is my favorite? ")
food = str(input("\nChoose between 'sushi', 'pizza', or 'hamburger. "))
food = food.lower()
if food == 'pizza':
    score = score +1
    print("Correct!")
elif food == 'sushi':
    print("Wrong!")
elif food == 'hamburger':
    print("Wrong!")
else: 
    print("I'm sorry, I didn't catch that!")
    
print("That's all the questions!")
print("\nYour score is... " + str(score) + " out of 3! Thank you for playing!")
