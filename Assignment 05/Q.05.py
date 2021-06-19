# Write a recursive program which accept number from user and return its
# factorial.
# Input : 5
# Output : 120

fact=1
def factorial(no):
    global fact
    if no>0:
        fact = fact * no
        no= no - 1
        factorial(no)
    return fact

def main():
    no=int(input("Enter the Number: "))
    ret=factorial(no)
    print("Factorial is:",ret)

if __name__=="__main__":
    main()