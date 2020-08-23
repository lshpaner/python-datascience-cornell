"""
Simple Ciphers With Lists and Dictionaries
Author: Leon Shpaner
Date:   August 14, 2020

"""

# Examine the starter code in the editor window.
# We first define a character string named letters which includes all the 
# upper-case and lower-case letters in the Roman alphabet.
# We then create a dictionary (using a one-line dictionary comprehension) named
# cipher that maps each letter to another letter shifted three to its left in 
# the list of all letters.
# Run the starter code in the interpreter and print the contents of the cipher.
# You should see that it maps each letter in letters to a different letter.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
cipher = {letters[i]: letters[(i-3) % len(letters)] for i in range(len(letters))
}

# Let’s encrypt some messages now, using cipher. In the code editor, write the 
# function named transform_message(message, cipher) that takes two inputs: a 
# message that you want to encrypt, and a cipher to do the encryption. The body 
# of this function is rather simple: it initializes an empty string named tmsg, 
# loops over the characters in the input message, transforms them according to 
# the cipher, and sticks that transformed character onto the end of tmsg. Once 
# the entire message is transformed, the transformed message is returned.

def transform_message(message, cipher):
    tmsg = ''
    for c in message:
        tmsg = tmsg + (cipher[c] if c in cipher else c)
    return tmsg

"""
The starter code has a test message (named test). Try your transform_message 
function on the test message: does the output look like this: 
'F Zljb ql Yrov zXbpXo, klq ql moXfpb efj.'? In addition to having it printed 
out on the screen, you should also save the transformed message to a variable 
named ttest, so that we can reuse it later.
"""
test = "I come to bury Caesar, not to praise him."

# Having a coded message does not help you so much if you don’t have a way to 
# decode it. Fortunately, we can do that just by creating another cipher. In the
# code editor, define a new dictionary named decoder that maps from a 
# transformed letter back to the original letter, i.e., it just undoes the 
# transformation that the original cipher did. The easiest way to do this is to
# recognize that the cipher is a dictionary that maps keys to values, and you
# want a different dictionary that maps the values back to keys.

decoder = {letters[i]: letters[(i+3) % len(letters)] for i in range(len(letters)
)}