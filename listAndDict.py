#! /usr/bin/env python3

# lists and dictionaries

mylist = ['beer', 'free', 'banana', 'gorilla']
print("I am a list")
for item in mylist:
  print(item)

# the list is indexed from 0

print("the first item on the list is {0}".format(mylist[0]))

mydict = {'free':'as in beer', 'linux':'operating system'}
print("")
print("The item that corresponds to 'free' is '{0}'".format(mydict['free']))
