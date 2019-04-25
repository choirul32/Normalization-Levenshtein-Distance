import tweepy
import preprocessor as p
from string import punctuation
import re
import csv
punctuation =  re.sub("-", "…", punctuation)

class CrwTwitter():
	def __init__(self, consumer_key=None, consumer_secret=None, access_token=None, access_secret=None):
		if consumer_key != None:
			self.consumer_key = consumer_key
			self.consumer_secret = consumer_secret
			self.access_token = access_token
			self.access_secret = access_secret
		else:
			self.consumer_key = 'DmHd7uZy5Gr4g7trOOKqphuhW'
			self.consumer_secret = 'Xfjg012XcljlbmoPOFW4Rxw7hwI77ol06DAHCztaf2nssdjxVZ'
			self.access_token = '1951831687-aqX3J0MTGegdFQDdcRXiNUS8cN5dtWNWg9qOIAA'
			self.access_secret = 't2ObeFAUqVTZBS5eFN27aYK6e9K1VVHX2OIgCv4FHoCRJ'
		p.set_options(p.OPT.URL,p.OPT.MENTION,p.OPT.HASHTAG, p.OPT.RESERVED, p.OPT.EMOJI, p.OPT.SMILEY, p.OPT.NUMBER)
		self.resultDump = []
		self.slangword = self.loadSlangword("normalisasi/python/slang_word_list.csv")

	def authCon(self):
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_secret)
		api = tweepy.API(auth, wait_on_rate_limit=True)
		return api

	def crawlingToSentences(self, text, n ,clean=False):
		data = self.authCon()
		result = []
		for status in tweepy.Cursor(data.search, q=text,tweet_mode="extended", lang="in").items(n):
			result.append(status.full_text.lower())
		result_2 = []
		if clean==True:
			for text in result:
				result_2.append(self.preprocess(text))
			self.resultDump = result_2
			return result_2
		else:
			self.resultDump = result
			return result

	def loadCsv(self, filename):
	    lines = csv.reader(open(filename, "r"))
	    dataset = list(lines)
	    return dataset

	def loadSlangword(self, filename):
	    lines = csv.reader(open(filename, "r"))
	    dataset = dict(lines)
	    return dataset

	def saveToTxt(self):
		filetwitters = open("resultCrawling.txt", "w")
		for sentence in self.resultDump:
			filetwitters.write(sentence+'\n')
		filetwitters.close()

	def cleanRT(self, s):
		return re.sub(r'^rt[\s]+', '', s, flags=re.MULTILINE)

	def remove_punctuation(self, s):
		for t in list(punctuation):
			s = s.replace(t,'')
		return self.cleanRT(s)

	def preprocess(self, text):
		text = p.clean(text)
		#text = self.punctuationSpacing(text)
		text = self.remove_punctuation(text)
		text = " ".join(text.split())#menghilangkan spaci ganda
		text = text.replace(' - ', '-')#menggabungkan setelah dan sebelum tanda hubung
		text = re.sub(r'[^\x00-\x7F]+',' ', text)#menghapus karakter selain karakter ASCII
		text = self.looprepeat(text)
		text = self.replaceWithMeaning(text.split())
		return text

	def repeats(self, string):
		for x in range(1, len(string)):
			substring = string[:x]

			if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
				return re.sub(r'(.)\1+', r'\1\1', substring)#haaaaaaaaaaappppyyyy -> haappyy
				
		return re.sub(r'(.)\1+', r'\1\1', string)#haaaaaaaaaaappppyyyy -> haappyy

	def looprepeat(self, words):
		value = map(self.repeats, words.split())
		return " ".join(list(value))

	def replaceWithMeaning(self, words):
		new_words = []
		for i in words:
			if i in self.slangword.keys():
				new_words.append(self.slangword[i])
			else:
				new_words.append(i)

		return " ".join(new_words)


	