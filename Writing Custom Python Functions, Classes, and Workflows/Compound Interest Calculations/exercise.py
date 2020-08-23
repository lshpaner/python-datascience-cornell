"""
Compound Interest Calculations
Author: Leon Shpaner
Date: August 17, 2020


"""

# Examine the starter code in the editor window, and run that code in the 
# interpreter. What this code is describing is the growth of a pot of money, 
# which started at $100, and which grows over time at a rate of 3% per year. The
# balance at the end of a given year is equal to balance*rate from the year 
# before. The current balance is rounded to the nearest two decimal places 
# (i.e.,$0.01), and is printed out each year for a total period of 10 years. 
# (The balance at year 0 is just the initial principal invested.)


balance = 100.0
rate = 0.03

print(0, round(balance,2))
for n in range(1,11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))

# This is the sort of calculation that we would probably like to do repeatedly, 
# so let’s write a function to capture the basic logic.
# In the code editor, write a function named compound that takes three inputs: 
# balance, rate, and num_periods. That function should take the initial balance,
# a fixed interest rate, and the number of time periods over which the balance 
# is to be compounded. (If the interest rate represents a yearly interest rate, 
# then num_periods would correspond to the number of years; if it is a monthly
# interest rate, it would reflect the number of months.) You’ll want your 
# function to return the current balance (i.e., the total of the principal plus 
# all accrued interest) at the end of the function so that you know how much 
# money you have if you would like to reinvest it.

def compound(balance, rate, num_periods):    
    Amount = round(balance * ((1 + rate) ** num_periods),2)
    return Amount

# Your function is useful, but maybe you’d like to have a record of what the 
# balance was at the end of each year, rather than just a print out of it on the
# screen. So let’s create another function that takes care of that. Write a new 
# function named compound_by_period that takes the same three inputs as before; 
# instead of writing it from scratch, you can copy the previous function 
# definition, paste a new function definition below, and then change the name of
# the function. In this new function, you don’t want to just update and print 
# the balance each year, but keep a list of what those yearly balances are that
# you can return at the end. Initialize an empty list at the start of the 
# function, and then append the yearly balance to the end of the list each time 
# through the loop. Instead of returning just the current balance at the end, 
# return the entire list of yearly balances (the last element of which will be 
# the current balance).

def compound_by_period(balance, rate, num_periods): 
    Amounts = []
    for i in range(num_periods+1):
        Amounts.append(round(balance * ((1 + rate) ** i),2))
    return Amounts

# Since we now have our yearly balances stored in a list, it is easy for us to 
# write other functions to process that data. Write a new function named 
# change_per_period that takes a list of yearly balances and returns a new list
# that contains the change in account value from year to year. So the first 
# element of this new list will contain the difference between the year 1 and 
# year 0 balances, the second element will contain the difference between year 2
# and year 1, etc. Since you are calculating the difference between two 
# consecutive years, the list that is returned by this new function will have 
# one element less than the list of yearly balances that you input.

def change_per_period(Amounts):
    Difference = []
    for i, _ in enumerate(Amounts):
        if i == len(Amounts)-1:
            continue
        Difference.append(round(Amounts[i+1]-Amounts[i],2))
    return Difference

# With your function compound_by_period in hand, we can apply it to a very 
# different problem in compound interest: the wheat on a chessboard problem. 
# First read [url](https://en.wikipedia.org/wiki/Wheat_and_chessboard_problem/) if you
# are unfamiliar with the story. In this problem, the initial investment of 1 
# grain of wheat is compounded for each square on the chessboard, leading to a 
# staggering amount of wheat by the time the chessboard is filled. Your function 
# compound_by_period is just what we need to compute how much wheat will 
# actually end up on the chessboard.

wheat = []    
for i in range(0,64):
    wheat.append(compound(1,1,i))
#print(wheat)
total_wheat = sum(wheat)