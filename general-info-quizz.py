from ast import Continue


print("Welcome to General Information Quizz! ")

playing = input("Do you want to play? ")

if playing.lower() in ["yes" , "y"]:
    Continue
else:    
    quit()
    
print("Kudos! Lets start :D ")
score = 0 

answer = input("1-What is the name of our planetary system? ")
if answer.lower() == "solar system":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("2-What is the longest river in the world? ")
if answer.lower() == "nile":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("3-Who was the second founding father of United States? ")
if answer.lower() == "alexander hamilton":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

answer = input("4-What is the capital of Finland? ")
if answer.lower() == "helsinki":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("5-Who is next in line to the British throne after Queen Elizabeth II? ")
if answer.lower() == "prince charles":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("6-What is the biggest state in America? ")
if answer.lower() == "alaska":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
answer = input("7-What animal alive today is even bigger than a dinosaur? ")
if answer.lower() == "blue whale":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")                

answer = input("8-What's the best selling book of all time? ")
if answer.lower() == "the bible":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")    

answer = input("9-What is David Schwimmer's character's full name in Friends called? ")
if answer.lower() == "ross geller":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("10-Who was the forth US president to be assassinated? (last name only) ")
if answer.lower() == "kennedy":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")        
    
print("You got " + str(score) + " questions correct!")
print("Thats " + str((score / 10 ) * 100) + "%.")
