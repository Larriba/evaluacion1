def figura():
    z=input("escribe el tamaño= ")
    
    a="*"
    b=" "
    for i in range(1,z+1):
        n=(2*i)-1
        m=2*i
        if i<4:
            print(i*a)+((z-m)*b)+(i*a)
        if i==4:
            print z*a
        if i>4:
            print((z-(i-1))*a)+((m-(z+2))*b)+((z-(i-1))*a)
                                                
figura()
                        
