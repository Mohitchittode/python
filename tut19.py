for i in range(12):
    
    print("5 X" , i+1 , "=" , 5*(i+1))  

print(" loop ko chod ke bahar aa gao ")

print(" next code ")
for i in range(12):
    if(i == 10):
        break
    print("5 X" , i+1 , "=" , 5*(i+1))  

print(" loop ko chod ke bahar aa gao ")

print(" next 2 nd programme ")
for i in range(12):
    if(i == 10):
        continue
    print("5 X" , i , "=" , 5*(i+1))  

print(" loop ko chod ke bahar aa gao ")
 
j = 0
while True:
    print(j)
    j = j + 1
    if(j%100 == 0):
        break



