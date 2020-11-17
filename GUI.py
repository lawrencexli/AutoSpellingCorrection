import tkinter as tk
from tkinter import messagebox
from spellCheck import *

dict_trie = loadWordsTrie()         # global variable for the trie of words

def spellcheck_popularity(word_input, trie):
    """
    takes a word, word_input, and a trie to search for that word
    returns the word that is most common in the resulting possible words
    """
    words = getWordsDistance(word_input, 2)
    possibleWords = []
    for word in words:
        possibleWords += trie.matchAll(word)

    lowest_rank = 11000
    best_word = ""
    cur_rank = 0

    for candidate in possibleWords:
        cur_rank = trie.findFreq(candidate)
        if cur_rank != -1 and cur_rank < lowest_rank:
            lowest_rank = cur_rank
            best_word = candidate

    return best_word


    """
    # find most common word returned
    popularity = {}
    for candidate in possibleWords:
        if candidate not in popularity:
            popularity[candidate] = 1
        else:
            popularity[candidate] += 1

    best_match = 0
    best_word = ""

    for candidate in popularity:
        if popularity[candidate] > best_match:
            best_match = popularity[candidate]
            best_word = candidate

    """

    #return best_word


def changeWords(text):
    '''
    Takes unedited text from the text box
    Returns the suggested corrected text
    '''
    
    correctedText = ""

    for word in text.split():
        word = word.lower()
        #Check if the word contains any symbols at the end
        if (any(elem in word[-1] for elem in ".,?!();:")):
                # Check if word is already correct
                if (dict_trie.search(word[0:-1])):
                    correctedText += (word[0:-1] + " ")
                # Otherwise, correct the word
                else:
                    corrected = spellcheck_popularity(word[0:-1], dict_trie)
                    #If the autocorrect cannot find any matches, it will not modify that word
                    if (len(corrected) != 0):
                        correctedText += (word.replace(word[0:-1], corrected) + " ")
                    else:
                        correctedText += (word + " ")
        # Normally ended words
        else:
            # Check if word is already correct
            if (dict_trie.search(word)):
                correctedText += (word + " ")
            # Otherwise, correct the word
            else:
                corrected = spellcheck_popularity(word, dict_trie)
                #If the autocorrect cannot find any matches, it will not modify that word
                if (len(corrected) != 0):
                    correctedText += (word.replace(word, corrected) + " ")
                else:
                    correctedText += (word + " ")

    return correctedText


def handle_click(event):
    """
    Handles the Check Spelling button click
    """
    if (algorithm.get() == 0):              # check that algorithm was selected
        messagebox.showwarning("Warning", "Must select an algorithm before proceeding!")

    # else changeWords with algorithm specified in algorithm.get()
    
    output_text.delete("1.0", tk.END)       # clear the current output text box
    text = input_text.get("1.0", tk.END)    # get all of the current text from the input text box
    updatedText = changeWords(text)         # update any mistakes to the text
    output_text.insert("1.0", updatedText)  # display updated text in the output text box
    

if __name__ == "__main__":
    window = tk.Tk()
    title = tk.Label(text="Spellchecker", width=100, font=("Helvetica", 16))
    title.pack()

    subtitle = tk.Label(text="Developed by Sebastian Ascoli, Jonathan Basom, Khoi Lam, Lawrence Li", width=100, font=("Helvetica", 8))
    subtitle.pack()

    subtitle2 = tk.Label(text="CSCI 311 - Fall 2020", width=100, font=("Helvetica", 8))
    subtitle2.pack()


    frame = tk.Frame(master=window, width=100, height=50)
    frame.pack(fill=tk.BOTH)

    tk.Label(frame, text="Word Selection Algorithm:", bg="Orange", width=50).pack(anchor=tk.W)
    # radio buttons for word selection algorithm
    algorithm = tk.IntVar()
    tk.Radiobutton(frame, text="Appearance", variable=algorithm, value=1).pack(anchor=tk.W)
    tk.Radiobutton(frame, text="Longest Common Subsequence", variable=algorithm, value=2).pack(anchor=tk.W)
    tk.Radiobutton(frame, text="Frequency", variable=algorithm, value=3).pack(anchor=tk.W)
    

    button = tk.Button(master=frame, text="Check Spelling", width=25, height=5, bg="blue", fg="orange")
    button.pack()
    button.bind("<Button-1>", handle_click)

    input_lbl = tk.Label(master=frame, text="Enter Text Here:", width=75, font=("Helvetica", 10))
    input_lbl.pack(fill=tk.BOTH, side=tk.LEFT)

    output_lbl = tk.Label(master=frame, text="Suggested Corrections:", width=75, font=("Helvetica", 10))
    output_lbl.pack(fill=tk.BOTH, side=tk.LEFT)

    input_text = tk.Text()
    input_text.pack(fill=tk.BOTH, side=tk.LEFT)

    output_text = tk.Text()
    output_text.pack(fill=tk.BOTH, side=tk.LEFT)

    window.mainloop()


    
