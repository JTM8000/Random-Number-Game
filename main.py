import random
#import random module
#the magic number project
#use for/while loops
#numeric and boolean variable
#learn to use random number generation 
#learn to use breaks

#fixed number to test program



#create function to ask user for number
#pass variables as a parameter within the function 
def ask_number(nb_min,nb_max):
    #What is the magic number (between 1 and 10) ?
    #return int
    #no error management
    
    #number_str = input(f"What is the magic number (between {nb_min} and {nb_max}? ")
    #formatted string needs f in front of it
    number_int = 0
    while number_int == 0:
        number_str = input(f"What is the magic number (between {nb_min} and {nb_max}? ")
        #to solve infinite error loop, make sure input line is inside while loop
        try:
            number_int = int(number_str)
        
        except:
            print("ERROR: You must enter a number. Please try again")
        else:
            if number_int < nb_min or number_int > nb_max:
                print("Error: You must enter a number between 1 and 10.")
                number_int = 0 #returns to the loop
        
    return number_int

MIN_NUMBER = 1
MAX_NUMBER = 10
MAGIC_NUMBER = random.randint(MIN_NUMBER, MAX_NUMBER)
NB_LIVES = 4


#conditions 
#test user input against magic number
#3 conditions
#the magic number is greater
#the magic number is lower
#you won


# number = ask_number(MIN_NUMBER, MAX_NUMBER)
# if number == MAGIC_NUMBER:
#     print("You Won!")
# elif number > MAGIC_NUMBER:
#     print("You Lose. The Magic nuumber is less!")
# else:
#     print("You lose! The Magic Number is greater!")
    
#add while loop to have user guess magic number
# while not number ==  MAGIC_NUMBER:
#     number = ask_number(MIN_NUMBER, MAX_NUMBER)
#     if number == MAGIC_NUMBER:
#         print("You Won!")
#     elif number > MAGIC_NUMBER:
#         print("You Lose. The Magic nuumber is less!")
#     else:
#         print("You lose! The Magic Number is greater!")

#manage invalid entry // look at function try/except
# number = 0
# lives = NB_LIVES

# while not number ==  MAGIC_NUMBER and lives > 0:
#     print(f"You have {lives} lives")
#     number = ask_number(MIN_NUMBER, MAX_NUMBER)
#     if number == MAGIC_NUMBER:
#         print("You Won!")
#     elif number > MAGIC_NUMBER:
#         print("You Lose. The Magic nuumber is less!")
#         lives -= 1
#     else:
#         print("You lose! The Magic Number is greater!")
#         lives -= 1
        
        
# if lives <= 0:        
#     print(f"You lost! The magic number was: {MAGIC_NUMBER}")

win = False
for i in range (0, NB_LIVES):
    lives = NB_LIVES - i
    print(f"You have {lives} lives")
    number = ask_number(MIN_NUMBER, MAX_NUMBER)
    if number == MAGIC_NUMBER:
        print("You Won!")
        win = True
        break
    elif number > MAGIC_NUMBER:
        print("The Magic nuumber is less!")
    else:
        print("The Magic Number is greater!")
     
        
if not win:        
    print(f"You lost! The magic number was: {MAGIC_NUMBER}")
