

def display(bpass1, bpass2,im,ic,fm,fc,flag):
    print("\n\n")
    for i in range(0,fm):
        print(" M ",end='') 
    for i in range(0,fc):
        print(" C ",end='') 

    if (flag == 0):
        print("     ~~~~~WATER~~~~~<B0("+str(bpass1)+","+str(bpass2 )+")AT>  ",end='')
    else:
        print("     <BO("+str(bpass1)+","+str(bpass2 )+")AT>~~~~~WATER~~~~~  ",end='')
   
    for i in range(0,im):
        print(" M ",end=''); 
    for i in range(0,ic):
        print(" C ",end=''); 


def win(fc,fm):
    return (fc == 3 and fm == 3) if 0 else 1

def solution():
    im,ic,fm,fc,status,flag,slt = 3,3,0,0,0,0,0 

    while (win(fc,fm)):
        if (flag==0):
            if(slt==1):
                display('C', ' ',im,ic,fm,fc,flag)
                ic+=1
            elif(slt==2):
                display('C', 'M',im,ic,fm,fc,flag)
                ic+=1
                im+=1
            
            if(((im - 2) >= ic and (fm + 2) >= fc) or (im - 2) == 0):
                im = im - 2
                slt = 1
                display('M', 'M',im,ic,fm,fc,flag)
                flag = 1
            elif((ic - 2) < (im and (fm == 0 or (fc + 2) <= fm)) or im == 0):
                ic = ic - 2
                slt = 2
                display('C', 'C',im,ic,fm,fc,flag)
                flag = 1
            else: 
                ic-=1
                im-=1
                fm+=1
                fc+=1
                if ((ic) <= (im) and (fm) >= (fc)):
                    ic = ic - 1
                    im = im - 1
                    slt = 3
                    display('M', 'C',im,ic,fm,fc,flag)
                    flag = 1
        else:
            if(slt==1):
                display('M', 'M',im,ic,fm,fc,flag)
                fm = fm + 2
            
            elif(slt==2):
                display('C', 'C',im,ic,fm,fc,flag)
                fc = fc + 2
            
            elif(slt==3):
                display('M', 'C',im,ic,fm,fc,flag)
                fc = fc + 1
                fm = fm + 1
   
            if (win(fm,fc)):
                if (((fc > 1 and fm == 0) and im == 0)):
                    fc-=1
                    slt = 1
                    display('C', ' ',im,ic,fm,fc,flag)
                    flag = 0
                
                elif ((ic + 2) > im):
                    fc-=1
                    fm-=1
                    slt = 2
                    display('C', 'M',im,ic,fm,fc,flag)
                    flag = 0
    


print("MISSIONARIES AND CANNIBAL SOLUTION")
display(' ', ' ',3,3,0,0,0)
solution()