# Iterative approach
def StartDynamic(No,message="Jay Ganesh"):
    iCnt = 0
    while iCnt < No:
        print(message)
        iCnt = iCnt + 1
        
def Display(No):
    print("Jay Ganesh" * No)
    
def main():
    print("Enter number of times you want to display message on screen")
    value = int(input())
    print("Enter the message")
    name = input()
    
    StartDynamic(value,name)
    
    StartDynamic(value)
    
    Display(value)
    
if __name__ == "__main__":
    main()
