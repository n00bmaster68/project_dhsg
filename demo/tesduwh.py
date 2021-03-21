import os

for filename in os.listdir("test_img"):
	print(filename)


a = ['a', 'duwhuh', 'b', 'wduwhuiwhuihcd']

a = [i for i in a if len(i) > 1]

print(a)