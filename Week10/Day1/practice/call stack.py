def func(n: int):
    if n == 0:
        return 
    
    print("Start",n)

    func(n - 1)

    print("End",n)

func(3)