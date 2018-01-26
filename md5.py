import hashlib

f = open('numberlist', 'w') # for making a wordlist named 'numberlist'

for i in range(1,20): # this is where you put the range of numbers to hash
    print "MD5 of %s is:" % (i), hashlib.md5(str(i)).hexdigest()
    f.write(hashlib.md5(str(i)).hexdigest() + '\n')

f.close() # wordlist

