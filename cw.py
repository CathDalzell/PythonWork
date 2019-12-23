#! /usr/bin/env python3

# short program from Coding Academy 2019
# counts number of occurrences of each word from the Time Machine.

tm = open('data/timemachine.txt', 'r')
dict = {}

for line in tm:
    line = line.strip()
    line = line.translate({ord(i): ' ' for i in '!@#$%&""+-,.;:*?<==>~(){}[]1234567890'})
    line = line.lower()
    line = line.split(' ')
    for word in line:
        if word in dict:
            count = dict[word]
            count += 1
            dict[word] = count
        else:
            dict[word] = 1

output = open("munging/word_count.txt", "w+")
for word, count in dict.items():
    output.write("{0}: {1:d}".format(word, count))
    output.write("\n")

output.close()
