def fact(num):
    res = 1
    for num in range(1,num + 1):
        res = res * num
    print("El Factorial de",num,"es:",res)    

fact(5)    
