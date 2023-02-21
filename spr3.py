n = int(input('podaj jak długi jest jest ciąg'))
a = 4
w=1
for i in range(n):
    w *= a
    if a < 0:
        a*=-1
        a += 4
    else:
        a +=4
        a*=-1
        
print(w)