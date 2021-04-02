import numpy as np
import matplotlib.pyplot as plt
 
# set width of bars
barWidth = 0.25
 
# set heights of bars
bars1 = [12, 30, 1, 8, 22]
bars2 = [28, 6, 16, 5, 10]
 
# Set position of bar on X axis
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Make the plot
plt.bar(r1, bars1, color='#7f6d5f', width=barWidth, edgecolor='white', label='N-GRAMS')
plt.bar(r2, bars2, color='#557f2d', width=barWidth, edgecolor='white', label='TFIDF')
 
# Add xticks on the middle of the group bars
plt.xlabel('Methods', fontweight='bold')
plt.xticks([r + barWidth for r in range(len(bars1))], ['A', 'B', 'C', 'D', 'E'])
 
# Create legend & Show graphic
plt.legend()	
plt.show()

# from collections import Counter
# test = ['a', 'a', 'b']
# elements_count = Counter(test)
# print(elements_count)