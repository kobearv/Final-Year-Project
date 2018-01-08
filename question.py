import re
from processText import ProcessText

class Question:
	def __init__(self, file_pointer):
		file_contents = file_pointer.read()
		
		self.question = re.search('(?<=Question:)(.|\n)*(?=Marks:)', file_contents).group().strip()
		if not self.question:
			raise Exception
		self.marks = float(re.search('(?<=Marks:)(.|\n)*(?=Difficulty:)', file_contents).group().strip())
		self.difficulty = float(re.search('(?<=Difficulty:)(.|\n)*', file_contents).group().strip())
		self.keywords = ProcessText.process(self.question)

	def __str__(self):
		return 'Marks: %s\tDifficulty: %s\n\n%s\n\n' % (self.marks, self.difficulty, self.question)

	def getQuestion(self):
		return self.question

	def getDifficulty(self):
		return self.difficulty

	def getMarks(self):
		return self.marks

	def getKeywords(self):
		return self.keywords