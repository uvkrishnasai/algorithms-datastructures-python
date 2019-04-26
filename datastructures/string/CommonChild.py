

def common_child(s1, s2):
    m, n = len(s2), len(s1)
    matrix = [[0 for i in range(n+1)] for j in range(m+1)]

    for i, x in enumerate(s1):
        for j, y in enumerate(s2):
            if x==y:
                matrix[i+1][j+1] = matrix[i][j]+1
            else:
                matrix[i+1][j+1] = max(matrix[i][j+1], matrix[i+1][j])

    print(matrix)
    return matrix[-1][-1]


#s1 = 'SHINCHAN'
#s2 = 'NOHARAAA'
s1 = 'WEWOUCUIDGCGTRMEZEPXZFEJWISRSBBSYXAYDFEJJDLEBVHHKS'
s2 = 'FDAGCXGKCTKWNECHMRXZWMLRYUCOCZHJRRJBOAJOQJZZVUYXIC'
common_child(s1, s2)
