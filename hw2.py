import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=[0]*26
    with open (filename,encoding='utf-8') as f:
        while True:
            ch = f.read(1)
            if ch == '':
                break
            
            c = ord(ch)
            if (c <= 90 and c >= 65) or (c <= 122 and c >= 97):
                X[ord(ch.upper()) - 65] += 1
            
        i = 0
        print("Q1")
        for count in X:
            print(chr(i + 65) + " " + str(count))
            i += 1
        
    return X

# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!
def getF(counts, language, p):
    result = 0
    for i in range(26):
        result += counts[i] * math.log(language[i])
        
    return math.log(p) + result

letterCounts = shred("letter.txt")
engcounts, spancounts = get_parameter_vectors()
f_eng = getF(letterCounts, engcounts, 0.6)
f_span = getF(letterCounts, spancounts, 0.4)
f_exp = f_span - f_eng;

if f_exp >= 100:
    final_prob = 0
elif f_exp <= -100:
    final_prob = 1
else:
    final_prob = 1/(1 + math.e**f_exp)       

print("Q2\n%.4f\n%.4f" % (letterCounts[0] * math.log(engcounts[0]) 
                          , letterCounts[0] * math.log(spancounts[0])))
print("Q3\n%.4f\n%.4f" % (f_eng, f_span))
print("Q4\n%.4f" % final_prob)
