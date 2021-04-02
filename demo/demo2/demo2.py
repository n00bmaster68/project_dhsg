from ngrams import predict_main_word
# from TF_IDF_lib import get_name_of_object_in_image
from TF_IDF import get_name_of_object_in_image
import time
import random
from tabulate import tabulate

if __name__ == "__main__":
	
	f = open("../data1.txt") #data.txt
	lines = f.readlines()
	f.close()

	titles = []
	for line in lines:
		titles.append(line.strip('\n'))

	samples = []

	for i in range(1, 10):
		samples.append(random.sample(titles, int(len(titles)*10*i/100)))
	samples.append(titles)

	results = []
	headers = ["TF-IDF", "Time","N-GRAMS", "Time", "Percentage of data"]
	res = []

	for i in range (0, 10):	
		start1 = time.time()
		name1   = get_name_of_object_in_image(samples[i])
		p_time1 = time.time() - start1

		start2 = time.time()
		name2 = predict_main_word(samples[i])
		p_time2 = time.time() - start2

		name2 = name2.to_dict()
		name2 = list(name2.keys())
		# print("Key: ", name1, "|| time: ", p_time1)
		# print("Key: ", name2[0][0], "|| time: ", p_time2)
		res.append(name1)
		res.append(p_time1)
		res.append(name2[0][0])
		res.append(p_time2)
		res.append((i + 1)*10)
		results.append(res)
		res = []

	print(tabulate(results, headers=headers))
	# print(results)