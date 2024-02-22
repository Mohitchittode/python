name = input()
friend = input()
anotherfriend = "ram"
more_line = ''' he said , hi  

i
 am  
 good 
 "i want to eat an apple '''
print(name+friend) 
print(name[0])     #--------------!
print(name[1])     #              !
print(name[2])     #              !----------------> acess the name variable string word by word 
                   #              !                     SYNTAX -----> print(variable[no of letter which we can acess]  )
print(name[3])     #              !
print(name[4])     #--------------!

# print(name[5]) # throw an error 

print("lets use a for loop \n")
for character in name: #-------------------------!
                       #                         !---------------> print letter by letter using for loop in python 
    print(character)   #-------------------------!


for character in more_line:
    print(character)


