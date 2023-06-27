from heapq import nlargest
from nltk import ngrams

filename = "much_ado.txt"
N = 20

def lowercase(word):
    return word.lower()

def strip(word):
    punc = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    for char in word:
        if char in punc:
            word = word.replace(char, "")
    return word

def count(text):
    counts = {}
    for word in text:
        if word not in counts.keys():
            counts[word] = 0
        counts[word] += 1
    return counts

def print_top(grams, n):
    print("most frequent {}-grams of words:".format(n))
    for gram in grams:
        print("{: <30} {} times".format(' '.join(gram[0]), gram[1]))
    print()

def main():
    text = open(filename, "r")
    text = text.read()
    text = text.split()
    text = list(map(lowercase, text))    
    text = list(map(strip, text))
    
    for i in range(1,5):
        grams = ngrams(text, i)
        counts = count(grams)
        top = nlargest(N, counts.items(), key=lambda i: i[1])
        print_top(top, i)    

if __name__=='__main__':
    main()
