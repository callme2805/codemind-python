t=int(input())
for i in range(1,t+1):
    n=int(input())
    prev_prime=n
    while True:
        p_fc=0
        for k in range(1,prev_prime+1):
            if prev_prime%k==0:
                p_fc+=1
        if p_fc==2:
            break
        prev_prime-=1
    next_prime=n+1
    while True:
        n_fc=0
        for j in range(1,next_prime+1):
            if next_prime%j==0:
                n_fc+=1
        if n_fc==2:
            break
        next_prime+=1
    if n-prev_prime==next_prime-n:
        print(min(prev_prime,next_prime))
    elif n-prev_prime<next_prime-n:
        print(prev_prime)
    else:
        print(next_prime)
  
        
                
        