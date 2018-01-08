from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

class ProcessText:
	@staticmethod
	def process(text):
		stop_words = set(stopwords.words('english'))
		porterStemmer = PorterStemmer()
		return set(\
			map(lambda token: porterStemmer.stem(token),\
				filter(lambda token: len(token) > 1 and token not in stop_words,\
					map(lambda token: token.lower(), word_tokenize(text)))))