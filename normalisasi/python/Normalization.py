try:
	from .CrwTwitter import CrwTwitter
except:
	from CrwTwitter import CrwTwitter
prep = CrwTwitter()
class LD:
	def __init__(self):
		self.words = self.openFile()

	def levenshteinDistance(self, s1, s2):
	    if len(s1) > len(s2):
	        s1, s2 = s2, s1

	    distances = range(len(s1) + 1)
	    for i2, c2 in enumerate(s2):
	        distances_ = [i2+1]
	        for i1, c1 in enumerate(s1):
	            if c1 == c2:
	                distances_.append(distances[i1])
	            else:
	                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
	        distances = distances_
	    return distances[-1]
	
	def find_closest_word(self, s, dictionary):
	    distances = []
	    for key in dictionary:
	        distance = self.levenshteinDistance(s, key)
	        #distance = qwerty_LD(s, key,1,1)
	        if distance < 3:
	            distances.append(key)
	    return distances

	def openFile(self, file="normalisasi/python/data.txt"):
		text_file = open(file, "r")
		lines = text_file.read().split()
		text_file.close()
		return lines

	def test_LDtoken(self, words):
		dic = self.openFile()
		result = []
		for key in words:
		    if key in dic:
		        result.append([key])
		    else:
		        result.append([key, self.find_closest_word(key, dic)])
		return result

	def test_LD(self, word):
		dic = self.openFile()
		result = []
		if word in dic:
			return [word]
		else:
			a = self.find_closest_word(word, dic)
			a.sort(key=len, reverse=True)
			
			return [word, a]

	def preprocessing(self, sent):
		
		return prep.preprocess(sent)

	
