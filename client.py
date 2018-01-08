from selectorContext import SelectorContext

from selectors import DifficultySelector
from selectors import KeywordsSelector
from selectors import MarksSelector

from questionBank import QuestionBank

from processText import ProcessText

def loadQuestionBank():
	# root_dir = input('Enter directory path: ')
	qb = QuestionBank('./bank')
	print('Loaded question bank')
	return qb

def reloadQBIfNeeded(qb):
	if not len(qb):
		choice = int(input('Question Bank is empty. Load it afresh again?\n1. Yes\n2.No\nEnter choice: '))
		if choice == 2:
			exit(0)
		else:
			qb = loadQuestionBank()
	return qb

if __name__ == '__main__':
	sc = SelectorContext()
	qb = loadQuestionBank()
	choice = 0
	while choice != 5:
		choice = int(input('\n\nSuccessively filter by:\n1. Marks\n2. Difficulty\n3. Keywords\n4. Write output into file\n5. Exit\n\nEnter choice: '))
		if choice == 1:
			min_mark = float(input('Enter the lower range: '))
			max_mark = float(input('Enter the upper range: '))
			sc.setContext(MarksSelector())
			qb = reloadQBIfNeeded(sc.selectQuestions(qb, min_marks=min_mark, max_marks=max_mark))

		elif choice == 2:
			mindif = float(input('Enter the minimum difficulty level: '))
			maxdif = float(input('Enter the maximum difficulty level: '))
			sc.setContext(DifficultySelector())
			qb = reloadQBIfNeeded(sc.selectQuestions(qb, max_difficulty=maxdif, min_difficulty=mindif))

		elif choice == 3:
			keywords = ProcessText.process(input('Enter space separated keywords to search for: '))
			sc.setContext(KeywordsSelector(THRESHOLD=2/3))
			qb = reloadQBIfNeeded(sc.selectQuestions(qb, keywords=keywords))

		elif choice == 4:
			qb.writeIntoFile(input('Enter filename to save in (default is "output"): '))
			break
		else:
			...