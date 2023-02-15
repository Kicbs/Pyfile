'''x='computer'
x+='ret'
print(x[1::2])
l=[1,12,56,5,6]
l.append('rt')
l.insert(2,7)
print(l)
l.append(l)
print(l)
l.extend(l)
print(l)
l.reverse()
print(l)
la=[4,9,67,5]
print(la.sort())
print(la)

di={'a':12,'b':25}''

l2=['where', 'is', 'the', 'plane']
i = 0
while i < len(l2):
    print(l2[i],len(l2[i]))
    i+=1
from collections import deque
stack=[3,4,5]
stack.append(6)
stack.append(7)
stack.pop()
stack
print(stack)
queue=deque(["Eric","John","Michael"])
print(queue.popleft())
print(queue)
squares=[i*i for i in range(10)]
print(squares)

squares2=list(map(lambda x:x**2,range(10)))
print(squares2)'''

def toadd(n):
    n=n+2
    #return n
#print(toadd(5))


def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=" ")
        a,b=b,a+b
    #return n
print(fib(35))