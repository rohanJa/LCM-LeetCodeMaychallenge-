star = []
size = int(input())

for i in range(3):
    star.append(list(str(input()).replace(' ','')))

answer=''
print(len(star[0]))
i=0
while(i<size):
    print("For i = "+str(i)) 
    print(str(star[1][i])+str(star[1][i+1])+str(star[1][i+2]))
    if(star[0][i]=='#' and star[1][i]=='#' and star[2][i]=='#'):
        i+=1
        answer+='#'
        continue
    elif(star[0][i]=='.' and star[1][i]=='.' and star[2][i]=='.'):
        i+=1
        continue

    elif(star[1][i]=='*' and star[1][i+1]=='.' and star[1][i+2]=='*'):
        
        if(star[0][i+1]=='.'):
            answer+='U'
        else:
            answer+='O'
        i+=3
        continue
    elif(star[1][i]=='.' and star[1][i+1]=='*' and star[1][i+2]=='.'):
        answer+='I'
        i+=3
        continue
    elif(star[1][i]=='*' and star[1][i+1]=='*' and star[1][i+2]=='*' and star[2][i+1]=='.'):
        answer+='A'
        i+=3
        continue
    else:
        answer+='E'
        i+=3
        continue
print(answer)