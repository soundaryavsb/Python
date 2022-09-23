x=""
def longest_word(filename):
    with open(filename,'r') as infile:
        words=infile.read().split()
    min_len=len(min(words,key=len))
    return[word for word in words if len(word)==min_len]
    
x=longest_word("text.txt")
for i in x:
    print(i)
