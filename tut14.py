# string are immutable  
#  meaning of  immutable -----> string change nahi hoga  vo nai string bana dega 

a = "!!!!!ram!!!! !!!!!!!! ram!!!!!!!!!!!!!"
print(a)
print(len(a)) 
print(a.upper())  #-----------------> string a ko change nahi karega a ki nai string ban gayegi 
print(a.lower())  #-----------------> string a ko change nahi karega a ki nai string ban gayegi 
print(a.rstrip("!")) # ----------------> eleminate the last ! mark
print(a.replace("ram" , "mohit "))  # --------------------> replace harry with mohit at all place 
print(a.split(" ")) # split the string and make in list from 
b = "rohan  is KJ4 for std"
print(b.capitalize()) # they are only convert first letter in capital and left in covert into small letter 
str1 = "welcome to the console !!!"
print (len(str1))       # -----------> lenth of the  string 
print (str1.center(70)) # -----------> center ki aur puri string ho gayegi 
print (len(str1.center(50))) 
print (a.count("ram ")) #  --------------> count ram in program
print (a.endswith("!!!")) # -----------------> if string end with !!! then give true otherwise false
print(str1.endswith("to" , 4 ,10)) # -----------> true if the string end 4 -10 letter between  with "to" otherwise
str2 = "he's name is dan . he is an honest man "

print(str2.find("is ")) # -----------------------> ye batayega ki is kaha lika he 
print(str2.find("ishh ")) # -----------------------> ishh nahi hoga to return -1
#print(str2.index("ishh ")) # -----------------------> ishh nahi hoga to error milega


print ("----------------------------------------------------------------------")
str2 = "welcone in my world "

print(str2.isalnum())
print(str2.isalpha())


str2 = "welcome524"
print(str2.isalnum())
print(str2.isalpha())

print (str2.islower())

str3 = "is caracter are printable "

print(str3.isprintable())



str3 = "    is   caracter are printable    \n "

print(str3.isprintable())
str3 = "          "
print(str3.isspace())

str3  = " jhklhkjhhfiuhyihjhj"
print(str3.isspace())

print(str2.istitle())


str4 = " python is covered by me "
print(str4.startswith(" python"))
print(str4.swapcase())

print(str4.title())



