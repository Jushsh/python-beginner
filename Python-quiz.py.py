print("welcome to my quiz!")

playing = input("do you want to play? ")
score = 0

if playing.lower() != "yes":
  quit()

print("okay let start!")
answer = input('What does cpu stand for? ')
if answer.lower() == "central processing unit":
  print("correct")
  score += 1
else:
  print("incorrect")

answer = input('What does NYU stand for? ')
if answer.lower() == "new york university":
  print("correct")
  score += 1
else:
  print("incorrect")

answer = input('What does PP stand for? ')
if answer.lower() == "phnom penh":
  print("correct")
  score += 1
else:
  print("incorrect")
print("You got " +  str(score)  + " question correct!")
print("You got " +  str((score/3)  * 100) + " %.")