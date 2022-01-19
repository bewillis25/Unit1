'''
######################
Lab 1.04 - Magic Genie
######################
Project Objective
------------------
Use Python to interact with variables and user input
Create a genie program below in the editor.

Project Specifications
----------------------
Have the program introduce itself
Have the program ask for three separate wishes
Print all the wishes together
Example output:
    I am a genie, you have 3 wishes.
    What would you like to wish for? cats
    What would you like to wish for? dogs
    What would you like to wish for? more cats
    Your wishes are cats, kittens and more cats
    ** there are some repeated string there, make sure to move those into variables.

Genie Confusion
---------------
Now it's time to make your genie confused. Edit your code to have him print your first wish as your last wish,
and your second wish as your first wish, and your third wish as your second wish.

Hint
----
Remember to add spaces you can combine " " to the end of your string using the + operator. So
print("hello" + " " + "student") would print hello student
'''

# Original Genire Script
print("Hello, I am a genie, and I will grant you three wishes")
a = input("What is your first wish? ")
b = input("What is you second wish? ")
c = input("What is your third wish? ")
print(f"Your first wish is {a}, your second wish is {b}, and your third wish is {c}.")


# Confused Genire Script
print("Hello, I am a genie, and I will grant you three wishes")
a = input("What is your first wish? ")
b = input("What is you second wish? ")
c = input("What is your third wish? ")
print(f"Your first wish is {b}, your second wish is {c}, and your third wish is {a}.")