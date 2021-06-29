def mergeSortedArrays(A1, A2):
    i = j = 0
    A = []
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            A.append(A1[i])
            i += 1
        else:
            A.append(A2[j])
            j += 1

    while i < len(A1):
        A.append(A1[i])
        i += 1
    while j < len(A2):
        A.append(A2[j])
        j += 1

    return A
