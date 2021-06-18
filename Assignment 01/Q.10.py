# Write a program which accept name from user and display length of its name.
# Input : Marvellous
# Output : 10


def Length(str):
    #print(len(str))

    # icnt=0
    # for i in range(1,len(str)+1,1):
    #     icnt=icnt+i
    # print(i)

     icnt=0
     for i in str:
         icnt=icnt+1
     print(icnt)

def Main():
    str=(input("ENter the any Word : "))
    Length(str)

if __name__=="__main__":
    Main()