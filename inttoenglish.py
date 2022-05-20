import copy

class Solution:
    numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 
               5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
               10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
               14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
               18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty',
               40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
               80: 'eighty', 90: 'ninety',}


    def helper(num:int ) -> str:
        # instantiate empty result string
        # this will be built as we iterate through input
        wordResult = ""

        hundreds = num // 100
        if (hundreds > 0):
            wordResult += Solution.numbers[hundreds]
            wordResult += ' hundred'
        num = num % 100
        tens = num // 10
        ones = num % 10 

        if (tens == 0 and ones == 0):
            return wordResult

        if (hundreds > 0 and (tens > 0 or ones > 0)):
            wordResult += ' '

        if (tens == 1 and ones > 0):
            wordResult += Solution.numbers[num]
        elif(tens == 1 and ones == 0):
            wordResult += Solution.numbers[num]
        elif(tens >=2 and ones == 0):
            wordResult += Solution.numbers[num]
        elif(tens >=2 and ones > 0):
            wordResult += Solution.numbers[tens*10]
            wordResult += ' '
            wordResult += Solution.numbers[ones]
        else:
            wordResult += Solution.numbers[ones]

        return wordResult

    
    def numberToWords(num: int) -> str:
        0 <= num <= 2^31 - 1

        Solution.wordResult = ""
        temp = copy.copy(num)
        billions = temp // (10**9)
        temp = temp % (10**9)
        millions = temp //  (10**6)
        temp = temp % (10**6)
        thousands = temp // (10**3)
        hundreds = temp % (10**3)

        if (billions > 0):
            Solution.wordResult += Solution.helper(billions)
            Solution.wordResult += ' billion'
            if (millions + thousands + hundreds > 0):
                Solution.wordResult += ' '
        
        if (millions > 0):
            Solution.wordResult += Solution.helper(millions)
            Solution.wordResult += ' million'
            if (thousands + hundreds > 0):
                Solution.wordResult += ' '

        if (thousands > 0):
            Solution.wordResult += Solution.helper(thousands)
            Solution.wordResult += ' thousand'
            if (hundreds > 0):
                Solution.wordResult += ' '

        if(hundreds > 0):
            Solution.wordResult += Solution.helper(hundreds)

        if (num == 0):
            Solution.wordResult += Solution.numbers[num]

        # return Solution.wordResult
        print(Solution.wordResult)



def main():
        numb = int(input("Enter a number to write out in English: "))
        Solution.numberToWords(numb)

if __name__ == "__main__":
        main()
        