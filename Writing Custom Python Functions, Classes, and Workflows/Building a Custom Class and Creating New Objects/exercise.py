"""
Building a Custom Class and Creating New Objects
Author: Leon Shpaner
Date: August 16, 2020

Because the strings, dictionaries and functions work together
to carry out various tasks, which we’d probably like to reuse, it makes sense to
bundle them together in a new datatype, the ShiftCipher. We’re calling it a 
ShiftCipher since it is based on the principle of shifting letters in the 
alphabet by a fixed amount. Other ciphers might be based on other 
transformations of letters (such as a RandomCipher that randomly maps one letter
to another), so it’s good to give our new datatype a name as specific as 
possible.
"""

# Let’s first complete the __init__ method. This is code that is called when you
# want to create a new ShiftCipher. You’ll see that the __init__ method takes 
# one input beyond the required self: that is the number of letters to shift in 
# the alphabet (either a positive or negative integer). You’ll want to store the
# value of the shift, and then construct both the self.cipher and self.decoder 
# based upon the value of the shift.

 def __init__(self, shift):
        """
        Constructs a ShiftCipher for the specified degree of shift (positive or 
        negative),
        by building a cipher (dictionary mapping from letters to other letters),
        and 
        a decoder (the inverse of the cipher)
        """
        self.shift = shift
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        self.cipher = {self.letters[i]: self.letters[(i + shift) % \
            len(self.letters)] for i in range(len(self.letters))}
        self.decoder = {self.letters[i]: self.letters[(i - shift) % \
            len(self.letters)] for i in range(len(self.letters))}

# The method transform_message is more or less like the function you wrote in 
# the earlier exercise, except converted to a method for ShiftCipher objects.

def transform_message(self, message, cipher):
        """
        Transforms a message using the specified cipher.  Is not called by users
        directly,
        and can be called with either the cipher (to encrypt) or the decoder 
        (to decode).
        """
        tmsg = ''
        for c in message:
            tmsg = tmsg + cipher.get(c, c)
        return tmsg
        
# Complete both the encrypt and decode methods so that they call self.
# transform_message with the appropriate cipher. Each of these methods should 
# return a string (either an encrypted one, or a decoded one). Remember: 
# whenever you call one of these functions inside the class, make sure to 
# prepend the function name with self.

    def encrypt(self, message):
        """
        Transforms a message using the cipher, by calling self.transform_message
        """
        return self.transform_message(message, self.cipher)

    def decode(self, message):
        """
        Transforms a message using the decoder, by calling 
        self.transform_message
        """
        return self.transform_message(message, self.decoder)

test = "I come to bury Caesar, not to praise him."
