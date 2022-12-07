print("ma = mv^2/r")
print('ma =k m^a x v^b / r^c')
print('k is constant')
a = 0
q = 0
b = 0
c = 0
print("""M = 2.00
v = 5.00
r = 4.00""")
m = 2.00
v = 5.00
r = 4.00
while a < 10:
    c = 0
    b = 0
    a += 1
    while b < 10:
        b += 1
        c = 0
        while c < 10:
            c += 1
            k = (12.5*(r**c))/((m**a)*(v**b))
            print('constant k is' ,k)
            print("for"'( a =',a,')( b =',b,')( c =',c,')')
            Ma = (k*(5**a)*(4**b))/(2**c)
            print("Ma is",Ma)
            print('==========================================================================')
            if Ma == 40.00:
                FG = k
                A = a
                B = b
                C = c
                q = 1
                print('constant valu is',FG)
                print('dimention of constant is ==  N ''m^',c,'Kg^-',a+b,)
                print("found one relation ")
                input("press enter to serch for more")
print('constant valu is',FG)
print('dimention of constant is ==  N ''m^',C,'Kg^-',A+B,)
print("""this will help you to calculate formula of any relation
 you just need to update the setting of the code and
 to give two observation""")
