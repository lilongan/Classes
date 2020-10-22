first = 'look only single quotes'
second = "A string with double quotes"
third = '''
I want to cross spaces
now I am down here
'''

fourth = """This is going to
be 
spaced down"""

print("hello"+" "+"world")

#Very bad not working
# bob = "YES!"
# bob =  42 + bob

message = "Hello World!"
name = "黎明"

#f string
combined = f"I want to say {message} to {name}."
print(f"I want to say {message} to {name}.")

#
adj = "Awesome"
#new_string = "Hey this is %s, and  I like it" % thing
print("Hey this is %s, and  I like it" % adj)

print("I want to tell %s %s and Hey this is %s" % (name,message,adj))

haiku = "\tHaikus are easy.\nBut sometimes they don't make sense.\n\tRefrigerator."
print(haiku)