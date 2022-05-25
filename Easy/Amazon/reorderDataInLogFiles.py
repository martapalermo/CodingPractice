from typing import List

"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

    Letter-logs: All words (except the identifier) consist of lowercase English letters.
    Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

    The letter-logs come before all digit-logs.
    The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
    The digit-logs maintain their relative ordering.

Return the final order of the logs.
"""

def reorderLogFiles(logs: List[str]) -> List[str]:
    # instantiate 2 empty arrays 
    arr1, arr2 = [], []

    for log in logs: 
        if (log.split()[1]).isdigit():
            arr2.append(log)
        else:
            arr1.append(log.split())

    arr1.sort(key = lambda x:x[0])
    arr1.sort(key = lambda x:x[1:])

    for i in range(len(arr1)):
        arr1[i] = (" ".join(arr1[i]))
    arr1.extend(arr2)
    print(arr1)

def main():

    logList = [
        ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
        ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"],
    ]
    for logs in logList:
        reorderLogFiles(logs)
    
    print("Expected: \n")
    print("[let1 art can, let3 art zero, let2 own kit dig, dig1 8 1 5 1, dig2 3 6]")
    print("[g1 act car, a8 act zoo, ab1 off key dog, a1 9 2 3 1, zo4 4 7]")
    

if __name__ == "__main__":
        main()
