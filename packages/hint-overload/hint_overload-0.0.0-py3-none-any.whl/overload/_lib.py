from typing import Callable
from dataclasses import dataclass
import inspect
from inspect import Parameter
from type_hint_checker import are_type_compatible
import functools
from types import MethodType

class OverloadSelectionError(Exception):
	"""TODO ALL DOCS"""

@dataclass
class _FnSig:
	fn: Callable
	@property
	def sig(self):
		if not hasattr(self, "_sig"):self._sig = inspect.signature(self.fn)
		return self._sig
	def __call__(self, *args, **kwargs): self.fn(*args, **kwargs)

class overload:
	def __new__(cls, fn):
		last_frame = inspect.currentframe().f_back
		pre_existing = last_frame.f_locals.get(fn.__name__)
		ns = last_frame.f_globals | last_frame.f_locals
		if isinstance(pre_existing, overload):
			pre_existing.add_overload(fn)
			pre_existing._ns |= ns
			return pre_existing
		rv = object.__new__(cls)
		rv._ns = ns
		return rv
	def __init__(self, fn):
		if hasattr(self, "_functions"):return
		self._functions = [_FnSig(fn)]
		functools.update_wrapper(self, fn, assigned=('__module__', '__name__', '__qualname__'))
	def add_overload(self, fn):
		self._functions.append(_FnSig(fn))
	@property
	def __annotations__(self):
		if len(self._functions) == 1: return self._functions[0].__annotations__
		# dont give any annotations here.
		# there might be a way to notate overloaded arguments in annotations but this
		# will do for now
		return {}
	@property
	# there is probably somthing better we can do with generics but saying there arent
	# any will do for now
	def __type_params__(self):return ()
	@property
	def __doc__(self):return (
		"this is an overloaded function it has the following definitions:\n"+
		"\n".join([
			self.__name__+
			str(inspect.signature(fn.fn))+
			("" if (
				not hasattr(fn.fn, "__doc__") or
				not isinstance(fn.fn.__doc__, str) or
				len(fn.fn.__doc__.strip()) == 0
			) else ("\n\t"+fn.fn.__doc__.replace("\n", "\n\t")))
			for fn in self._functions
		])
	)
	def check_args(self, fn: _FnSig, args: list, kwargs: dict, typed: bool):
		params = list(fn.sig.parameters.items())

		# if the function takes no args and there are no args or kwargs return true
		if len(args) == 0 and len(kwargs) == 0 and len(params) == 0:return True

		var_pos = False

		param_i = 0
		for arg in args:
			# if there is a *args skip the rest of `args`
			if var_pos: break
			# if there is no coresponding param
			try: _, param = params[param_i]
			except IndexError:return False

			if param.kind not in [ # if we dont expect a positional argument
				Parameter.POSITIONAL_ONLY,
				Parameter.POSITIONAL_OR_KEYWORD,
				Parameter.VAR_POSITIONAL
			]:return False
			if typed and not are_type_compatible(
				arg,
				param.annotation,
				fn.fn,
				self._ns
			): return False
			# ignore extra positional args
			if param.kind == Parameter.VAR_POSITIONAL: var_pos = True
			param_i += 1

		if param_i < len(params):
			_, param = params[param_i]
			# if there is var pos but it takes no args
			if param.kind == Parameter.VAR_POSITIONAL:
				param_i += 1
				var_pos = True
			else: # these should be mutualy exclusive anyway
				while param.kind == Parameter.POSITIONAL_ONLY:
					# make sure that all the remaining positional only params have defaults
					if param.default == Parameter.empty: return False
					param_i += 1
					_, param = params[param_i]

		var_kw = False
		checked_kwargs = 0
		for name, param in params[param_i:]:
			# if arg is **kwargs ignore
			if param.kind ==  Parameter.VAR_KEYWORD:
				var_kw = True
				break
			if param.kind not in [
				Parameter.POSITIONAL_OR_KEYWORD,
				Parameter.KEYWORD_ONLY
			]: return False
			if name in kwargs:
				if typed and not are_type_compatible(
					kwargs[name],
					param.annotation,
					fn.fn,
					self._ns
				): return False
				checked_kwargs += 1
			elif param.default == Parameter.empty: return False

		return var_kw or len(kwargs) == checked_kwargs

	def choose(self, args: list, kwargs: dict):
		fns = self._functions
		if len(fns) == 1:return fns[0]
		fns = [fn for fn in fns if self.check_args(fn, args, kwargs, False)]
		if len(fns) == 1:return fns[0]
		# if there are still multiple fns check types to whittle it down more
		fns = [fn for fn in fns if self.check_args(fn, args, kwargs, True)]
		if len(fns) == 1:return fns[0]
		# if there are still multiple (or none) fns it means it is amibgous so fail
		raise OverloadSelectionError("TODO")
	def __get__(self, instance, owner):
		return self if instance is None else MethodType(self, instance)
	def __call__(self, *args, **kwargs):
		print("over", args)
		self.choose(args, kwargs).fn(*args, **kwargs)


if __name__ == "__main__":
	@overload
	def a()->None:
		"""this one prints 1st and returns none"""
		print("1st")
	@overload
	def a(a):print("2nd")
	@overload
	def a(a,b,*args):print("3rd")

	a()
	a(0)
	a(a=0)
	a(0,1,2,3,4,5)
	print(a.__doc__)
	#todo more tests