# from Normalization import LD

# a = LD()
# kalimat = a.preprocessing("diatur")
# print(a.test_LD(kalimat.split()))

# import StemmerFactory class
def repeats(string):
		for x in range(1, len(string)):
			substring = string[:x]

			if substring * (len(string)//len(substring))+(substring[:len(string)%len(substring)]) == string:
				return substring
				
		return string

def looprepeat(words):
	value = map(repeats, "wkwkwkwk saya dan pkpk".split())
	print(" ".join(list(value)))

import csv
def loadCsv(filename):
	lines = csv.reader(open(filename, "r"))
	dataset = dict(lines)
	return dataset

data = loadCsv("slang_word_list.csv")
for a in data.keys():
	print(a)
