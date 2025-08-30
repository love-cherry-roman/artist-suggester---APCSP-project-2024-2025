import os
from itertools import islice

speed = ["speed", "slow", "med-slow", "medium", "fast", "very fast"]
instruments = ["instruments","piano", "drums", "guitar", "woodwind", "string", "electronic"]
bass = ["bass", "low", "medium", "high", "extreme"]
mood = ["mood", "sad", "angry", "happy", "other"]
energy = ["energy", "low", "medium", "high", "extreme"]
vocals = ["vocals", "none", "singing", "rapping/lighter singing", "storytelling", "other/mix"]

categories = [speed, instruments, bass, mood, energy, vocals]


def ask_questions():
    answers = []
    for category in categories:
        print("-----------------------------------")
        #gets the input from the user
        print("What " + str(category[0]) + " do you prefer? ")
        for index, choice in enumerate(category[1:]):
            print(str(index + 1) + ": " + choice)
        answer = int(input("Answer: "))
        print("You picked: " + category[answer])
        answers.append(answer)
    print(answers)
    return answers
    
def suggestion_calculator(total):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("-----------------------------------")
    #prints result
    with open('lnswerkey.txt') as I:
        if (total[0] in [1, 2]) and (total[1] in [1, 2, 3]):
            print("You might enjoy artists like: \n")
            for line1 in islice(I, 1, 6): 
                print(line1.strip())
                
        if (total[0] in [1, 2]) and (total[1] in [4, 5, 6]):
            print("You might enjoy artists like: \n")
            for line1 in islice(I, 8, 13): 
                print(line1.strip())
                
        if (total[0] == 3 ) and (total[1] in [1, 2, 3]): 
            print("You might enjoy artists like: \n") 
            for line3 in islice(I, 15, 20): 
                print(line3.strip())
                
        if (total[0] == 3 ) and (total[1] in [4, 5, 6]):
            print("You might enjoy artists like: \n")  
            for line4 in islice(I, 22, 27): 
                print(line4.strip())
                
        if (total[0] in [4, 5] ) and (total[1] in [1, 2, 3]):
            print("You might enjoy artists like: \n")  
            for line4 in islice(I, 29, 34): 
                print(line4.strip())
                
        if (total[0] in [4, 5] ) and (total[1] in [4, 5, 6]):
            print("You might enjoy artists like: \n")  
            for line4 in islice(I, 36, 41): 
                print(line4.strip())
    #print resukt
    with open('lnswerkey.txt') as II:
        if (total[2] in [1, 2]) and (total[3] in [1,2]):
            for line1 in islice(II, 45, 50): 
                print(line1.strip())
                
        if (total[2] in [3, 4]) and (total[3] in [1,2]):
            for line1 in islice(II, 52, 57): 
                print(line1.strip())
                
        if (total[2] in [1, 2]) and (total[3] in [3, 4]):  
            for line3 in islice(II, 59, 64): 
                print(line3.strip())
                
        if (total[2] in [3, 4]) and (total[3] in [3, 4]):  
            for line4 in islice(II, 66, 71): 
                print(line4.strip())
    #print result
    with open('lnswerkey.txt') as III:
        if (total[4] in [1, 2]) and (total[5] in [1, 2]):
            for line1 in islice(III, 75, 80): 
                print(line1.strip())
                
        if (total[4] in [1, 2]) and (total[5] in [3]):
            for line1 in islice(III, 82, 87): 
                print(line1.strip())
                
        if (total[4] in [1, 2]) and (total[5] in [4,5]):  
            for line3 in islice(III, 89, 94): 
                print(line3.strip())
                
        if (total[4] in [3, 4]) and (total[5] in [1, 2]):  
            for line4 in islice(III, 96, 101): 
                print(line4.strip())
                
        if (total[4] in [3, 4] ) and (total[5] in [3]):  
            for line4 in islice(III, 103, 108): 
                print(line4.strip())
                
        if (total[4] in [3, 4]) and (total[5] in [4, 5]):  
            for line4 in islice(III, 110, 115): 
                print(line4.strip())

result = ask_questions()
suggestion_calculator(result)

# islice from itertools module and os module are created by python