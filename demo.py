class Demo:
    Count = 0
    
    def __init__(self):
        Demo.Count = Demo.Count+1

def main():
    obj1 = Demo()
    obj2 = Demo()
    
    print(Demo.Count)

if __name__ == "__main__":
    main()





