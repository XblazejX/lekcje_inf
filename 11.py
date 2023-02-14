# ciag liczb

'''n = int(input('podaj liczbe liczb'))
while n < 1:
    n = int(input('nie można podac na minusie głąbie'))
k = 4

for i in range(n):
    print(k,end=" * ")
    if k > 0:
        k += 4
    else:
        k -= 4
    
    k *= -1'''
    
'''n = int(input('podaj liczbe liczb'))
while n < 1:
    n = int(input('nie można podac na minusie głąbie'))
k = 1

for i in range(n):
    print(k,end=" , ")
    if k > 0:
        k *= 2
    else:
        k *= 2
    
    k *= -1
print(k)'''

n = int(input('podaj liczbe liczb'))
while n < 1:
    n = int(input('nie można podac na minusie głąbie'))
k = 7
s = 0
print(k, end=" , ")
for i in range(n):
    if s % 3 != 0:
        k += 1
    else:
        k += 2
    print(k, end=" , ")
    s +=1