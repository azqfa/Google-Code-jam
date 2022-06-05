#https://codingcompetitions.withgoogle.com/codejam/round/0000000000877b42/0000000000afe6a1
t = input()
def sticky(letters):
    mega=[]
    c=0
    while True:
        mega.append([])
        while True:
            g=len(mega[c])
            for i in range(len(letters)):
                if letters[i][1]==True:
                    if len(mega[c])==0:
                        mega[c]=letters[i][0]
                        letters[i][1]=False
                    elif mega[c][0]==letters[i][0][-1]:
                        mega[c]=letters[i][0]+mega[c]
                        letters[i][1]=False
                    elif mega[c][-1]==letters[i][0][0]:
                        mega[c]=mega[c]+letters[i][0]
                        letters[i][1]=False
            if g==len(mega[c]):
                break
        if len(mega[c])==0:
            mega.pop(-1)
            break
        c+=1
    return mega
for o in range(int(t)):
    num=int(input())
    letters=input().split(" ")
    data=[]
    priority=[]
    for i in letters:
        if i[0]==i[-1]:
            priority.append([i,True])
        else:
            data.append([i,True])
    for i in range(len(data)):
        for g in range(len(priority)):
            if priority[g][1]:
                if data[i][0][0]==priority[g][0][0]:
                    priority[g][1]=False
                    data[i][0]=priority[g][0]+data[i][0]
                if data[i][0][-1]==priority[g][0][0]:
                    priority[g][1]=False
                    data[i][0]=data[i][0]+priority[g][0]
    for i in priority:
        if i[1]:
            data.append(i)
    mega=""
    stuff=sticky(data)
    for i in stuff:
        mega+=i
    a=26*[0]
    c='8'
    Valid=True
    for i in mega:
        if i!=c:
            a[ord(i)-65]+=1
            if a[ord(i)-65]>1:
                Valid=False
        c=i
    if Valid:
        print("Case #"+str(o+1)+": "+mega)
    else:
        print("Case #"+str(o+1)+": IMPOSSIBLE")
