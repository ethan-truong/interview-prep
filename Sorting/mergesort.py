#Returns a sorted arr
def mergesort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2
        left = mergesort(arr[:mid])
        right = mergesort(arr[mid:])
        return merge(left, right)

#Merges two sorted lists into one sorted list
def merge(left, right):
    rtn = []

    while 0 < len(left) or 0 < len(right):
        if len(left) == 0:
            rtn.extend(right)
            right = []
        elif len(right) == 0:
            rtn.extend(left)
            left = []
        elif left[0] > right[0]:
            rtn.append(right.pop(0))
        else:
            rtn.append(left.pop(0))

    return rtn
