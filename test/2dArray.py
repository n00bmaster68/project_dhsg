array = []
with open("2d.txt", "r") as f:
	for line in f.read().splitlines():
		line = line.split(' ')
		array.append(line)
f.close()
array = [list(map(int,i)) for i in array]
print(type(array[0][0]))