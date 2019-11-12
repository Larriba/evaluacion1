def ejc7():
        a=input("primer numero entero ")
        b=input("segundo numero entero ")
        c=raw_input("escribe una letra ")
        if c=="s":
            print a+b
        if c=="r":
            print a-b
        if c=="m":
            print a*b
        if c=="d":
                if b==0:
                        j=input("otro numero")
                        print a/j
                else:
                        print a/b
        
ejc7()
