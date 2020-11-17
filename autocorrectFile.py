from autocorrect import spellcheck
from spellCheck import loadWordsTrie

"""
Input a text document and it can autocorrect all the words 
and output a file with corrected words
Parameters
@filenameIn: name of the input file
@filenameOut: name of the output file containing the corrected result
"""
def changeWords(filenameIn,filenameOut):
    dict_trie = loadWordsTrie()
    fileIn = open(filenameIn, "rt")
    fileOut = open(filenameOut,"wt")
    for line in fileIn:
        for word in line.split():
            #Check if the word contains any symbols at the end
            #For example: "Hello," and "World!"
            if (any(elem in word[-1] for elem in ".,?!();:")):
                corrected = spellcheck(word[0:-1], dict_trie)
                #If the autocorrect cannot find any matches, it will not modify that word
                if (len(corrected) != 0):
                    fileOut.write(word.replace(word[0:-1], corrected) + " ")
            else:
                corrected = spellcheck(word, dict_trie)
                if (len(corrected) != 0):
                    fileOut.write(word.replace(word, corrected) + " ")
        fileOut.write("\n")
    fileIn.close()
    fileOut.close()

#Test
if __name__ == "__main__":
    changeWords("input_test.txt","output_text.txt")