def cuenta_primos():
    a=input ("contaremos desde este numero= ")
    x=input("contaremos hasta este numero= ")
    primo=True
    for i in range (a,x+1):
        for b in range(2,i-1):
            if (i%b==0):
                primo=False
        if(primo==True):
            print i,"primo"
        else:
            print i,"no es primo"
        primo=True
cuenta_primos()

            
        
