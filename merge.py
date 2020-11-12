def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
        i=0
        j=0
        k=0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

if __name__ == '__main__':
    arr = [ 1, 2, 50, 80, 15, 23, 8, 9, 10, 12, 11, 13, 5, 6, 7, 45]
    print("", end="\n")
    print('Array fornecido: {}'.format(arr))
    mergeSort(arr)
    print("Vetor ordenado é: ", end="")
    printList(arr)