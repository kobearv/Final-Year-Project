from abstractSelector import AbstractSelector
class KeywordsSelector(AbstractSelector):

	def __init__(self, THRESHOLD=0.75):
		self.THRESHOLD = THRESHOLD

	def getPredicate(self, kwargs):
		keywords = kwargs['keywords'] if 'keywords' in kwargs else set()
		if not keywords:
			return lambda question: True
		no_of_keywords = len(keywords)
		def predicate(question):
			question_keywords = question.getKeywords()
			matched_keywords = set(filter(lambda keyword: keyword in question_keywords, keywords))
			match_count = len(matched_keywords)
			return match_count / no_of_keywords >= self.THRESHOLD
		return predicate