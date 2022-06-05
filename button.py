#https://codingcompetitions.withgoogle.com/codejam/round/000000000087711b/0000000000accfdb
t = input()
def steps(customer, goingup, preassure, stuff):
    steps2=0
    big=0
    if goingup==True:
        steps2+=abs(stuff[customer][-1]-preassure)
        steps2+=stuff[customer][-1]-stuff[customer][0]
        big=stuff[customer][0]
    if goingup==False:
        steps2+=abs(stuff[customer][0]-preassure)
        steps2+=stuff[customer][-1]-stuff[customer][0]
        big=stuff[customer][-1]
    if customer==len(stuff)-1:
        return steps2
    thing1=int(steps(customer+1, True, big,stuff))
    thing2=int(steps(customer+1, False, big,stuff))
    answer=steps2+min(thing1,thing2)
    return answer
for o in range(int(t)):
    data=input()
    customers=int(data.split(" ")[0])
    products=int(data.split(" ")[1])
    stuff=[]
    for i in range(customers):
        things=input().split(" ")
        for j in range(len(things)):
            things[j]=int(things[j])
        things.sort()
        stuff.append(things)
    p=o+1
    print("Case #{0}: {1}".format(p, min(steps(0, True, 0, stuff),steps(0, False, 0, stuff))))
