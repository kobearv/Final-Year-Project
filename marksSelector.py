from abstractSelector import AbstractSelector
class MarksSelector(AbstractSelector):

	def __init__(self, MIN_MARKS=0.0, MAX_MARKS=float('inf')):
		self.MIN_MARKS = MIN_MARKS
		self.MAX_MARKS = MAX_MARKS

	def getPredicate(self, kwargs):
		min_marks = kwargs['min_marks'] if 'min_marks' in kwargs else self.MIN_MARKS
		max_marks = kwargs['max_marks'] if 'max_marks' in kwargs else self.MAX_MARKS
		def predicate(question):
			return min_marks <= question.getMarks() <= max_marks
		return predicate