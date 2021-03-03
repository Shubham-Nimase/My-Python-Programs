# Accept  N numbers from user and return addition of that N numbers
def AdditionX(LIST):
    sum = 0
    i = 0
    while i < len(LIST):
        sum = sum + LIST[i]
        i = i + 1
    return sum

def Addition(LIST):
    sum = 0
    for i in range(len(LIST)):
        sum = sum + LIST[i]
    return sum
    
def main():
    arr = []
    print("Enter the number of elements")
    size = int(input())
    
    for i in range(size):
        print("Enter the element no : ",i + 1)
        value = int(input())
        arr.append(value)
        
    print("Accepted data is : ",arr)
    
    ret = Addition(arr)
    
    print("Addition of all ements is : ",ret)
    
if __name__ == "__main__":
    main()
