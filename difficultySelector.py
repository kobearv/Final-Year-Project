from abstractSelector import AbstractSelector
class DifficultySelector(AbstractSelector):

	def __init__(self, MIN_DIFFICULTY=0.0, MAX_DIFFICULTY=float('inf')):
		self.MIN_DIFFICULTY = MIN_DIFFICULTY
		self.MAX_DIFFICULTY = MAX_DIFFICULTY

	def getPredicate(self, kwargs):
		min_difficulty = kwargs['min_difficulty'] if 'min_difficulty' in kwargs else self.MIN_DIFFICULTY
		max_difficulty = kwargs['max_difficulty'] if 'max_difficulty' in kwargs else self.MAX_DIFFICULTY
		def predicate(question):
			return min_difficulty <= question.getDifficulty() <= max_difficulty
		return predicate