hex1 = '7d2e03292f3370267435262277363b2c2328233c3b2f33'.decode("hex")
len(hex1) # shows that it has 23 characters
key = 'WUTANGWUTANGWUTANGWUTAN' # 23 characters

print ''.join(chr(ord(x) ^ ord(y)) for x,y in zip(hex1,key))
