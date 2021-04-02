from collections import Counter
import math

f = open("stop_words.txt.txt") #data.txt
lines = f.readlines()
f.close()

stop_words = []
for line in lines:
	stop_words.append(line.strip('\n'))

tf_dict = {}
idf_dict = {}
processed_titles = []

def getMaxFrequency(title):
	words = title.split()
	dictWord = {}

	for word in words:
		dictWord[word] = 0
	for word in words:
		dictWord[word] += 1

	return max(dictWord.values())

def tf (title):
	max_value = getMaxFrequency(title)

	elements_count = Counter(title.split())
	for key, value in elements_count.items():
		tf_dict[key] += value/max_value

def idf (titles, word):
	length = len(titles)
	count = 0

	for title in titles:
		if word in title:
			count += 1

	idf_dict[word] = math.log(length*1.0/(count + 1), 10)
	# return math.log(length*1.0/count, 10)

def tf_idf(titles):
	tf_idf_dict = {}

	for title in processed_titles:
		tf(title)

	for word in tf_dict.keys():
		idf(titles, word)

	for word in tf_dict.keys():
		tf_idf_dict[word] = tf_dict[word]*idf_dict[word]

	return tf_idf_dict

def preprocess_titles(titles):
	sen = ""
	print(titles)
	global processed_titles

	for title in titles:
		for word in title.split():
			if len(word) >= 3 and word not in stop_words and word[:-1] not in stop_words:
				sen += word.lower() + " "
		processed_titles.append("".join(sen.rstrip().lstrip()))
		sen = ""


def preprocess_data(titles):
	preprocess_titles(titles)
	global tf_dict
	global idf_dict

	words = []
	for title in processed_titles:
		words = words + title.split()

	tf_dict = dict.fromkeys(words, 0) 
	idf_dict = dict.fromkeys(words, 0) 
	# print(idf_dict)

def get_name_of_object_in_image(titles):
	preprocess_data(titles)
	# print("processed_titles", processed_titles)

	tf_idf_dict = tf_idf(titles)
	result_value = tf_idf_dict[min(tf_idf_dict, key = tf_idf_dict.get)]
	
	for key in tf_idf_dict:
		if tf_idf_dict[key] == result_value:
			return key

str1 = "Seals are something ugly, fat"
str2 = "seals are so cool"

test = []
test.append(str1)
test.append(str2)

print(get_name_of_object_in_image(test))