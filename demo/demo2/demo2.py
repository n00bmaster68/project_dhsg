from ngrams import predict_main_word
from crawl_titles import get_titles_on_web
from natural_language_processing import get_name_of_object_in_image
import time
import random

if __name__ == "__main__":
	
	f = open("large_data.txt")
	lines = f.readlines()
	f.close()

	titles = []
	for line in lines:
		titles.append(line.strip('\n'))
	# print(titles)

	start1 = time.time()
	name1   = get_name_of_object_in_image(titles)
	p_time1 = time.time() - start1

	start2 = time.time()
	name2 = predict_main_word(titles)
	p_time2 = time.time() - start2

	name2 = name2.to_dict()
	name2 = list(name2.keys())
	print("Key: ", name1, "|| time: ", p_time1)
	print("Key: ", name2[0][0], "|| time: ", p_time2)