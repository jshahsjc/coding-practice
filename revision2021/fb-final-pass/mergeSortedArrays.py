def mergeSortedArrays(A1, A2):
    i = j  = 0
    M = []
    while i < len(A1) and j < len(A2):
        if A1[i] <= A2[j]:
            M.append(A1[i])
            i += 1
        else:
            M.append(A2[j])
            j += 1

    while i < len(A1):
        M.append(A1[i])
        i += 1

    while j < len(A2):
        M.append(A2[j])
        j += 1
