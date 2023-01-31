print('lekcja 12_1')

print('wprowadz 2 liczby z przedzialu <0,1000> i <0,100>')

l1 = float(input('podaj liczbe z przedzialu <0,1000>\n'))

while l1 < 0 or l1 > 1000:
    print('wprowadziles zla liczbe')
    l1 = float(input('podaj ppoprawna liczbe z przedzialu <0,1000>\n'))

l2 = float(input('podaj kolejna liczbe z przedzialu <0,100>\n'))

while l2 < 0 or l2 > 100:
    print('wprowadziles zla liczbe')
    l2 = float(input('podaj poprawna 2 liczbe z przedzialu <0,100>\n'))

znak = input('podaj co chcesz zrobic z tymi liczbami: "-","+","/","*","**" ')

while znak != "-" and znak !="+" and znak !="/" and znak !="*" and znak !="**":
    print("ZLEEEEEE")
    znak = input('podaj poprawnie LAMO co chcesz zrobic z tymi liczbami: "-","+","/","*","**" ')


if znak == '-':
    print(f'{l1} - {l2} = {l1-l2}')
elif znak == '+':
    print(f'{l1} + {l2} = {l1+l2}')
elif znak == '/':
    print(f'{l1} / {l2} = {l1/l2}')
elif znak == '*':
    print(f'{l1} * {l2} = {l1*l2}')
elif znak == '**':
    print(f'{l1} ** {l2} = {l1**l2}')

print("konieccccc programu")

