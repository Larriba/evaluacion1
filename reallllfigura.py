def realfigura():
    z=input("escribe el tamano(numero impar)= ")
    
    a="*"
    b=" "
    k=((z/2)+1/2)
    for i in range(1,z+1):
        n=(2*i)-1
        m=2*i
        if i<(k+1):
            print(i*a)+((z-m)*b)+(i*a)
        if i==k:
            print z*a
        if i>(k+1):
            print((z-(i-1))*a)+((m-(z+2))*b)+((z-(i-1))*a)
realfigura()
