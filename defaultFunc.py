#	defaultFunction.py 
#	I'm getting a few errors so I just need to get this syntax down right 
# 	code from this site: https://www.programiz.com/python-programming/function-argument
def greet(name, msg = "Good morning!"):
   """
   This function greets to
   the person with the
   provided message.

   If message is not provided,
   it defaults to "Good
   morning!"
   """

   print("Hello",name + ', ' + msg)

greet("Kate")
greet("Bruce","How do you do?")
