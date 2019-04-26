def sort_scores(unsorted_scores, highest_possible_score):
    counter = [0] * (highest_possible_score+1)

    for score in unsorted_scores:
        counter[highest_possible_score-score] += 1

    res = []
    for ind, count in enumerate(counter):
        for i in range(count):
            res.append(highest_possible_score-ind)
    return res


out = sort_scores([37, 89, 41, 65, 91, 53], 100)
print(out)
