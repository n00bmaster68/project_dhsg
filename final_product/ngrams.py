import re
import unicodedata
import nltk
from nltk.corpus import stopwords
import pandas as pd 

import matplotlib.pyplot as plt

def basic_clean(text):
	wnl = nltk.stem.WordNetLemmatizer()
	stopwords = nltk.corpus.stopwords.words('english')
	text = (unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore').lower())
	words = re.sub(r'[^\w\s]', '', text).split()
	return [wnl.lemmatize(word) for word in words if word not in stopwords]

def predict_main_word(titles):
	text = ""
	for title in titles:
		text += title.replace("\n", "") + " "
	return (pd.Series(nltk.ngrams(basic_clean(text), 1)).value_counts())[:10]
