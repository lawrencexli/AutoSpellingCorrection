import tkinter as tk
from spellCheck import *

dict_trie = loadWordsTrie()         # global variable for the trie of words

def spellcheck_popularity(input, trie):
    """
    takes a word, input, and a trie to search for that word
    returns the word that is most common in the resulting possible words
    """
    words = getWordsDistance(input, 2)
    possibleWords = []
    for word in words:
        possibleWords += trie.matchAll(word)

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

    return best_word


def changeWords(text):
    '''
    Takes unedited text from the text box
    Returns the suggested corrected text
    '''
    
    correctedText = ""

    for word in text.split():
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

    
