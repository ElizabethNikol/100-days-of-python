"""
Day 13 - Debugging Techniques

What I learned:
1. Describe the Problem
2. Reproduce the Bug
3. Play Computer (trace through code)
4. Fix the Errors
5. Print is your Friend
6. Use a Debugger
7. Take a Break
8. Ask for Help
9. Run Often
10. Ask StackOverflow

Common Errors:
- SyntaxError
- IndentationError
- TypeError
- NameError
- IndexError
- KeyError
- AttributeError

Debugging Tips:
- Read error messages carefully
- Check line numbers
- Use print() statements
- Comment out code sections
- Test with simple inputs
"""

# Example 1: Fixed IndexError
def my_function():
    for i in range(1, 21):  # Changed from range(1, 20)
        if i == 20:
            print("You got it")

# Example 2: Fixed Infinite Loop
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # Changed from randint(1, 6)
print(dice_imgs[dice_num])

# Example 3: Fixed TypeError
year = int(input("What's your year of birth?"))  # Added int()
if year > 1980 and year < 1994:
    print("You are a millennial.")

# Example 4: Fixed IndentationError
def mutate_string(string, position, character):
    return string[:position] + character + string[position+1:]

# Example 5: Fixed Logic Error
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print("Day 13 - Debugging Practice Complete!")
