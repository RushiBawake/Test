
z=[]
y=[]
def Something(input1,input2,input3):
    if input1%2==0:
        for i in range(0,input1-1,2):
            a=input2[i]+input2[i+1]
            b=a*input3
            y.append(b)
            z.append(a)
        c=sum(z)*input3
        d=sum(y)
        print(c+d)
    elif input1%2==1:
        for i in range(0,input1-2,2):
            a=input2[i]+input2[i+1]
            b=a*input3
            y.append(b)
            z.append(a)
        e=(input2[input1-1]+input2[input1-1])*input3
        c=sum(z)*input3
        d=sum(y)
        print(e+d)
    
if __name__=="__main__":

    l=[2,3,1]
    Something(3,l , 2)
    """
    l=[4,5,6,7]
    Something(4,l , 3)
    """
