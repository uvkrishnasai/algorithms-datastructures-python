import collections


def find_min(string, char_set):

    if len(string) == 0:
        return ""

    if len(char_set) == 0:
        return ""

    visited = set()
    min_len = float("Inf")
    res = ""

    for ind, char in enumerate(string):
        if char not in char_set:
            continue

        visited.add(char)

        for nex in range(ind+1, len(string)):
            if string[nex] in char_set:
                visited.add(string[nex])

            if len(char_set-visited) == 0:
                print(char_set, visited, ind, nex)
                visited = set()
                if nex - ind < min_len:
                    min_len = nex-ind
                    res = string[ind:nex+1]
                break

    return res


string_in = "aaabbacb"
char_set_in = {'a', 'b', 'c'}
out = find_min(string_in, char_set_in)
print(out)
