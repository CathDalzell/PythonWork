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

print("Another example\n")
m = list(range(0, 11))

i = 0
while i < 5:
    print(m[i])
    i += 1

print("Using the break command\n")
i = 0
while True:
    if i > 7:
        break
    print(m[i])
    i += 1
