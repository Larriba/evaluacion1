def ajedrez():
    a=input("numero de filas y columnas")
    b="*"
    c=" "
    for i in range(1,a+1):
        if i%2==0:
            print (b+c)*a
        else:
            print (c+b)*a
ajedrez()
