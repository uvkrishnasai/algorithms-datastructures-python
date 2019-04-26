def find_shortest_subarray(nums, set_):
    if not nums:
        return 0

    map_ = {val: 0 for val in set_}

    for i in range(len(nums)):
        num = nums[i]
        if num in map_:
            map_[num] = i

    indexes = map_.values()
    return nums[min(indexes): max(indexes)]


arr = [1, 2, 2, -5, -4, 0, 1, 1, 2, 2, 0, 3, 3]
set_1 = {1, 2, 3}
output = find_shortest_subarray(arr, set_1)
print(output)
