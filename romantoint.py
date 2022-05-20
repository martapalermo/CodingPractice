class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, 
                 "C":100, "D":500, "M":1000}
        
        intResult = 0
        # iterating thru length of string s
        for i in range(len(s)):
        # check if i+1 is inbound, then
        # we check what the value of character at index i is 
        # if i is smaller than next (i+1):  
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                # subtract smaller value from result,
                intResult-= roman[s[i]]
                # otherwise we add to the result int
            else:
                intResult+= roman[s[i]]
            
        print(intResult) 

def main():
        s = input("Enter a roman numeral: ")
        Solution.romanToInt(Solution, s)

if __name__ == "__main__":
        main()



          
        