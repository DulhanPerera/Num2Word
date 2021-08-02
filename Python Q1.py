#Import math
import math

# Getting User Inputs
num1 = int(input("Please Enter the Amount:"))

letter = str(input("Please enter your Option:"))
# Converting to USD
if letter == 'C' or letter == 'c':
    #covertNum = round(num1/200.0)
    covertNum = math.ceil(num1 / 200.0)
    print("Result: USD", covertNum)

elif letter == 'W' or letter == 'w':
    # Lists
    ones = ["", "one", "two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
            "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    ones1 = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    hundreds = ["", "One hundred", "Two hundred", "Three hundred", "Four hundred", "Five hundred","Six hundred",
                "Seven hundred", "Eight hundred", "Nine hundred"]

    thousands = ["", "One thousand", "Two thousand", "Three thousand", "Four thousand", "Five thousand", "Six thousand",
                 "Seven thousand", "Eight thousand", "Nine Thousand"]

# Converting Integers into Words
    if num1 <= 19:
        print(ones[num1])

    elif num1 <= 99:
        a1 = num1 // 10
        a2 = num1 % 10
        print(tens[a1], ones[a2])

    elif num1 == 100:
        print("One hundred")

    elif num1 <= 999:
        b2 = num1 // 100
        b1 = num1 % 100
        a1 = b1 // 10
        a2 = b1 % 10
        print(hundreds[b2], tens[a1], ones[a2])
# 1000
    elif num1 == 1000:
        print("One thousand")

    elif num1 <= 9999:
        b3 = num1 // 1000
        b4 = num1 % 1000
        a1 = b4 // 100
        a2 = b4 % 100
        a3 = a2 // 10
        a4 = a2 % 10
        print(thousands[b3], hundreds[a1], tens[a3], ones[a4])

    elif num1 == 10000:
        print("Ten thousand")

    elif num1 <= 99999:
        b3 = num1 // 10000
        b2 = num1 % 10000
        a1 = b2 // 1000
        a2 = b2 % 1000
        a3 = a2 // 100
        a4 = a2 % 100
        a5 = a4 // 10
        a6 = a4 % 10
        print(tens[b3], thousands[a1], hundreds[a3], tens[a5], ones[a6])

    elif num1 == 100000:
        print("Hundred Thousand")
