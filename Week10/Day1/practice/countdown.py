def countdown(n: int):
    if n == 0:
        return 
    
    print(n)

    countdown(n-1)

print(countdown(3))