import time
import random

def main():

    print("""
    **************************
    *                        *
    *       Welcome to       *
    *   Password Generator   *
    *                        *
    *          v2.0          *
    *                        *
    *                        *
    *   [i] Intermediate     *
    *                        *
    *   [d] Difficult        *
    *                        * 
    *   [e] Expert           *
    *                        *
    *   [h] Help             *        *
    *                        *
    **************************
""")

    #creating a dictionary to store the acceptable values from the menu
    
    accDict = {"i": 0, "d": 0, "e": 0, "h": 0}

    #while loop validates user input by looping 'valInput' function until it returns true
    #when the user's input is in the correct format, the variable 'isValid' will turn to true


    isValid=False

    while isValid !=True:

        isValid, accDict = valInput(input("Enter Here: "), accDict)

                
    menu(accDict)


#menu will handle the results from the user's input and use 'match' 'case' statements 

def menu(accDict):
    choice = ""
    
    for x,y in accDict.items():
        if y == 1:
            choice = x

    match choice:
        case 'i':
            passW = genPass(10,False)
        case 'd':
            passW = genPass(20,False)
        case 'e':
            passW = genPass(30,True)
        case 'h':
            passW = helpScreen()

    print(f"""
       Your passowrd is :
       {passW} 

""")
    time.sleep(5)

    
    main()


#help screen displays message


def helpScreen():
    print("""

    **************************
    *                        *
    *       Welcome to       *
    *   Password Generator   *
    *                        *
    *          v2.0          *
    *                        *
    *                        *
    *   [r] Return Home      *
    *                        *
    *   This is a password   *
    *   generator made       * 
    *   by Luca, Thanks      *
    *                        *
    *                        *
    *                        *
    **************************
""")
    choice = ""

    i = input("Enter here :")
    accDict = {"r": 0}

    isValid, accDict = valInput(i,accDict)

    for x,y in accDict.items():
        print(x,y)
    if y == 1:
        main()
    else:
        helpScreen()



#genPass takes a desired password length and whether or not to use special characters and returns a random string


def genPass(passLen, useSpecial):

    randomCharacters = "OMyGEFrNIsKLBHqPQzUTSWVZfXaecdbYghujoimklADJwpvtxCR0123456789=-+_][}{'#;@~:.,/>?}{@|@{};.;']]'/..'@:?><"

    count = 0

    output = ""

    while count < passLen:
        
        if useSpecial == False:
            output = output + random.choice(randomCharacters[:35]) 

        if useSpecial == True:
            output = output + random.choice(randomCharacters) 

        count+=1
        

    return output

#valInput - is the function that will return a boolean representing the state of whether the user's input is valid
#         - it also returns an updated dictionary with the value increased, on which option the user selected


def valInput(menuChoice, acceptableList):

    count = 0
    
    if len(menuChoice) > 1:
        return False, acceptableList

    #updating the value in the dictionary (if the key matches)

    #using '.items' to obtain both the key and value when iterating through the dictionary then update them

    for x, y in acceptableList.items():
        
        if x == menuChoice:
            acceptableList.update({x: 1})
            count+=1
   
    #count only increases when the dictionary is updated meaning if there is an acceptable answer


    if count == 1:
        return True, acceptableList
    
    
    return False, acceptableList

main()
