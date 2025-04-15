print("WELCOME TO MY QUIZZ")
playing=input("DO you want to play the game ").lower()
if(playing!="yes"):
    print("exiting the game")
    quit()
print("COMPUTER QUIZZ")
correct=0
incorrect=0
print(" choose the options for the mcqs")
q1=input('''
Q1-What does CPU stand for?
    A. Central Process Unit
    B. Central Processing Unit
    C. Computer Personal Unit
    D. Control Processing Unit ''' ).lower()
if(q1=='b'):
    print(f"you choosed {q1}.your answer is corrrect")
    correct+=1
else:
    print(f"you choosed {q1}.your answer is wrong.The correct answer is B")
    incorrect+=1

q2=input('''
Q2-Which part of the computer is considered the "brain"?
    A. RAM
    B. Monitor
    C. CPU
    D. Hard Disk ''' ).lower()
if(q2=='c'):
    print(f"you choosed {q2}.your answer is corrrect")
    correct+=1
else:
    print(f"you choosed {q2}.your answer is wrong.The correct answer is C")
    incorrect+=1

q3=input('''
Q3-Which of these is an input device?
    A. Printer
    B. Monitor
    C. Keyboard
    D. Speaker ''' ).lower()
if(q3=='c'):
    print(f"you choosed {q3}.your answer is corrrect")
    correct+=1
else:
    print(f"you choosed {q3}.your answer is wrong.The correct answer is C")
    incorrect+=1

q4=input('''
Q4-What is the main function of RAM?
    A. Store files permanently
    B. Process data
    C. Temporarily store data being used
    D. Display output ''' ).lower()
if(q4=='c'):
    print(f"you choosed {q4}.your answer is corrrect")
    correct+=1
else:
    print(f"you choosed {q4}.your answer is wrong.The correct answer is C")
    incorrect+=1

q5=input('''
Q5-Which device is used to store large amounts of data permanently?
    A. RAM
    B. Hard Drive
    C. CPU
    D. Scanner ''').lower()
if(q5=='b'):
    print(f"you choosed {q5}.your answer is corrrect")
    correct+=1
else:
    print(f"you choosed {q5}.your answer is wrong.The correct answer is B")
    incorrect+=1

print("thanks for answering the quizz")
print(f" you got {correct} questions right and {incorrect} questions wrong")
if(correct>=3):
    print(f"you got {correct} questions right and your pass")
else:
    print(f"you got {incorrect} questions false and your fail")
percentage=(correct/5)*100
print(f"you got {percentage}% score")





