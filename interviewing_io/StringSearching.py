def grep_soln1(haystack, needle):
    if not haystack or not needle:
        return []

    res = []
    k = len(needle)
    for i in range(len(haystack)-k):
        if is_match(haystack[i:i+k], needle):
            res.append(i)
    return res

def is_match(str1, str2):
    print(str1, str2)
    if str1 == str2:
        return True
    return False


def grep_soln2(haystack, needle):

    haystack_len = len(haystack)
    needle_len = len(needle)

    if haystack_len <= 0 or needle_len <= 0:
        return []

    matrix = [[0 for _ in range(haystack_len)] for _ in range(needle_len)]
    left, right = 0, needle_len

    for row in range(needle_len):
        for col in range(left, haystack_len-right, 1):
            if row > 0 and col > 0:
                if haystack[col] == needle[row]:
                    matrix[row][col] = matrix[row-1][col-1] + 1
            else:
                if haystack[col] == needle[row]:
                    matrix[row][col] = 1
        left += 1
        right -= 1

    last_row = matrix[-1]
    return [i-needle_len+1 for i in range(haystack_len) if last_row[i] == len(needle)]


string1 = "aaabccbabcdef"
string2 = "abc"
out = grep_soln1(string1, string2)
print(out)

string1 = "bbbbbb"
string2 = "bbb"
out = grep_soln1(string1, string2)
print(out)

string1 = "aaabccbabcdef"
string2 = "abc"
out = grep_soln2(string1, string2)
print(out)

string1 = "bbbbbb"
string2 = "bbb"
out = grep_soln2(string1, string2)
print(out)
