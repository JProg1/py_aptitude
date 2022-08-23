# Candidate ID 6843335 - James Cotton

# importing math for factorial function and trunc function
import math

# seperator used for formatting to easily see when we have removed to the next test
def print_seperator():
    print('#######################')
    pass

# First Factorial function
# Get factorial from user input, expected whole number. Will output forumla on user request if includeFormula is set as true
def first_factorial(num, includeFormula = False):
    formula = ''
    if includeFormula:
        formula = '('
        # save a repeat value we can edit
        _num = int(num)
        # get factorial calulcations via loop while removing 1 each time, until we get to 2, where we add on the final 1 after and correct the string formatting (adding a bracket and equals)
        # Calculations could be added here in an alterative to using the math library.
        while int(_num) >= 2:
            # build string by adding onto it the next number in the squence
            formula += str(_num) + ' * '
            _num-=1
            pass
        formula+= '1) = '
        pass

    # get the actual factorial from the inputted number
    factorial = math.factorial(int(num))

    return formula + str(factorial)

# Time conversion (whole number* to H:M - *user entered)
def time_convert(to_convert):
    # calculate the hours by dividing the input by 60, and removing decimal places via math.trunc
    hours = math.trunc(to_convert/60)
    # caclulate minutes by removing the amount of hours determinted above (60 x hours) 
    minutes = to_convert - (60 * hours)
    # print result
    return str(hours) + ':' + str(minutes)

# Consonant Count function. Returns amount of consonants in a string, not prepared to handle for punctation or spaces as per input criteria
def consonant_count(sentence):
    # List of vowels to compare, and can count as consonant if not a vowel
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    # Get input from user to search for consonants, and lower it to allow for comparing to array of lowercase vowels
    sentence = sentence.lower()
    # Loop through sentence for comparison to vowels, if not a match of either, then it should be a consonant/blank space based on input critera.
    for x in sentence:
        if x not in vowels:
            count += 1
    return count

# Hamming Distance (Count differences between two items in an array)
def h_distance(array):
    # using a count to comapre to other item
    count = 0
    # define hamming so we can return the result
    hamming = 0
    for x in list(array[0]):
        if x != list(array[1])[count]:
            hamming+=1
        count+=1
    return hamming

# Roman Numbers function - return Roman Numbers str from whole number
def roman_numbers(num):
    # I'm using an array that maps numbers to the relevant roman numberals where they change based on number.
    roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
    # saving variable to add to as we build the roman numberal
    result = ''

    # loop while number is more than 0
    while num > 0: 
        # run through array map and get variables
        for n, l in roman_map:
            # If the number is a more or equal to the number relating to the letter in the array, progress to add it to the result
            while num >= n:
                # Add the roman numeral to the result
                result += l
                # remove the number relating to the letter as we have added it to the result
                num -= n
    return result

# start the execution cycle to allow for test variables.
def test():
    # Factorial
    print_seperator()
    print('First Factorial - Enter number to return factorial of it')
    # ask if formula is wanted
    includeFormula = False
    if input('Include formula? y/n: ') == 'y':
        includeFormula = True

    print('Result:', first_factorial(input('Enter number: '), includeFormula))
    print_seperator()

    # Convert Time
    print('Enter a whole number to return hours and minutes in H:M format')
    print('Result:', time_convert(int(input('Enter number: '))))
    print_seperator()

    # Consonant Count
    print('Consonant Count - Enter string to return consonant count')
    print('Result:', consonant_count(input('Enter sentence: ')))
    print_seperator()

    # Hammming Distance
    print('Enter two items to count the differences (Hamming Distance)')
    # Get variables for the array (Expected numbers that are equal length as per input critera)
    print('Result:', h_distance(
        [input('Enter array item 1: '), input('Enter array item 2: ')]))
    print_seperator()

    # Roman Numerals
    print('Enter a whole number to return the roman numerals conversion')#
    print('Result:', roman_numbers(int(input('Enter number: '))))
    print_seperator()
    pass

# Run tests
test()