def median(a): 
    n = len(a)
    i = 2
    aux = []
    while(n % i != 0):
      i +=1
    print("Para realizar a seleção da mediana das medianas primeiro temos que dividir o vetor em n vetores de mesmo tamanho")
    print("O vetor fornecido possui tamanho {} então devemos dividí-lo em {} vetores\n".format(n, i))
    for x in range(0, i):
      aux.append([])
    j = 0
    medians = []
    print("A divisão dos vetores resultou em: ", end='')
    for x in a:
      aux[j].append(x)
      if len(aux[j]) == n//i:
        print(aux[j], end=' ')
        aux[j].sort()
        j += 1
    for array in aux:
      half = len(array)//2
      medians.append(array[half])
    print("\nApós a divisão temos que ordenar todos os {} vetores:".format(i), end=' ')
    print(aux)
    print("\nApós a ordenação, temos que selecionar as medianas de cada vetor:", end=' ')
    print(medians)
    medianOfMedians = medians[len(medians)//2]
    print("A mediana das medianas:", medianOfMedians)
    return medianOfMedians

from random import randint
size = randint(5,25)
if size%2 == 0:
  size += 1
a = [randint(0, 100) for x in range(0,size)]
print(a)
median(a)