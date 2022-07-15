# python code to correct spelling of words.
from textblob import TextBlob
def convert(string):
    li=list(string.split())
    return li
string1=input("Enter your word:")
words=convert(string1)
corrected=[]
for i in words:
    corrected.append(TextBlob(i))
print("Wrong words= ",words)
print("Corrected words= ")
for i in corrected:
    print(i.correct(), end=" ")

