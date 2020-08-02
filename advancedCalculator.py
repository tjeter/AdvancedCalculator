def askForNumberInput(numInput):
    #Define local variable
    convertedNumber = math.nan

    #Wait for valid numerical input 
    while True:
        number = input(numInput)
        try:
            #Try to typecast the input to a float
            float(number)
        except ValueError:
            #Catch the exception if it is not a number
            print("ERROR: Syn: Invalid Num")
        else:
            #Typecasting
            convertedNumber = float(number)
            break
    return convertedNumber

# Define Function Listing Function
def abilitiesList():
    print("+...Addition")
    print("-...Subtraction")
    print("*...Multiplication")
    print("/...Division")
    print("^...Powers")
    print("/-...Square Roots ")
    print("!...Factorials (Input Cannot Be Negetave)")
    print("Abs...Absolute Value")
    print("d/r...Degrees To Radians")
    print("r/d...Radians To Degrees")
    print("pi...Returns PI")
    print("e...Returs 'e'")
    print("tau...Returns TAU (2xPI)")
    print("M+...Save input to memory")
    print("MR...Recall Memory")
    print("M-...Clear Memory")
    print("sin...Sine")
    print("cos...Cosine")
    print("tan...Tangent")
    print("asin...Arc Sine")
    print("acos...Arc Cosine")
    print("atan...Arc Tangent")
    print("log10...Log(10) of Input")
    print("log...Returns The Apropriate Log of the Input (input1 is the log power)")
    print("rand...Returns A Random Number Between 0 and 1")
    print("randint...Returns A Random Number Between The Two Inputs")
    print("//////////////////////////////////////////////////////////////////////////")

# Import 'math' and 'random' Libraries
import math
import random

# Loop for getting operation
while True:
    operator = input("What operation do you want to perform? ")
    # Is operator == to any of out constants or predefines?
    if operator == "help":
        abilitiesList()
    elif operator == "pi":
        print(math.pi)
    elif operator == "e":
        print(math.e)
    elif operator == "tau":
        print(math.pi*2)
    elif operator == "MR":
        print(str(memStore))
    elif operator == "M-":
        memStore = "Empty"
        print("Memory Cleared")
    elif operator == "rand":
        print(random.random())
    # Has the user entered in a valid operator?
    elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^" or operator == "/-" or operator == "!" or operator == "Abs" or operator == "d/r" or operator == "r/d" or operator == "M+" or operator == "M-" or operator == "MR" or operator == "sin" or operator == "cos" or operator == "tan" or operator == "asin" or operator == "acos" or operator == "atan" or operator == "log10" or operator == "log" or operator == "randint":
        break
    else:
        print("ERROR: Invalid Operator")

# Loop for 1st number input
while True:
    number1 = askForNumberInput("First Number? ")
    # Catch asin and acos out of bounds error case
    if (operator == "asin" or operator == "acos") and (number1 > 1 or number1 < -1):
        print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
    elif operator == "!" and number1 < 0:
        print("ERROR: Math: Factorials only accept inputs > 0")
    else:
        break

# Does the operation require a 2nd input?
if not (operator=="/-" or operator=="!" or operator=="Abs" or operator=="d/r" or operator=="r/d" or operator=="M+" or operator=="sin" or operator=="cos" or operator=="tan" or operator=="asin" or operator=="acos" or operator=="atan" or operator=="log10"):
    # Loop for 2nd number input
    while True:
        number2 = askForNumberInput("Second Number? ")
        # Catch x/0 error case
        if  operator == "/" and number2 == "0":
            print("ERROR: Math: Canot divide by 0!")
        else:
            break

# Calculations
if operator == "+":
    output = number1 + number2
    print("Your Answer: "+str(output))
elif operator == "-":
    output = number1 - number2
    print("Your Answer: "+str(output))
elif operator == "*":
    output = number1 * number2
    print("Your Answer: "+str(output))
elif operator == "/":
    output = number1 / number2
    print("Your Answer: "+str(output))
elif operator == "^":
    output = math.pow(number1,number2)
    print("Your Answer: "+str(output))
elif operator == "/-":
    output = math.sqrt(number1)
    print("Your Answer: "+str(output))
elif operator == "!":
    output = math.factorial(number1)
    print("Your Answer: "+str(output))
elif operator == "Abs":
    output = math.fabs(number1)
    print("Your Answer: "+str(output))
elif operator == "d/r":
    output = math.radians(number1)
    print("Your Answer: "+str(output))
elif operator == "r/d":
    output = math.degrees(number1)
    print("Your Answer: "+str(output))
elif operator == "M+":
    memStore = number1
    print("Number Stored")
elif operator == "sin":
    output = math.sin(number1)
    print("Your Answer: "+str(output))
elif operator == "cos":
    output = math.cos(number1)
    print("Your Answer: "+str(output))
elif operator == "tan":
    output = math.tan(number1)
    print("Your Answer: "+str(output))
elif operator == "asin":
    output = math.asin(number1)
    print("Your Answer: "+str(output))
elif operator == "acos":
    output = math.acos(number1)
    print("Your Answer: "+str(output))
elif operator == "atan":
    output = math.atan(number1)
    print("Your Answer: "+str(output))
elif operator == "log10":
    output = math.log10(number1)
    print("Your Answer: "+str(output))
elif operator == "log":
    output = math.log(number2, number1)
    print("Your Answer: "+str(output))
elif operator == "randint":
    output = random.randint(number1, number2)
    print("Your Answer: "+str(output))
