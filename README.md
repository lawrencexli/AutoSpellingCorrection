# CSCI 311 - Programming Project

Bucknell University

Fall 2020

## Group members
Jonathan Basom

Sebastian Ascoli

Khoi Lam

Lawrence Li

## Algorithm Discussion

**When the program first runs:**

1. Generate terms with an edit distance of d (deletes only) from each dictionary term and add them together with the original term to the dictionary.

**The above step will only do ONCE**

2. Generate terms with an edit distance (deletes only) from the input term and search them in the dictionary.

3. Use Trie to choose candidate words, and use LCS to compare the candidate words 
