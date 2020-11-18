import tkinter as tk
from tkinter import messagebox
from spellCheck import *
from spellCheckingAlgorithms import *

dict_trie = loadWordsTrie()         # global variable for the trie of words



def handle_click(event):
    """
    Handles the Check Spelling button click
    """
    output_text.delete("1.0", tk.END)       # clear the current output text box

    #select algo
    algo = None
    if algorithm.get() == 1:
        algo = spellcheck_appearances
    elif algorithm.get() == 2:
        algo = spellcheck_LCS
    elif algorithm.get() == 3:
        algo = spellcheck_popularity
    else:
        messagebox.showwarning("Warning", "Must select an algorithm before proceeding!")
        return 

    
    text = input_text.get("1.0", tk.END)    # get all of the current text from the input text box
    updatedText = changeWords(text, dict_trie, algo)         # update any mistakes to the text
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


    
