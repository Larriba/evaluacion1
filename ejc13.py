
def realpiramide():
    a=input("numero de pisos de la piramide ")
    b="*"
    c=" "
    for i in range (1,a+1):
        n=(2*i)-1
        print ((a-i)*c)+(b*n)
realpiramide()
