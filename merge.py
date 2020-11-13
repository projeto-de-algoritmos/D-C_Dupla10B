count = 0
tam = 0

def mergeSort(arr):
    global count, tam
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        if count == 0:
            tam = len(arr)
            print('Divide-se o array:', L, R)
            count += 1
        mergeSort(L)
        mergeSort(R)
        if count == tam - 1:
            print('Ordena-se os sub-arrays:', L, R)
        count += 1
        i = j = k = 0
        if count == tam:
            print('Juntando e ordenando os sub-arrays:')
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                if count == tam:
                    print(arr[:i+j+1], '(Indíce {} do array L)'.format(i))
                i += 1
            else:
                arr[k] = R[j]
                if(count == tam):
                    print(arr[:i+j+1], '(Indíce {} do array R)'.format(j))
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            if count == tam:
                print(arr[:i+j], '(Indíce {} do array L)'.format(i-1))

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            if(count == tam):
                print(arr[:i+j], '(Indíce {} do array R)'.format(j-1))
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