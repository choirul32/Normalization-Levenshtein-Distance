train_file = 'OPUS_source_target.txt'
f = open(train_file, "r")
print(f.readlines().split(''))

data_ = list(datasetNon) + random_dataset_katabaku(datasetBaku, len(list(datasetNon)))
berhasil_baku = 0
gagal_baku = 0
berhasil_non = 0
gagal_non = 0

for i in data_:
	hasil = classifier.classify(word_features(i[0], 3))
	if hasil == i[1]:
		if i[1] == 'Baku':
			berhasil_baku += 1
		else:
			berhasil_non += 1
	elif hasil != i[1]:
		if i[1] == 'Baku':
			gagal_baku += 1
		else:
			gagal_non += 1

print("prediksi kata baku {0} dan kata tidak baku {1} BERHASIL".format(berhasil_baku, berhasil_non))
print("prediksi kata baku {0} dan kata tidak baku {1} GAGAL".format(gagal_baku, gagal_non))

def testClassification(text):
	#text = stemmer.stem(text)
	if classifier.classify(word_features(text))=='Baku':
		return "Kata Baku"
	else:
		#hasil = testNormalization(text)
		return "Tidak Baku"


	
