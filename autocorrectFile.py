from spellCheck import loadWordsTrie, changeWords
from spellCheckingAlgorithms import *


def changeWordsFile(filenameIn,filenameOut, algo):
    """
    Input a text document and it can autocorrect all the words 
    and output a file with corrected words
    Parameters
    @filenameIn: name of the input file
    @filenameOut: name of the output file containing the corrected result
    @algo: algorithm to be used for changing the words
    """
    dict_trie = loadWordsTrie()
    fileIn = open(filenameIn, "rt")
    fileOut = open(filenameOut,"wt")
    
    inputText = ""
    for line in fileIn: inputText += line
    outputText = changeWords(inputText, dict_trie, algo)
    
    fileOut.write(outputText)
    fileIn.close()
    fileOut.close()

#Test
if __name__ == "__main__":

    #select algo
    algo = None
    inp = input("Please select algorithm (1=appearances, 2=lcs, 3=popularity):")
    if inp == "1":
        algo = spellcheck_appearances
    elif inp == "2":
        algo = spellcheck_LCS
    elif inp == "3":
        algo = spellcheck_popularity
    else:
        print("Incorrect input")
        exit()

    inputFile = input("Input File: ")
    if inputFile == "": inputFile = "test.txt"

    outputFile = input("Output File: ")
    if outputFile == "": outputFile = "out.txt"

    changeWordsFile(inputFile,outputFile, algo)