print('program kulkulator')

l1 = float(input("podal 1 liczbe z przedziualu <-5;101>"))
    
l2 = float(input("podal 2 liczbe z przedziualu <-5;101>"))

while (l1 or l2) <= -5 or (l1 or l2) >= 101:
    print('podano zla wartosc')
    if l2 <= -5 or l2 >= 101:
        l2 = float(input("podal 2poprawna liczbe z przedziualu <-5;101>"))
    elif l1 <= -5 or l1 >= 101:
        l1 = float(input("podal 1 liczbe z przedziualu <-5;101>"))


znak = input('podaj znak +/-')

while znak != '+' and znak != '-':
    print('zly znaak')
    znak = input('podaj poprawny znak +/-')

if znak == '+':
    print(f'{l1} + {l2} = {l1+l2}')
elif znak == '-':
    print(f'{l1} - {l2} = {l1-l2}')
   

  
    