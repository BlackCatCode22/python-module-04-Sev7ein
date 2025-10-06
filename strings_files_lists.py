#10/5/25
# s.n


# code written up is only practice, no file it grabs from
#will open our selected file ex. open('')
han = open('fakeExample.txt')
# A for loop that goes through each line, running the next codes to check if it falls in their parameters
for line in han:
    # this line throws out any white space in the text file, between each line and word.
    line = line.rstrip()
    ## This line grabs the words to check and see if the first word is "from" and if not it's skipped.
    # Once From is found it checks the next 3 words and prints the next two
    wds = line.split()
    # A guardian pattern, named because the next line can potentially break. The current line used to check before running
    # guardian in a compound statement.
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])