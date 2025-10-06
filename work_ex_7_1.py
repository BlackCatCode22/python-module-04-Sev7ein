# 10/5/25
# s.n

# This line opens our file to be examined
fileOpener = open('fileExample.text')
# A for loop that goes through each line in the document we selected
for line in fileOpener:
    lineReader = line.rstrip()
    print(lineReader.upper())
