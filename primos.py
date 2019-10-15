def primos ():
    a=input ("rapidito ")
    primo=True
    for i in range (2,a):
        if (a%i==0):
            primo=False
    if(primo==True):
        print "es primo"
    else:
        print "no es primo"
    

primos()
  
