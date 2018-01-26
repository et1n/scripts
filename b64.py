import base64

f = open('rlist', 'w') # wordlist named 'rlist'

for i in range(10,30): # insert range of numbers here
    print "Reversed base64 of %s is:" % (i), base64.b64encode(str(i))[::-1]
    f.write(base64.b64encode(str(i))[::-1] + '\n')

f.close()

