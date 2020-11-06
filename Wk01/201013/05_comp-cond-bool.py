#Using comparision operators
print(1 == 2)   #False
print(1 <  2)   #True
print(1 >  2)   #False
print(1 >= 1)   #True
print(1 <= 2)   #True
print(1 != 1)   #False

a = 1
b = 2
print(a == b) #false

name = "黎明"
print(name != "George")
print(name == "黎明")
print(name > "A")

if 1 < 3:
    print('This is the same level')
    print("This will be printed")
    print("More stuff")

did_do_something = True

if None:
    print('None is never printed')

if did_do_something:
    print("Yeah you did something")

if 0:
    print("0 is a falsy statement")

if 1:
    print("1 is a truthy statement")

something_at_all = {}

#Falsy statements
None    #Falsy
False   #Falsy
0       #Falsy
""      #Falsy
[]      #Falsy
{}      #Falsy

if something_at_all:
    print(something_at_all)