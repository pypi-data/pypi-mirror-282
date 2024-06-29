import sys
from _lib import overload
from typing import Self

class A:
	@overload
	def a(self):print("a", self)
	@overload
	def a(self, a):print("a", self)


a = A()
a.a()
a.a(1)