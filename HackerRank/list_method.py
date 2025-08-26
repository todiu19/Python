if __name__ == '__main__':
    N = int(input())
    arr = []
    for _ in range(N):
        s, *line  = input().split()
        list2 = list(map(int,line))
        if s == 'insert': arr.insert(list2[0],list2[1])
        if s == 'print' : print(arr)
        if s =='remove' : arr.remove(list2[0])
        if s =='sort': arr.sort()
        if s =='append': arr.append(list2[0])
        if s =='pop' : arr.pop()
        if s =='reverse': arr.reverse()
        
 





