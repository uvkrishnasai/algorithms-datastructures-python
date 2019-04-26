def get_permutations(string):
    if not string:
        return {''}

    return get_perms('', string)


def get_perms(prefix, postfix):

    if len(postfix) == 1:
        return {prefix+postfix, postfix+prefix}

    values = get_perms(postfix[0], postfix[1:])

    # print("prefix: {}, postfix: {}, values: {}".format(prefix, postfix, values))
    new_values = set()

    for value in values:
        for i in range(len(value)+1):
            new_values.add(value[:i] + prefix + value[i:])

    return new_values


actual = get_permutations('')
expected = set([''])
assert(actual == expected)

actual = get_permutations('a')
expected = set(['a'])
assert(actual == expected)

actual = get_permutations('ab')
expected = set(['ab', 'ba'])
assert(actual == expected)

actual = get_permutations('abc')
expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
assert(actual == expected)