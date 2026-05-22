def generate(n,path):
    if len(path) == n:
        print(path)
        return
    
    generate(n,path+"0")
    generate(n,path+"1")

print(generate(3,""))