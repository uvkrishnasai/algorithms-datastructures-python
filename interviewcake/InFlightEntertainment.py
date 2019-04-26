def solve(movie_length, flight_length):
    visited = set()
    for i, elem in enumerate(movie_length):
        if flight_length-elem in visited:
            return True
        else:
            visited.add(elem)
    return False


print(solve([1, 2, 3, 4, 5, 6], 7))
print(solve([3, 8, 3], 6))
print(solve([3, 8], 6))
