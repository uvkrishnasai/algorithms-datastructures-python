"""
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety O
"""


def number_to_words(num):
    output = []
    i = 0

    if num == 0:
        return "Zero"

    append_text(num, output, i)
    return " ".join(output)


def append_text(num, output, i):

    arr = [10 ** 9, 10 ** 6, 10 ** 3, 10 ** 2]

    if i == 10:
        return

    if num == 0:
        return

    if num <= 19:
        # print("num<=10: ", num)
        append_low_ext(num, output)
        return

    if num >= 20 and num <= 99:
        # print("num > 10 and num < 99: ", num)
        append_mid_text(num // 10, output)
        append_low_ext(num % 10, output)
        return

    if num >= 100:
        # print("num >= 100: ", num)
        for n in arr:
            if num // n > 0:
                quo = num // n
                mod = num % n
                print("quo: ", quo, "mod: ", mod)
                append_text(quo, output, i + 1)
                append_big_text(n, output)
                append_text(mod, output, i + 1)
                break
        return
    pass


def append_big_text(num, output):
    text_big = {
        10 ** 9: "Billion",
        10 ** 6: "Million",
        10 ** 3: "Thousand",
        10 ** 2: "Hundred"
    }
    return output.append(text_big[num]) if num in text_big else ""


def append_mid_text(num, output):
    text_mid = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
    }
    return output.append(text_mid[num]) if num in text_mid else ""


def append_low_ext(num, output):
    text_low = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
    }
    return output.append(text_low[num]) if num in text_low else ""
