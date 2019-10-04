#en este programa le pedimos al usuario
#teclee los coeficientes de un polinomio
#y hallamos el valor de las raices
def ecuacion():
    print"introduzca los coeficientes de el polinomio"
    print"A*x^2+B*x+C"
    a=input("A= ")
    b=input("B= ")
    c=input("C= ")
    raiz1=(-b+((b*b-4*a*c)^(1/2)))/(2*a)
    raiz2=(-b-((b*b-4*a*c)^(1/2)))/(2*a)
    ((b*b-4*a*c)^(1/2))=p
    if(p>0):
        print"no existe"
    print"primera solucion=" +raiz1
    print"segunda solucion=" +raiz2
    
ecuacion()


    
