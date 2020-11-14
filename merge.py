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
                    print(arr[:i+j+1], '(Indíce {} do array Esquerdo)'.format(i))
                i += 1
            else:
                arr[k] = R[j]
                if(count == tam):
                    print(arr[:i+j+1], '(Indíce {} do array Direito)'.format(j))
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
    from random import randint
    size = randint(5,25)
    if size%2 == 0:
        size += 1
    arr = [randint(0, 100) for x in range(0,size)]
    print("", end="\n")
    print('Array fornecido: {}'.format(arr))
    mergeSort(arr)
    print("Vetor ordenado é: ", end="")
    printList(arr)