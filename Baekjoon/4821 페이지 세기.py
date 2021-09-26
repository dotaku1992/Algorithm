while(True):
    page = int(input())
    if page == 0:
        break
    printtable = [0 for _ in range(page+1)]
    orderlist = input().split(',')

    for text in orderlist:
        if text.count('-')==0:
            if int(text)<=page:
                printtable[int(text)]=1

        else:
            s,e = map(int,text.split('-'))
            if s > e:
                continue
            if s > page:
                continue
            else:
                for idx in range(s,min(e+1,page+1)):
                    printtable[idx]=1
    print(sum(printtable))
