import abc

class AbstractSelector(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def getPredicate(self, kwargs):
		pass