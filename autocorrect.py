from spellCheckingAlgorithms import *
from spellCheck import *
import time


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
    print()

    dict_trie = loadWordsTrie()

    #You need to manually end the loop
    while (True):
        userInput = input('Enter text: ')
        t1 = time.time()
        result = changeWords(userInput, dict_trie, algo)#spellcheck(userInput,dict_trie)
        print("Output:")
        print(result)
        print("Total time taken: "+str(time.time() - t1))
        print()
