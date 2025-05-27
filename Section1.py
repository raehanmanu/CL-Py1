# 1
def prime_generator(x, y):

    def is_prime(n):
        if n < 2:
            return False
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
                else:
                    return True

    primeList = []
    for num in range(x, y+1):
        if is_prime(num):
            primeList.append(num)

    return primeList
                
# 2
def number_word_converter(n):
    if n == 0:
        return "zero"

    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", 
             "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", 
            "sixty", "seventy", "eighty", "ninety"]

    def two_digit(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num - 10]
        else:
            return tens[num // 10] + ("-" + ones[num % 10] if num % 10 != 0 else "")

    words = ""

    if n >= 1000:
        words += ones[n // 1000] + " thousand "
        n %= 1000

    if n >= 100:
        words += ones[n // 100] + " hundred "
        n %= 100
        if n:
            words += "and "

    if n > 0:
        words += two_digit(n)

    return words.strip()

# 3
def print_ttt_board():
    num = 1
    for row in range(3):
        for col in range(3):
            print(num, end="")
            if col < 2:
                print("|", end="")
            num += 1
        print()
        if row < 2:
            print ("-----")