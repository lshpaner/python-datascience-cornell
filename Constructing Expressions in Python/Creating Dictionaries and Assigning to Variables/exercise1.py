"""
Creating Dictionaries and Assigning to Variables
Author: Leon Shpaner
Date:   July 16, 2020

"""
#In exercise1.py in the code editor window, write several lines of code to do 
#the following in succession, and once you are finished, run the exercise code 
#file in the interpreter:

#Write an expression to create a dictionary that has the following letters as 
#keys and numbers as values: map the letter 'a' to the number 1, the letter 'b' 
#to the number 2, and the letter 'c' to the number 3. Assign the expression to 
#the variable my_dict

#After creating my_dict, write an expression to print its value.
#Access the value associated with the key "b", and assign it to the variable 
#val_b.

#Write a new statement that adds a new entry to the dictionary, by assigning the 
#value 4 to the key "d".
#Write another expression to print the value of my_dict.

my_dict = {"a": 1, "b": 2, "c": 3, "d":4}
my_dict['c'] = 30
print(my_dict)
val_e = my_dict['e']