file = open('AI.txt','r')

text = file.read()

words = {}

trash = ['"',',','.','(',')','\'','[',']','\\','/']

for x in trash:
    text = text.replace(x,'')

text = text.lower()
wordlist = text.split()


for x in wordlist:
    words[x] = wordlist.count(x)

for x in words:
    print("Word:", x , ',' , "Count:", words[x])