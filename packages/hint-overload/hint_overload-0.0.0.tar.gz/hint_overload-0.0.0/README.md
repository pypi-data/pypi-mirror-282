# overload

this allows for overloads based upon type hints amongst other things

```py
#just use @overload
@overload
def a()->None:
	"""this one prints 1st and returns none"""
	print("1st")
@overload
def a(a):print("2nd")
@overload
def a(a,b,*args):print("3rd")

a() # prints 1st
a(0) # prints 2nd
a(a=0) # prints 2nd
a(0,1,2,3,4,5) # prints 3rd
```