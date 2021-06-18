
def ChkPrime(List):

    sum=0
    for i in range(len(List)):
        no=List[i]
        if no>1:
            flag=True
            for j in range(2,int(no/2)+1):
                if no%j==0:
                    flag=False
                    break
            if flag:
                sum=sum+no
    return sum