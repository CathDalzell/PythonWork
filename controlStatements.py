#! /usr/bin/env python3


r = range(0, 7, 2)

# I can use a range as an iterator
print("Using a range")
for i in r:
    print(i)

# can convert the range to a list

l = list(r)
l[0] = 50

print("Using a list")
for i in l:
    print(i)
