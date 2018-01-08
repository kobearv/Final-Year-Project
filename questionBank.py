from question import Question
import os

class QuestionBank:
	def __init__(self, arg):
		self.questions = []
		# If arg is a directory path
		if type(arg) == str:
			self.dir_path = arg
			try:
				for dir_name, subdirs_list, files_list in os.walk(self.dir_path):
					print('Found directory: %s' % dir_name)
					for file_name in files_list:
						# print('\t%s' % file_name)
						try:
							with open(dir_name+'/'+file_name) as file_pointer:
								self.questions.append(Question(file_pointer))
						except:
							continue
			except:
				pass
		# If arg is a collection of questions
		else:
			iterable = arg
			try:
				for item in iterable:
					if type(item) == Question:
						self.questions.append(item)
			except:
				pass

	def __index__(self, index):
		return self.questions[index]

	def __iter__(self):
		return self.Iterator(self.questions)

	def __len__(self):
		return len(self.questions)

	def getQuestions(self):
		return self.questions

	def writeIntoFile(self, file_name):
		if not file_name:
			file_name = 'output'
		contents = ''
		count = 1
		sortedQuestions = sorted(self.questions, key = lambda question: question.getMarks())
		for question in sortedQuestions:
			contents += '%s. %s' % (count, question)
			count += 1
		open(file_name, 'w').write(contents)

	class Iterator:
		def __init__(self, iterable):
			self.iterable = iterable
			self.current_index = 0

		def __next__(self):
			try:
				self.current_index += 1
				return self.iterable[self.current_index-1]
			except:
				raise StopIteration