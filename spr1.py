n = int(input('podaj jak długi jest jest ciąg'))

while n <= 0:
    print('ZZZZZZZZZZZZZZZLLLLLLLLLLLLLLEEEEEEEEEEEEE')
    n = int(input('podaj jak długi jest jest ciąg MA BYC WIEKSZE OD 0'))
w=1  
k = 20
i = n
while i > 0:
    w *= k
    if i % 2 == 0:
        k -= 1
    else:
        k -=2
    i -= 1
print(w)