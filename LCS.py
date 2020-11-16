"""
Longest common subsequence implemented in python using dynamic programming
Input: string1 - user input string
       string2 - the correct spelling string from dictionary
Output: Largest number of common subsequence
Time complexity: O(string1.length * string2.length)
"""


def lcs(string1, string2):
    # Create a C table of dimension string1.length and string2.length
    c = [[None for i in range(len(string2) + 1)] for j in range(len(string1) + 1)]

    for i in range(len(string1) + 1):
        for j in range(len(string2) + 1):
            if i == 0 or j == 0:
                c[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

    return c[len(string1)][len(string2)]


# Test
if __name__ == "__main__":
    print(lcs("lawrence", "laurance"))
    print(lcs("Sebastian", "Sabestiam"))
    print(lcs("Jonathan","Jomathem"))