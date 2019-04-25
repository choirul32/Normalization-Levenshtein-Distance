from django.shortcuts import render, render_to_response
from django.template import loader, RequestContext
from django.http import HttpResponse
from .python.Normalization import LD

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

context = {
	'input':'',
	'input_split':'',
	'output_norm':'',
}

#clasy = Classifier()
#clasy.trainClassifier()
# ========== init Normalization ==========
norm = LD()

def index(request):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		text = request.POST['your-text']
		#classifier_ = clasy.testClassifier(text_)
		text_prep = norm.preprocessing(text)
		text_ = text_prep.lower()
		output = stemmer.stem(text_)
		text_ = text_.split().copy()
		output = output.split()
		normalize_ = []
		for a, b in zip(text_, output):
			if a != b:
				normalize_.append([a])
			else:
				normalize_.append(norm.test_LD(a))

			
		'''
		input_split = []
		output_1 = []
		output_2 = []
		list_text = text_.split()
		for i, j in enumerate(classifier_):
				input_split.append([list_text[i]])
				output_1.append(j)
				output_2.append(normalize_[list_text[i]])
		
		context['input_split'] = input_split
		context['output_classy'] = output_1
		
		'''
		context['input'] = text
		context['output_norm'] = normalize_
	
	return render(request, 'normalisasi.html', context)
'''
def index(request):
	if request.method == 'GET':
		pass
	elif request.method == 'POST':
		text_ = request.POST['your-text']
		classifier_ = clasy.testClassifier(text_)
		normalize_ = norm.Normalize(text_)
		results = []
		list_text = text_.split()
		for i, j in enumerate(classifier_):
			if j == True:
				results.append([list_text[i], "Prediksi Baku"])
			else:
				results.append([list_text[i], j] + normalize_[list_text[i]])
		context['hasil'] = results
		context['text'] = text_
	return render(request, 'normalisasi.html', context)
'''
def process(request):
	return render(request, 'normalisasi.html')


