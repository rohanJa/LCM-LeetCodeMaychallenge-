first = [1, 2, 3]
copyList = first
second = first.copy() 

first.append(4)
first.append(9)
first.pop(0)
# both copyList and second will contain the copy of 'first' list
# But differnce is that changes in 'first' is shown in copyList 
# but if we use 'copy()' method to copy the list 'second' list
# and no changes will be shown in the 'second' list
print("copyList "+str(copyList)) 
print('Second '+str(second))