
def ele(x):
    element = font
    for i in range(0,x):
        print("%c"%(element),end="")
        i=i+1

def emp(x):
    for i in range(0,x):
        print(" ",end="")
        i=i+1

def Render(str,left,right,font):
    for height in range(0,7):
        i = left
        for i in range(left,right+1):
            c=str[i]
            if c=='a' or c=="A":
                if height==0:
                    emp(4)
                    ele(3)
                    emp(6)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(1)
                    ele(3)
                    emp(4)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(3)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==5:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==6:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)

            if c=='b' or c=='B':
                if height==0:
                    ele(10)
                    emp(3)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(2)
                    emp(2)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(2)
                    emp(2)
                if height==3:
                    ele(9)
                    emp(4)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(2)
                    emp(2)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(2)
                    emp(2)
                if height==6:
                    ele(10)
                    emp(3)

            if c=='c' or c=='C':
                if height==0:
                    emp(3)
                    ele(7)
                    emp(3)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(8)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(9)
                if height==3:
                    ele(3)
                    emp(10)
                if height==4:
                    emp(1)
                    ele(3)
                    emp(9)
                if height==5:
                    emp(2)
                    ele(3)
                    emp(8)
                if height==6:
                    emp(3)
                    ele(7)
                    emp(3)

            if c=='d' or c=='D':
                if height==0:
                    ele(9)
                    emp(4)
                if height==1:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(3)
                    emp(7)
                    ele(2)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==6:
                    ele(9)
                    emp(4)

            if c=='e' or c=='E':
                if height==0:
                    ele(11)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(10)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    ele(3)
                    emp(10)
                if height==5:
                    ele(3)
                    emp(10)
                if height==6:
                    ele(11)
                    emp(2)

            if c=='f' or c=='F':
                if height==0:
                    ele(11)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(10)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(7)
                    emp(6)
                if height==4:
                    ele(3)
                    emp(10)
                if height==5:
                    ele(3)
                    emp(10)
                if height==6:
                    ele(3)
                    emp(10)

            if c=='g' or c=='G':
                if height==0:
                    ele(11)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(3)
                    emp(2)
                    ele(6)
                    emp(2)
                if height==4:
                    ele(3)
                    emp(2)
                    ele(2)
                    emp(1)
                    ele(3)
                    emp(2)
                if height==5:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==6:
                    ele(11)
                    emp(2)

            if c=='h' or c=='H':
                if height==0:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==2:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==5:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==6:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)

            if c=='i' or c=='I':
                if height==0:
                    emp(3)
                    ele(7)
                    emp(3)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(3)
                    ele(7)
                    emp(3)

            if c=='j' or c=='J':
                if height==0:
                    emp(3)
                    ele(8)
                    emp(2)
                if height==1:
                    emp(3)
                    ele(2)
                    emp(3)
                    ele(3)
                    emp(2)
                if height==2:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==3:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==4:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==5:
                    ele(2)
                    emp(6)
                    ele(3)
                    emp(2)
                if height==6:
                    ele(11)
                    emp(2)

            if c=='k' or c=='K':
                if height==0:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(4)
                    ele(3)
                    emp(3)
                if height==2:
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(5)
                if height==3:
                    ele(6)
                    emp(7)
                if height==4:
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(5)
                if height==5:
                    ele(3)
                    emp(4)
                    ele(3)
                    emp(3)
                if height==6:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)

            if c=='l' or c=='L':
                if height==0:
                    ele(5)
                    emp(8)
                if height==1:
                    ele(3)
                    emp(10)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(3)
                    emp(10)
                if height==4:
                    ele(3)
                    emp(10)
                if height==5:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)
                if height==6:
                    ele(11)
                    emp(2)

            if c=='m' or c=='M':
                if height==0:
                    ele(4)
                    emp(4)
                    ele(4)
                    emp(1)
                if height==1:
                    ele(5)
                    emp(2)
                    ele(5)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(1)
                    ele(4)
                    emp(1)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(3)
                    emp(2)
                    ele(2)
                    emp(2)
                    ele(3)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)

            if c=='n' or c=='N':
                if height==0:
                    ele(4)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==1:
                    ele(5)
                    emp(4)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(1)
                    ele(2)
                    emp(3)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(3)
                    emp(2)
                    ele(2)
                    emp(2)
                    ele(3)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(3)
                    ele(2)
                    emp(1)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(4)
                    ele(5)
                    emp(1)
                if height==6:
                    ele(3)
                    emp(5)
                    ele(4)
                    emp(1)

            if c=='o' or c=='O':
                if height==0:
                    emp(4)
                    ele(5)
                    emp(4)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(2)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==3:
                    emp(1)
                    ele(2)
                    emp(7)
                    ele(2)
                    emp(1)
                if height==4:
                    emp(1)
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==5:
                    emp(2)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(2)
                if height==6:
                    emp(4)
                    ele(5)
                    emp(4)

            if c=='p' or c=='P':
                if height==0:
                    ele(11)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    ele(3)
                    emp(10)
                if height==5:
                    ele(3)
                    emp(10)
                if height==6:
                    ele(3)
                    emp(10)

            if c=='q' or c=='Q':
                if height==0:
                    emp(4)
                    ele(5)
                    emp(4)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(2)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==3:
                    emp(1)
                    ele(2)
                    emp(7)
                    ele(2)
                    emp(1)
                if height==4:
                    emp(1)
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==5:
                    emp(2)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(2)
                if height==6:
                    emp(4)
                    ele(5)
                    emp(1)
                    ele(2)
                    emp(1)

            if c=='r' or c=='R':
                if height==0:
                    ele(11)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    ele(7)
                    emp(6)
                if height==5:
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(4)
                if height==6:
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(2)

            if c=='s' or c=='S':
                if height==0:
                    ele(12)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(10)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(12)
                    emp(1)
                if height==4:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==5:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(12)
                    emp(1)

            if c=='t' or c=='T':
                if height==0:
                    ele(13)
                if height==1:
                    ele(2)
                    emp(3)
                    ele(3)
                    emp(3)
                    ele(2)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(4)
                    ele(5)
                    emp(4)
            i=i+1

            if c=='u' or c=='U':
                if height==0:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(12)
                    emp(1)

            if c=='v' or c=='V':
                if height==0:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(4)
                    ele(3)
                    emp(2)
                if height==3:
                    emp(2)
                    ele(2)
                    emp(4)
                    ele(2)
                    emp(3)
                if height==4:
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(4)
                if height==5:
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(4)
                if height==6:
                    emp(4)
                    ele(4)
                    emp(5)

            if c=='w' or c=='W':
                if height==0:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(3)
                    emp(2)
                    ele(2)
                    emp(2)
                    ele(3)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(1)
                    ele(4)
                    emp(1)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(5)
                    emp(2)
                    ele(5)
                    emp(1)
                if height==6:
                    ele(4)
                    emp(4)
                    ele(4)
                    emp(1)

            if c=='x' or c=='X':
                if height==0:
                    ele(4)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(3)
                if height==2:
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(4)
                if height==3:
                    emp(4)
                    ele(4)
                    emp(5)
                if height==4:
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(4)
                if height==5:
                    emp(2)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(3)
                if height==6:
                    ele(4)
                    emp(5)
                    ele(3)
                    emp(1)

            if c=='y' or c=='Y':
                if height==0:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(3)
                if height==2:
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(4)
                if height==3:
                    emp(4)
                    ele(3)
                    emp(6)
                if height==4:
                    emp(4)
                    ele(3)
                    emp(6)
                if height==5:
                    emp(4)
                    ele(3)
                    emp(6)
                if height==6:
                    emp(2)
                    ele(7)
                    emp(4)

            if c=='z' or c=='Z':
                if height==0:
                    ele(12)
                    emp(1)
                if height==1:
                    emp(8)
                    ele(4)
                    emp(1)
                if height==2:
                    emp(6)
                    ele(4)
                    emp(3)
                if height==3:
                    emp(4)
                    ele(4)
                    emp(5)
                if height==4:
                    emp(2)
                    ele(4)
                    emp(7)
                if height==5:
                    ele(4)
                    emp(9)
                if height==6:
                    ele(12)
                    emp(1)
            if c=='0':
                if height==0:
                    ele(12)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(12)
                    emp(1)

            if c=='1':
                if height==0:
                    emp(2)
                    ele(6)
                    emp(5)
                if height==1:
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(3)
                    ele(7)
                    emp(3)

            if c=='2':
                if height==0:
                    emp(1)
                    ele(10)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(2)
                    emp(6)
                    ele(3)
                    emp(2)
                if height==3:
                    emp(6)
                    ele(3)
                    emp(4)
                if height==4:
                    emp(3)
                    ele(3)
                    emp(7)
                if height==5:
                    emp(1)
                    ele(3)
                    emp(9)
                if height==6:
                    emp(1)
                    ele(11)
                    emp(1)

            if c=='3':
                if height==0:
                    emp(1)
                    ele(10)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==3:
                    emp(7)
                    ele(5)
                    emp(1)
                if height==4:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==6:
                    emp(1)
                    ele(10)
                    emp(2)
                    
            if c=='4':
                if height==0:
                    emp(6)
                    ele(5)
                    emp(2)
                if height==1:
                    emp(4)
                    ele(3)
                    emp(1)
                    ele(3)
                    emp(2)
                if height==2:
                    emp(3)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(2)
                if height==3:
                    emp(2)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(2)
                if height==4:
                    emp(1)
                    ele(12)
                    emp(0)
                if height==5:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==6:
                    emp(8)
                    ele(3)
                    emp(2)
                    
            if c=='5':
                if height==0:
                    ele(10)
                    emp(3)
                if height==1:
                    ele(3)
                    emp(10)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==5:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(11)
                    emp(2)
                    
            if c=='6':
                if height==0:
                    ele(11)
                    emp(2)
                if height==1:
                    ele(3)
                    emp(10)
                if height==2:
                    ele(3)
                    emp(10)
                if height==3:
                    ele(11)
                    emp(2)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(11)
                    emp(2)
                    
            if c=='7':
                if height==0:
                    emp(2)
                    ele(10)
                    emp(1)
                if height==1:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==2:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==3:
                    emp(4)
                    ele(6)
                    emp(3)
                if height==4:
                    emp(6)
                    ele(3)
                    emp(4)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(4)
                    ele(3)
                    emp(6)
                    
            if c=='8':
                if height==0:
                    ele(12)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(12)
                    emp(1)
                if height==4:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(12)
                    emp(1)
                    
            if c=='9':
                if height==0:
                    ele(12)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(6)
                    ele(3)
                    emp(1)
                if height==3:
                    ele(12)
                    emp(1)
                if height==4:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==5:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(12)
                    emp(1)
                    
            if c=='+':
                if height==0:
                    emp(13)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(1)
                    ele(11)
                    emp(1)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(13)
                    
            if c=='-':
                if height==0:
                    emp(13)
                if height==1:
                    emp(13)
                if height==2:
                    emp(13)
                if height==3:
                    emp(1)
                    ele(11)
                    emp(1)
                if height==4:
                    emp(13)
                if height==5:
                    emp(13)
                if height==6:
                    emp(13)
                    
            if c=='*':
                if height==0:
                    emp(13)
                if height==1:
                    emp(1)
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==2:
                    emp(3)
                    ele(3)
                    emp(1)
                    ele(3)
                    emp(3)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(3)
                    ele(3)
                    emp(1)
                    ele(3)
                    emp(3)
                if height==5:
                    emp(1)
                    ele(3)
                    emp(5)
                    ele(3)
                    emp(1)
                if height==6:
                    emp(13)
                    
            if c=='/':
                if height==0:
                    ele(13)
                if height==1:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==2:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==3:
                    emp(7)
                    ele(3)
                    emp(3)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(4)
                    ele(3)
                    emp(6)
                if height==6:
                    emp(3)
                    ele(3)
                    emp(7)
                    
            if c=='=':
                if height==0:
                    emp(13)
                if height==1:
                    emp(13)
                if height==2:
                    emp(1)
                    ele(11)
                    emp(1)
                if height==3:
                    emp(13)
                if height==4:
                    emp(1)
                    ele(11)
                    emp(1)
                if height==5:
                    emp(13)
                if height==6:
                    emp(13)
                    
            if c=='"':
                if height==0:
                    emp(2)
                    ele(4)
                    emp(1)
                    ele(4)
                    emp(2)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(3)
                if height==2:
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(4)
                if height==3:
                    emp(5)
                    ele(1)
                    emp(3)
                    ele(1)
                    emp(3)
                if height==4:
                    emp(13)
                if height==5:
                    emp(13)
                if height==6:
                    emp(13)
                    
            if c=='"':
                if height==0:
                    emp(2)
                    ele(4)
                    emp(1)
                    ele(4)
                    emp(2)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(3)
                if height==2:
                    emp(4)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(3)
                if height==3:
                    emp(3)
                    ele(1)
                    emp(3)
                    ele(1)
                    emp(5)
                if height==4:
                    emp(13)
                if height==5:
                    emp(13)
                if height==6:
                    emp(13)
                    
            if c=='!':
                if height==0:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(13)
                if height==6:
                    emp(5)
                    ele(3)
                    emp(5)
                    
            if c=='#':
                if height==0:
                    emp(5)
                    ele(2)
                    emp(4)
                    ele(2)
                if height==1:
                    emp(4)
                    ele(2)
                    emp(4)
                    ele(2)
                    emp(1)
                if height==2:
                    ele(13)
                if height==3:
                    emp(2)
                    ele(2)
                    emp(4)
                    ele(2)
                    emp(3)
                if height==4:
                    ele(13)
                if height==5:
                    ele(2)
                    emp(4)
                    ele(2)
                    emp(5)
                if height==6:
                    ele(1)
                    emp(4)
                    ele(2)
                    emp(6)
                    
            if c=='&':
                if height==0:
                    ele(12)
                    emp(1)
                if height==1:
                    ele(3)
                    emp(3)
                    ele(2)
                    emp(2)
                    ele(2)
                    emp(1)
                if height==2:
                    ele(3)
                    emp(3)
                    ele(2)
                    emp(5)
                if height==3:
                    ele(12)
                    emp(1)
                if height==4:
                    emp(6)
                    ele(2)
                    emp(1)
                    ele(3)
                    emp(1)
                if height==5:
                    ele(2)
                    emp(4)
                    ele(2)
                    emp(1)
                    ele(3)
                    emp(1)
                if height==6:
                    ele(12)
                    emp(1)
                    
            if c=='%':
                if height==0:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==1:
                    emp(1)
                    ele(3)
                    emp(3)
                    ele(3)
                    emp(3)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(2)
                    ele(3)
                    emp(4)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(4)
                    ele(3)
                    emp(3)
                    ele(3)
                if height==5:
                    emp(3)
                    ele(3)
                    emp(4)
                    ele(3)
                if height==6:
                    emp(2)
                    ele(3)
                    emp(8)
                    
            if c=='(':
                if height==0:
                    emp(3)
                    ele(4)
                    emp(6)
                if height==1:
                    emp(2)
                    ele(3)
                    emp(8)
                if height==2:
                    emp(1)
                    ele(3)
                    emp(9)
                if height==3:
                    ele(3)
                    emp(10)
                if height==4:
                    emp(1)
                    ele(3)
                    emp(9)
                if height==5:
                    emp(2)
                    ele(3)
                    emp(8)
                if height==6:
                    emp(3)
                    ele(4)
                    emp(6)
                    
            if c==')':
                if height==0:
                    emp(6)
                    ele(4)
                    emp(3)
                if height==1:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==2:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==3:
                    emp(10)
                    ele(3)
                if height==4:
                    emp(9)
                    ele(3)
                    emp(1)
                if height==5:
                    emp(8)
                    ele(3)
                    emp(2)
                if height==6:
                    emp(6)
                    ele(4)
                    emp(3)
                    
            if c==':':
                if height==0:
                    emp(13)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(13)
                if height==3:
                    emp(13)
                if height==4:
                    emp(13)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(13)
                    
            if c==';':
                if height==0:
                    emp(13)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(13)
                if height==3:
                    emp(13)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(6)
                    ele(2)
                    emp(5)
                if height==6:
                    emp(6)
                    ele(1)
                    emp(6)
                    
            if c==',':
                if height==0:
                    emp(13)
                if height==1:
                    emp(13)
                if height==2:
                    emp(13)
                if height==3:
                    emp(13)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(6)
                    ele(2)
                    emp(5)
                if height==6:
                    emp(6)
                    ele(1)
                    emp(6)
                    
            if c=='.':
                if height==0:
                    emp(13)
                if height==1:
                    emp(13)
                if height==2:
                    emp(13)
                if height==3:
                    emp(13)
                if height==4:
                    emp(13)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(13)
                    
            if c=='?':
                if height==0:
                    emp(1)
                    ele(11)
                    emp(1)
                if height==1:
                    emp(1)
                    ele(3)
                    emp(4)
                    ele(4)
                    emp(1)
                if height==2:
                    emp(2)
                    ele(1)
                    emp(4)
                    ele(3)
                    emp(3)
                if height==3:
                    emp(6)
                    ele(3)
                    emp(4)
                if height==4:
                    emp(6)
                    ele(3)
                    emp(4)
                if height==5:
                    emp(13)
                if height==6:
                    emp(6)
                    ele(3)
                    emp(4)
                    
            if c=='[':
                if height==0:
                    emp(5)
                    ele(6)
                    emp(2)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(5)
                    ele(6)
                    emp(2)
                    
            if c=='[':
                if height==0:
                    emp(2)
                    ele(6)
                    emp(5)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(2)
                    ele(6)
                    emp(5)
                    
            if c=='{':
                if height==0:
                    emp(5)
                    ele(6)
                    emp(2)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(2)
                    emp(6)
                if height==3:
                    emp(3)
                    ele(3)
                    emp(7)
                if height==4:
                    emp(5)
                    ele(2)
                    emp(6)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(5)
                    ele(6)
                    emp(2)
                    
            if c=='}':
                if height==0:
                    emp(2)
                    ele(6)
                    emp(5)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(6)
                    ele(2)
                    emp(5)
                if height==3:
                    emp(7)
                    ele(3)
                    emp(3)
                if height==4:
                    emp(6)
                    ele(2)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(2)
                    ele(6)
                    emp(5)
                    
            if c=='|':
                if height==0:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==1:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==2:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==3:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==4:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==5:
                    emp(5)
                    ele(3)
                    emp(5)
                if height==6:
                    emp(5)
                    ele(3)
                    emp(5)
                break
            # else:
            #     if height==0:
            #         emp(13)
            #     if height==1:
            #         emp(13)
            #     if height==2:
            #         emp(13)
            #     if height==3:
            #         emp(13)
            #     if height==4:
            #         emp(13)
            #     if height==5:
            #         emp(13)
            #     if height==6:
            #         emp(13)

            i=i+1
        print("\n",end="")
        height=height+1
    for i in range(0,4):
        print("\n",end="")
        i=i+1

def printf(str,font):
    i=len(str)
    left = 0
    right = 0
    for j in range(0,i):
        if str[j] != " ":
            right = j
        else:
            Render(str,left,right,font)
            left = right+1
        j=j+1
    Render(str,left,right,font)


font = "|"







# make another .py file and enter this code and store this let.py to this folder


# from let import *
# str = "Type anything"
# printf(str,font)