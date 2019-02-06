# Import Modules
import os
import csv

# Read File
textpath=os.path.join("example.txt")

# Initialize values
characters=0 
wordlist=[]
sentencelist=[]
letterlist=[]

with open(textpath, 'r', newline="") as textfile:
    for line in textfile:
        wordlist+=line.split(' ') # list of all words separated by space
        sentencelist+=line.split('.') # list of all sentences separated by dots.
        characters+=len(line) # total number of characters

#Calculations
wordlist=list(filter(lambda x: x!="\n", wordlist)) #exclude line break from word count
wordcount=len(wordlist)
sentencelist=list(filter(lambda x: x!="\n", sentencelist)) #exclude line break from sentence count
sentencecount=len(sentencelist)-1
letters=round(sum(len(x) for x in wordlist)) #exclude spaces between words from letter count
avg_lt_count=round(letters/wordcount,1)
avg_snt_len=round(sum(len(x.split())for x in sentencelist)/sentencecount,1)

print("Paragraph Analysis")
print("-----------------------------")
print(f"Approximate Word Count: {wordcount}")
print(f"Approximate Sentence Count: {sentencecount}")
print(f"Average Letter Count: {avg_lt_count}")
print(f"Average Sentence Length: {avg_snt_len}")

