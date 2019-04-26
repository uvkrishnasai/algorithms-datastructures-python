def quick_sort(arr, left, right):
    if len(arr) == 0 or len(arr) == 1:
        return

    if left < right:
        partition(arr, left, right, c)


def partition(arr, l, r):
    pivot = arr[r]
    i = l-1
    for j in range(l, r+1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]

    quick_sort(arr, l, i)
    quick_sort(arr, i+2, r)


arr_in = [10, 7, 8, 9, 1, 5]
quick_sort(arr_in, 0, len(arr_in)-1, 0)
print(arr_in)
