from questionBank import QuestionBank

class SelectorContext:
	def __init__(self):
		self.context = None

	def setContext(self, context):
		self.context = context

	def selectQuestions(self, question_bank, **kwargs):
		if self.context:
			predicate = self.context.getPredicate(kwargs)
			return QuestionBank(filter(predicate, question_bank))