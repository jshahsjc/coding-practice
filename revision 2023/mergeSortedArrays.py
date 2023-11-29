def mergeSortedArrays(list1, list2):
    i = j = 0
    res = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    while i <  len(list1):
        res.append(list1[i])
        i += 1
    while j < len(list2):
        res.append(list2[j])
        j += 1

    return res
