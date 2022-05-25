


"""
Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.
"""

def countBinarySubstrings(s: str) -> int:
    N = len(s)
    previous, current = 0,1
    output = 0

    for i in range(1,N):
        if s[i]!=s[i-1]:
            output += min(current,previous)
            previous = current
            current = 1
        else:
            current +=1
    print(output + min(previous, current))

def main():
    testCases = ["00110011", "10101"]

    for case in testCases:
        countBinarySubstrings(case)

if __name__ == "__main__":
        main()
