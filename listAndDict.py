#! /usr/bin/env python3

# lists and dictionaries

mylist = ['beer', 'free', 'banana', 'gorilla']
print("I am a list")
for item in mylist:
  print(item)

# the list is indexed from 0

print("the first item on the list is {0}".format(mylist[0]))
print("The length of the list is {0:d}".format(len(mylist)))

print("")
print("""let's look at sorting
            .sort() sorts the list in place.
            sorted() returns the sorted list without destroying the original.""")
L = [4, 6, 7, 19, 3, 2, 1]
print(sorted(L))
print("The original list")
print(L)
L.sort()
print("run L.sort(): {0}".format(L))
print("""
    Now let's reverse the order""")
L.reverse()
print("Run L.reverse(): {0}".format(L))

print("")
print("Now let's look at dictionaries")
mydict = {'free':'as in beer', 'linux':'operating system'}
print("")
print("The item that corresponds to 'free' is '{0}'".format(mydict['free']))
print("The length of the dictionary is {0:d}".format(len(mydict)))
