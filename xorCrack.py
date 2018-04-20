import detectEnglish # https://inventwithpython.com/detectEnglish.py and https://inventwithpython.com/dictionary.txt required

hex = open('test.txt') # filename of the list of hex you want to crack
for line in hex.read().splitlines():
    unhex = bytearray.fromhex(line)
    for i in range(1, 255):
        unxor = ''.join(chr(x ^ i) for x in unhex)
        if detectEnglish.isEnglish(unxor, wordPercentage=40): # set percentage
            print(line)
            print('Possible key:' + str(i))
            print(unxor + '\n')
