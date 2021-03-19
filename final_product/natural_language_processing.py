from collections import Counter
import math

stop_words = ['-', '|', '?', '...', '!', '1', '2', '3', '4', '5', '6', '7', '8', '9','.', ',', ';', ':','(', ')', '+', '*', '/', 'us', 'uk', "shouldn't", 'series', 'release', 'connect', 'etc', 'on', 'the', 'what', 'how', 'which', 'where', 'who', 'whom', 'whose', 'is', 'am', 'are', 'was', 'were', 'new', 'an',  'vs', 'these', 'why', 'it', 'about', 'needn', 'of', 'my', 'be', 'an', 'after', 'most', 'only', 'theirs', 'we', 'on', 'again', 'at', 're', 'up', 'that', 'are', 'while', 'been', 'or', 'there', 'above', "that'll", "it's", 'with', 'some', 'haven', "you'll", 'which', "you'd", 'below', "should've", 'am', 'than', 'ma', 'he', "you're", 'herself', 'through', 'themselves', 'they', 'if', 'she', 'have', 'until', 'yours', 'just', 'few', 'your', "you've", 'same', 'such', 'very', 'this', 'were', 'from', 'who', 'you', 'other', 'itself', 'having', 'once', 'here', 'will', 'now',  'should', 'when', 'ours', 'll', 'too', 'further', 'her', 'what', 'did', 'in', 'him', 'and', 'had', 'for', 'so', 'but', 'their', 'more', 'into', 'own', 'by', 'is', 'them', 'has', 'each', 'hers', 'our', 'ain', 'to', 'over', 'me', 'ourselves', 'yourself', 'during', 'how', 'does', 'whom', 'doing', 'between', 'shan', 'myself', 'because', 'do', 'the', 'any', 'where', 've', 'being', 'both', 'its', 'before', 'all', 'against', 'those', 'his', 'as', "she's", 'can', 'himself', 'yourselves', 'then']
stop_words = list(set(stop_words))

def tf (bag_of_word):
	max_key =  max(bag_of_word, key = bag_of_word.get)
	max_value = bag_of_word[max_key]
	tf_list = []

	for kw in bag_of_word:
		value = (bag_of_word[kw]/(max_value*1.0))
		tf_list.append(value)
	print(tf_list)

	return tf_list

def idf (titles, word):
	length = len(titles)
	count = 0
	
	for title in titles:
		if word in title:
			count += 1

	print(word,"  ", count, "  ", math.log(length*1.0/count, 10))
	return math.log(length*1.0/count, 10)

def tf_idf(titles, bag_of_word):
	processed_titles = []
	tf_idf_dict = {}
	tf_idf_list = []
	tf_list = tf(bag_of_word)
	idf_list = []

	for title in titles:
		processed_titles.append(title.lower())

	for word in bag_of_word:
		idf_list.append(idf(processed_titles, word))

	for i in range(len(tf_list)):
		tf_idf_list.append(tf_list[i]*idf_list[i])

	bag_of_word = list(bag_of_word)
	for (word, tf_idf_value) in zip (bag_of_word, tf_idf_list):
		tf_idf_dict[word] = tf_idf_value

	print (tf_idf_dict)
	return tf_idf_dict

def preprocess_data(titles):
	words = []
	for title in titles:
		words = words + title.split()

	bag_of_word = []
	for word in words:
		word = word.lower()
		flag = False
		if word in stop_words or word[-1] in stop_words or word[0] in stop_words:
			flag = True
		if flag == False:
			bag_of_word.append(word)

	bag_of_word = dict(Counter(bag_of_word))

	return bag_of_word

def get_name_of_object_in_image(titles):
	bag_of_word = preprocess_data(titles)

	tf_idf_dict = tf_idf(titles, bag_of_word)
	result_value = tf_idf_dict[min(tf_idf_dict, key = tf_idf_dict.get)]
	
	for key in tf_idf_dict:
		if tf_idf_dict[key] == result_value:
			print("Result: {}".format(key))
	