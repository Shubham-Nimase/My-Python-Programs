# Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64


# Power=lambda no:no*no
#
# def main():
#     no=int(input("Enter the number: "))
#     print("Power of two is :",Power(no))
#
# if __name__=="__main__":
#     main()
#


def main():
    value = int(input("Enter Number: "))

    result = lambda x : 2 ** x

    print("The Power of {} is {}".format(value,result(value)))

if __name__ == "__main__":
    main()
