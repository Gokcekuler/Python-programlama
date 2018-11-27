def asalçarpanlar(N):
    çarpanlar=[]    
    x =2
    while N > 1:
        
        asal = True
        i = 2
        while i*i <= x:
            if x % i ==0:
                asal = False
                break
            i += 1

        if asal and N % x == 0:
            çarpanlar.append(x)  
            while N % x == 0:
                N = N/x        
        x += 1
    return çarpanlar
