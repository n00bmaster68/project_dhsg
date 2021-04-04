import re
import unicodedata
import nltk
from nltk.corpus import stopwords
import pandas as pd 


def basic_clean(text):
	wnl = nltk.stem.WordNetLemmatizer() # đưa các từ về dạng cơ bản. Ví dụ: worked => work
	stopwords = nltk.corpus.stopwords.words('english') #load các stop words
	text = (unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore').lower()) #đưa các từ về lower case
	words = re.sub(r'[^\w\s]', '', text).split() #Bỏ các kí tự đặc biệt
	return [wnl.lemmatize(word) for word in words if word not in stopwords] #trả về các từ không trong stop words, đã được các kí tự đặc biệt và đưa từ về dạng cơ bản

def ngrams(sequence, n):
    history = []
    sequence = iter(sequence)
    while n > 1:
        try:
            next_item = next(sequence)
        except StopIteration:
            return
        history.append(next_item)
        n -= 1

    for item in sequence:
        history.append(item)
        yield tuple(history)
        del history[0]

def predict_main_word(titles):
	
	text = ""
	for title in titles:
		text += title.replace("\n", "") + " " #đưa tất cả titles vào text
	clean_text = basic_clean(text)
	return (pd.Series(ngrams(clean_text, 1)).value_counts())[:1] #tiền xử lí text qua hàm basic_clean, sau đó sử dụng nrams để lấy ra từ có trọng số lớn nhất.
