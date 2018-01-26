hex1 = '42696c6c792c20646f6e27'.decode("hex") # decodes the hex into ASCII
hex2 = '742062652061206865726f'.decode("hex")
ascii = '' # declare variable to put in XOR'd results

'''
hex1 is now "Billy, don'"
hex2 is now 't be a hero'

Now we will XOR the two values with a loop using ord() to get ASCII code
of character and then chr() to revert back to ASCII
'''

for x,y in zip(hex1,hex2):
    ascii += chr(ord(x) ^ ord(y))

print ascii.encode("hex") # the results after XOR
