'''
   A program to test hash function variations
'''
import Hash

def testHash(radix, modulus, fName):
    print "\n"
    print("Using radix " + str(radix) + " and modulus " + str(modulus) + ".")
    print"\n"
    print("  Input  |  hash value")
    print("----------------------")
    file = open(fName)
    for line in file:
        for word in line.strip().split(' '):
            if (word != ''):
                print('{0:10s} {1:8d}'.format(word, hash(word, radix, modulus)))

testHash(128, 31, "../dataFiles/wordList.txt")
