if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    list1.sort(key = lambda x : (x[1],x[0]))
    low2 = sorted(set([score for name,score in list1]))[1]
    for i in range(len(list1)):
        if list1[i][1] == low2:
            print(list1[i][0])

        
