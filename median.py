def median(a): 
    n = len(a)
    i = 2
    aux = [[],[]]
    while(n % i != 0):
      i +=1
      aux.append([])
    # k = a.group_by.with_index{|_, i| i % 5}.values
    # print(k)
    j = 0
    for x in a:
      aux[j].append(x)
      if len(aux[j]) == 5:
        j += 1
    print(aux)

    

a = [2,5,9,19, 24, 54, 5, 87, 9, 10, 44, 32, 18, 13, 2, 4, 23, 26, 16, 19, 25, 39, 47, 56, 71]
median(a)