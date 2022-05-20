class Solution:
    def intToRoman(self, num: int) -> str:
        # we added rules for numbers: 40, 90, 400 and 900
        # chose list structure because order matters here
        romanInt = [
            ["I",1], ["IV",4], ["V",5], ["IX", 9], 
            ["X",10], ["XL",40], ["L",50], ["XC",90], 
            ["C",100], ["CD",400], ["D",500], ["CM",900], 
            ["M",1000]
        ]
        
        romanResult = ""
        # iterating thru list in reverse order 
        for romanVal, intVal in reversed(romanInt):
            # does the number divide the integer value?
            # if it is zero -- symbol doesnt go into result. if it is zero, value goes into result
            if num // intVal:
                # count tells us how many time we are adding the roman symbol into the result
                count = num // intVal
                romanResult += (romanVal * count) #takes string (roman) and makes count amount of copies
                num = num % intVal #sets up the next iteration for loop 
        print(romanResult) 

def main():
        numb = int(input("Enter a number to turn roman: "))
        Solution.intToRoman(Solution, numb)

if __name__ == "__main__":
        main()



          
        